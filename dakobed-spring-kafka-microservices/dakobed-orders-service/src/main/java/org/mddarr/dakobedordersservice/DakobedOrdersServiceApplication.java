package org.mddarr.dakobedordersservice;

import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBMapper;
import com.amazonaws.services.dynamodbv2.document.*;
import com.amazonaws.services.dynamodbv2.document.spec.QuerySpec;
import com.amazonaws.services.dynamodbv2.document.utils.ValueMap;
import com.amazonaws.services.dynamodbv2.model.*;
import com.fasterxml.jackson.core.JsonFactory;
import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import org.joda.time.DateTime;
import org.joda.time.DateTimeZone;
import org.mddarr.dakobedordersservice.dynamo.OrdersTable;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.UUID;


@SpringBootApplication
public class DakobedOrdersServiceApplication implements CommandLineRunner {


	private DynamoDBMapper dynamoDBMapper;

	private static final Logger logger = LogManager.getLogger(DakobedOrdersServiceApplication.class);

	@Autowired
	private AmazonDynamoDB amazonDynamoDB;
	private static String tableName = "Dakobed-Orders";

//	private static String tableName = "gsi-example";

	public static void main(String[] args) {
		SpringApplication.run(DakobedOrdersServiceApplication.class, args);
	}

	public void createOrdersTable(DynamoDB dynamoDB){
		try {
			ArrayList<AttributeDefinition> attributeDefinitions = new ArrayList<AttributeDefinition>();

			attributeDefinitions.add(new AttributeDefinition()
					.withAttributeName("orderID")
					.withAttributeType("S"));
			attributeDefinitions.add(new AttributeDefinition()
					.withAttributeName("Date")
					.withAttributeType("S"));
			attributeDefinitions.add(new AttributeDefinition()
					.withAttributeName("Price")
					.withAttributeType("N"));

// Table key schema
			ArrayList<KeySchemaElement> tableKeySchema = new ArrayList<KeySchemaElement>();
			tableKeySchema.add(new KeySchemaElement()
					.withAttributeName("orderID")
					.withKeyType(KeyType.HASH));  //Partition key
			tableKeySchema.add(new KeySchemaElement()
					.withAttributeName("Date")
					.withKeyType(KeyType.RANGE));  //Sort key

// PrecipIndex
			GlobalSecondaryIndex precipIndex = new GlobalSecondaryIndex()
					.withIndexName("Price")
					.withProvisionedThroughput(new ProvisionedThroughput()
							.withReadCapacityUnits((long) 10)
							.withWriteCapacityUnits((long) 1))
					.withProjection(new Projection().withProjectionType(ProjectionType.ALL));

			ArrayList<KeySchemaElement> indexKeySchema = new ArrayList<KeySchemaElement>();

			indexKeySchema.add(new KeySchemaElement()
					.withAttributeName("Date")
					.withKeyType(KeyType.HASH));  //Partition key
			indexKeySchema.add(new KeySchemaElement()
					.withAttributeName("Price")
					.withKeyType(KeyType.RANGE));  //Sort key

			precipIndex.setKeySchema(indexKeySchema);

			CreateTableRequest createTableRequest = new CreateTableRequest()
					.withTableName("Dakobed-Orders")
					.withProvisionedThroughput(new ProvisionedThroughput()
							.withReadCapacityUnits((long) 5)
							.withWriteCapacityUnits((long) 1))
					.withAttributeDefinitions(attributeDefinitions)
					.withKeySchema(tableKeySchema)
					.withGlobalSecondaryIndexes(precipIndex);
			Table table = dynamoDB.createTable(createTableRequest);
			System.out.println(table.getDescription());

		}catch (Exception e){
			e.printStackTrace();
		}
	}


	public void LoadOrdersData(DynamoDB dynamoDB) throws IOException {

		Table table = dynamoDB.getTable("Dakobed-Orders");
		JsonParser parser = new JsonFactory().createParser(new File("/data/mddarr/Dakobed/dakobed-orders-service/src/main/resources/orders.json"));
		JsonNode rootNode = new ObjectMapper().readTree(parser);
		Iterator<JsonNode> iter = rootNode.iterator();
		ObjectNode currentNode;
		int count = 0;
		while (iter.hasNext()) {

			currentNode = (ObjectNode) iter.next();
			double price = currentNode.path("price").asDouble();
			long order_time = currentNode.path("order_time").asLong();
			String productName = currentNode.path("productName").asText();


//			String customerId = currentNode.path("customerId").asText();
//			long quantity = currentNode.path("quantity").asLong();
//			String state = currentNode.path("state").asText();

			DateTime date = new DateTime(Long.valueOf(order_time * 1000L), DateTimeZone.UTC);
			System.out.println("The date at which the oder occurs is " + date.toString());
			try {
				table.putItem(new Item().withPrimaryKey("orderID", UUID.randomUUID().toString(), "Date", date.toString())
						.withDouble("price",price));
				System.err.println("added product: " + price + " " + productName );
				System.out.println("PutItem succeeded: " + price + " " + productName);
			}
			catch (Exception e) {
				System.err.println("Unable to add product: " + price + " " + productName );
				System.err.println(e.getMessage());
				break;
			}
			count +=1;
		}
		parser.close();
	}


	public static void query(String indexName, DynamoDB dynamoDB ) {

		Table table = dynamoDB.getTable(tableName);

		System.out.println("\n***********************************************************\n");
		System.out.println("Querying table " + tableName + "...");

		QuerySpec querySpec = new QuerySpec().withConsistentRead(true).withScanIndexForward(true)
				.withReturnConsumedCapacity(ReturnConsumedCapacity.TOTAL);

		if (indexName == "IsOpenIndex") {

			System.out.println("\nUsing index: '" + indexName + "': Bob's orders that are open.");
			System.out.println("Only a user-specified list of attributes are returned\n");
			Index index = table.getIndex(indexName);

			querySpec.withKeyConditionExpression("CustomerId = :v_custid and IsOpen = :v_isopen")
					.withValueMap(new ValueMap().withString(":v_custid", "bob@example.com").withNumber(":v_isopen", 1));

			querySpec.withProjectionExpression("OrderCreationDate, ProductCategory, ProductName, OrderStatus");

			ItemCollection<QueryOutcome> items = index.query(querySpec);
			Iterator<Item> iterator = items.iterator();

			System.out.println("Query: printing results...");

			while (iterator.hasNext()) {
				System.out.println(iterator.next().toJSONPretty());
			}

		}
		else if (indexName == "OrderCreationDateIndex") {
			System.out.println("\nUsing index: '" + indexName + "': Bob's orders that were placed after 01/31/2015.");
			System.out.println("Only the projected attributes are returned\n");
			Index index = table.getIndex(indexName);

			querySpec.withKeyConditionExpression("CustomerId = :v_custid and OrderCreationDate >= :v_orddate")
					.withValueMap(
							new ValueMap().withString(":v_custid", "bob@example.com").withNumber(":v_orddate", 20150131));

			querySpec.withSelect(Select.ALL_PROJECTED_ATTRIBUTES);

			ItemCollection<QueryOutcome> items = index.query(querySpec);
			Iterator<Item> iterator = items.iterator();

			System.out.println("Query: printing results...");

			while (iterator.hasNext()) {
				System.out.println(iterator.next().toJSONPretty());
			}

		}
		else {
			System.out.println("\nNo index: All of Bob's orders, by OrderId:\n");

			querySpec.withKeyConditionExpression("CustomerId = :v_custid")
					.withValueMap(new ValueMap().withString(":v_custid", "bob@example.com"));

			ItemCollection<QueryOutcome> items = table.query(querySpec);
			Iterator<Item> iterator = items.iterator();

			System.out.println("Query: printing results...");

			while (iterator.hasNext()) {
				System.out.println(iterator.next().toJSONPretty());
			}

		}

	}

	public static void deleteTable(String tableName,  DynamoDB dynamoDB) {

		Table table = dynamoDB.getTable(tableName);
		System.out.println("Deleting table " + tableName + "...");
		table.delete();

		// Wait for table to be deleted
		System.out.println("Waiting for " + tableName + " to be deleted...");
		try {
			table.waitForDelete();
		}
		catch (InterruptedException e) {
			e.printStackTrace();
		}
	}


	@Override
	public void run(String... strings) throws Exception {
		DynamoDB dynamoDB = new DynamoDB(amazonDynamoDB);
		try {
			OrdersTable.createTable(dynamoDB);
		}catch (Exception e){}

		try {
			OrdersTable.loadOrdersData(dynamoDB);
		}catch(Exception e){e.printStackTrace();}
//	public Boolean isEmpty(AmazonDynamoDB database, String table) {
//		ScanRequest scanRequest = new ScanRequest().withTableName(table).withLimit(1);
//		return database.scan(scanRequest).getScannedCount() == 0;
//	}
//
//	public static void createTable(DynamoDB dynamoDB) {
//		String tableName = "gsi-example";
//		// Attribute definitions
//		ArrayList<AttributeDefinition> attributeDefinitions = new ArrayList<AttributeDefinition>();
//
//		attributeDefinitions.add(new AttributeDefinition().withAttributeName("IssueId").withAttributeType("S"));
//		attributeDefinitions.add(new AttributeDefinition().withAttributeName("Title").withAttributeType("S"));
//		attributeDefinitions.add(new AttributeDefinition().withAttributeName("CreateDate").withAttributeType("S"));
//		attributeDefinitions.add(new AttributeDefinition().withAttributeName("DueDate").withAttributeType("S"));
//
//		// Key schema for table
//		ArrayList<KeySchemaElement> tableKeySchema = new ArrayList<KeySchemaElement>();
//		tableKeySchema.add(new KeySchemaElement().withAttributeName("IssueId").withKeyType(KeyType.HASH)); // Partition
//		// key
//		tableKeySchema.add(new KeySchemaElement().withAttributeName("Title").withKeyType(KeyType.RANGE)); // Sort
//		// key
//
//		// Initial provisioned throughput settings for the indexes
//		ProvisionedThroughput ptIndex = new ProvisionedThroughput().withReadCapacityUnits(1L)
//				.withWriteCapacityUnits(1L);
//
//		// CreateDateIndex
//		GlobalSecondaryIndex createDateIndex = new GlobalSecondaryIndex().withIndexName("CreateDateIndex")
//				.withProvisionedThroughput(ptIndex)
//				.withKeySchema(new KeySchemaElement().withAttributeName("CreateDate").withKeyType(KeyType.HASH), // Partition
//						// key
//						new KeySchemaElement().withAttributeName("IssueId").withKeyType(KeyType.RANGE)) // Sort
//				// key
//				.withProjection(
//						new Projection().withProjectionType("INCLUDE").withNonKeyAttributes("Description", "Status"));
//
//		// TitleIndex
//		GlobalSecondaryIndex titleIndex = new GlobalSecondaryIndex().withIndexName("TitleIndex")
//				.withProvisionedThroughput(ptIndex)
//				.withKeySchema(new KeySchemaElement().withAttributeName("Title").withKeyType(KeyType.HASH), // Partition
//						// key
//						new KeySchemaElement().withAttributeName("IssueId").withKeyType(KeyType.RANGE)) // Sort
//				// key
//				.withProjection(new Projection().withProjectionType("KEYS_ONLY"));
//
//		// DueDateIndex
//		GlobalSecondaryIndex dueDateIndex = new GlobalSecondaryIndex().withIndexName("DueDateIndex")
//				.withProvisionedThroughput(ptIndex)
//				.withKeySchema(new KeySchemaElement().withAttributeName("DueDate").withKeyType(KeyType.HASH)) // Partition
//				// key
//				.withProjection(new Projection().withProjectionType("ALL"));
//
//		CreateTableRequest createTableRequest = new CreateTableRequest().withTableName(tableName)
//				.withProvisionedThroughput(
//						new ProvisionedThroughput().withReadCapacityUnits((long) 1).withWriteCapacityUnits((long) 1))
//				.withAttributeDefinitions(attributeDefinitions).withKeySchema(tableKeySchema)
//				.withGlobalSecondaryIndexes(createDateIndex, titleIndex, dueDateIndex);
//
//		System.out.println("Creating table " + tableName + "...");
//		dynamoDB.createTable(createTableRequest);
//
//		// Wait for table to become active
//		System.out.println("Waiting for " + tableName + " to become ACTIVE...");
//		try {
//			Table table = dynamoDB.getTable(tableName);
//			table.waitForActive();
//		}
//		catch (InterruptedException e) {
//			e.printStackTrace();
//		}
//	}
//
//	public static void queryIndex(String indexName, DynamoDB dynamoDB) {
//
//		Table table = dynamoDB.getTable(tableName);
//
//		System.out.println("\n***********************************************************\n");
//		System.out.print("Querying index " + indexName + "...");
//
//		Index index = table.getIndex(indexName);
//
//		ItemCollection<QueryOutcome> items = null;
//
//		QuerySpec querySpec = new QuerySpec();
//
//		if (indexName == "CreateDateIndex") {
//			System.out.println("Issues filed on 2013-11-01");
//			querySpec.withKeyConditionExpression("CreateDate = :v_date and begins_with(IssueId, :v_issue)")
//					.withValueMap(new ValueMap().withString(":v_date", "2013-11-01").withString(":v_issue", "A-"));
//			items = index.query(querySpec);
//		}
//		else if (indexName == "TitleIndex") {
//			System.out.println("Compilation errors");
//			querySpec.withKeyConditionExpression("Title = :v_title and begins_with(IssueId, :v_issue)")
//					.withValueMap(new ValueMap().withString(":v_title", "Compilation error").withString(":v_issue", "A-"));
//			items = index.query(querySpec);
//		}
//		else if (indexName == "DueDateIndex") {
//			System.out.println("Items that are due on 2013-11-30");
//			querySpec.withKeyConditionExpression("DueDate = :v_date")
//					.withValueMap(new ValueMap().withString(":v_date", "2013-11-30"));
//			items = index.query(querySpec);
//		}
//		else {
//			System.out.println("\nNo valid index name provided");
//			return;
//		}
//
//		Iterator<Item> iterator = items.iterator();
//
//		System.out.println("Query: printing results...");
//
//		while (iterator.hasNext()) {
//			System.out.println(iterator.next().toJSONPretty());
//		}
//
//	}
//
//	public static void deleteTable(String tableName, DynamoDB dynamoDB) {
//
//		System.out.println("Deleting table " + tableName + "...");
//
//		Table table = dynamoDB.getTable(tableName);
//		table.delete();
//
//		// Wait for table to be deleted
//		System.out.println("Waiting for " + tableName + " to be deleted...");
//		try {
//			table.waitForDelete();
//		}
//		catch (InterruptedException e) {
//			e.printStackTrace();
//		}
//	}
//
//	public static void loadData(DynamoDB dynamoDB) {
//
//		System.out.println("Loading data into table " + tableName + "...");
//
//		// IssueId, Title,
//		// Description,
//		// CreateDate, LastUpdateDate, DueDate,
//		// Priority, Status
//
//		putItem("A-101", "Compilation error", "Can't compile Project X - bad version number. What does this mean?",
//				"2013-11-01", "2013-11-02", "2013-11-10", 1, "Assigned", dynamoDB);
//		putItem("A-102", "Can't read data file", "The main data file is missing, or the permissions are incorrect",
//				"2013-11-01", "2013-11-04", "2013-11-30", 2, "In progress", dynamoDB);
//		putItem("A-103", "Test failure", "Functional test of Project X produces errors", "2013-11-01", "2013-11-02",
//				"2013-11-10", 1, "In progress", dynamoDB);
//		putItem("A-104", "Compilation error", "Variable 'messageCount' was not initialized.", "2013-11-15",
//				"2013-11-16", "2013-11-30", 3, "Assigned", dynamoDB);
//		putItem("A-105", "Network issue", "Can't ping IP address 127.0.0.1. Please fix this.", "2013-11-15",
//				"2013-11-16", "2013-11-19", 5, "Assigned", dynamoDB);
//
//	}
//
//	public static void putItem(String issueId, String title, String description, String createDate, String lastUpdateDate, String dueDate,
//			Integer priority, String status,DynamoDB dynamoDB) {
//
//		Table table = dynamoDB.getTable(tableName);
//
//		Item item = new Item().withPrimaryKey("IssueId", issueId).withString("Title", title)
//				.withString("Description", description).withString("CreateDate", createDate)
//				.withString("LastUpdateDate", lastUpdateDate).withString("DueDate", dueDate)
//				.withNumber("Priority", priority).withString("Status", status);
//
//		table.putItem(item);
//	}

//
//	public static void createTable( DynamoDB dynamoDB) {
//
//		CreateTableRequest createTableRequest = new CreateTableRequest().withTableName(tableName)
//				.withProvisionedThroughput(
//						new ProvisionedThroughput().withReadCapacityUnits((long) 1).withWriteCapacityUnits((long) 1));
//
//		// Attribute definitions for table partition and sort keys
//		ArrayList<AttributeDefinition> attributeDefinitions = new ArrayList<AttributeDefinition>();
//		attributeDefinitions.add(new AttributeDefinition().withAttributeName("CustomerId").withAttributeType("S"));
//		attributeDefinitions.add(new AttributeDefinition().withAttributeName("OrderId").withAttributeType("N"));
//
//		// Attribute definition for index primary key attributes
//		attributeDefinitions
//				.add(new AttributeDefinition().withAttributeName("OrderCreationDate").withAttributeType("N"));
//		attributeDefinitions.add(new AttributeDefinition().withAttributeName("IsOpen").withAttributeType("N"));
//
//		createTableRequest.setAttributeDefinitions(attributeDefinitions);
//
//		// Key schema for table
//		ArrayList<KeySchemaElement> tableKeySchema = new ArrayList<KeySchemaElement>();
//		tableKeySchema.add(new KeySchemaElement().withAttributeName("CustomerId").withKeyType(KeyType.HASH)); // Partition
//		// key
//		tableKeySchema.add(new KeySchemaElement().withAttributeName("OrderId").withKeyType(KeyType.RANGE)); // Sort
//		// key
//
//		createTableRequest.setKeySchema(tableKeySchema);
//
//		ArrayList<LocalSecondaryIndex> localSecondaryIndexes = new ArrayList<LocalSecondaryIndex>();
//
//		// OrderCreationDateIndex
//		LocalSecondaryIndex orderCreationDateIndex = new LocalSecondaryIndex().withIndexName("OrderCreationDateIndex");
//
//		// Key schema for OrderCreationDateIndex
//		ArrayList<KeySchemaElement> indexKeySchema = new ArrayList<KeySchemaElement>();
//		indexKeySchema.add(new KeySchemaElement().withAttributeName("CustomerId").withKeyType(KeyType.HASH)); // Partition
//		// key
//		indexKeySchema.add(new KeySchemaElement().withAttributeName("OrderCreationDate").withKeyType(KeyType.RANGE)); // Sort
//		// key
//
//		orderCreationDateIndex.setKeySchema(indexKeySchema);
//
//		// Projection (with list of projected attributes) for
//		// OrderCreationDateIndex
//		Projection projection = new Projection().withProjectionType(ProjectionType.INCLUDE);
//		ArrayList<String> nonKeyAttributes = new ArrayList<String>();
//		nonKeyAttributes.add("ProductCategory");
//		nonKeyAttributes.add("ProductName");
//		projection.setNonKeyAttributes(nonKeyAttributes);
//
//		orderCreationDateIndex.setProjection(projection);
//
//		localSecondaryIndexes.add(orderCreationDateIndex);
//
//		// IsOpenIndex
//		LocalSecondaryIndex isOpenIndex = new LocalSecondaryIndex().withIndexName("IsOpenIndex");
//
//		// Key schema for IsOpenIndex
//		indexKeySchema = new ArrayList<KeySchemaElement>();
//		indexKeySchema.add(new KeySchemaElement().withAttributeName("CustomerId").withKeyType(KeyType.HASH)); // Partition
//		// key
//		indexKeySchema.add(new KeySchemaElement().withAttributeName("IsOpen").withKeyType(KeyType.RANGE)); // Sort
//		// key
//
//		// Projection (all attributes) for IsOpenIndex
//		projection = new Projection().withProjectionType(ProjectionType.ALL);
//
//		isOpenIndex.setKeySchema(indexKeySchema);
//		isOpenIndex.setProjection(projection);
//
//		localSecondaryIndexes.add(isOpenIndex);
//
//		// Add index definitions to CreateTable request
//		createTableRequest.setLocalSecondaryIndexes(localSecondaryIndexes);
//
//		System.out.println("Creating table " + tableName + "...");
//		System.out.println(dynamoDB.createTable(createTableRequest));
//
//		// Wait for table to become active
//		System.out.println("Waiting for " + tableName + " to become ACTIVE...");
//		try {
//			Table table = dynamoDB.getTable(tableName);
//			table.waitForActive();
//		}
//		catch (InterruptedException e) {
//			e.printStackTrace();
//		}
//	}


//		try {
//			OrdersTable.createTable(dynamoDB);
//		}catch(Exception e){
//			e.printStackTrace();
//		}
//		query("IsOpenIndex",dynamoDB);
//		System.out.println("querying on ");
//		query("OrderCreationDateIndex", dynamoDB);
		//
//		try {
//			loadData(dynamoDB);
//		}catch (Exception e){
//			e.printStackTrace();
//		}
		//
//		queryIndex("CreateDateIndex",dynamoDB);
//		queryIndex("TitleIndex", dynamoDB);
//		queryIndex("DueDateIndex", dynamoDB);

//		createOrdersTable(dynamoDB);
//
//		if(isEmpty(amazonDynamoDB,"Dakobed-Orders")){
//			LoadOrdersData(dynamoDB);
//		}
	}
}
