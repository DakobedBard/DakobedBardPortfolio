package org.mddarr.dakobedordersservice.dynamo;

import com.amazonaws.services.dynamodbv2.document.DynamoDB;
import com.amazonaws.services.dynamodbv2.document.Item;
import com.amazonaws.services.dynamodbv2.document.Table;
import com.amazonaws.services.dynamodbv2.model.*;
import com.fasterxml.jackson.core.JsonFactory;
import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class ProductsTable {
    public static void createProductsTable(DynamoDB dynamoDB){
        String tableName = "Dakobed-Products";

        try {
            List<AttributeDefinition> attributeDefinitions = new ArrayList<AttributeDefinition>();
            attributeDefinitions.add(new AttributeDefinition().withAttributeName("id").withAttributeType("S"));
//            attributeDefinitions.add(new AttributeDefinition().withAttributeName("price").withAttributeType("N"));
            List<KeySchemaElement> keySchema = new ArrayList<KeySchemaElement>();
            keySchema.add(new KeySchemaElement().withAttributeName("id").withKeyType(KeyType.HASH));
//            keySchema.add(new KeySchemaElement().withAttributeName("price").withKeyType(KeyType.RANGE));

            CreateTableRequest request = new CreateTableRequest()
                    .withTableName(tableName)
                    .withKeySchema(keySchema)
                    .withAttributeDefinitions(attributeDefinitions)
                    .withProvisionedThroughput(new ProvisionedThroughput()
                            .withReadCapacityUnits(5L)
                            .withWriteCapacityUnits(6L));

            Table table = dynamoDB.createTable(request);
            table.waitForActive();

        } catch (Exception e) {
            {
                System.err.println("Unable to create table: ");
                System.err.println(e.getMessage());
            }
        }
    }


    public static void loadProductsData(DynamoDB dynamoDB) throws IOException {

        Table table = dynamoDB.getTable("Dakobed-Products");
        JsonParser parser = new JsonFactory().createParser(new File("/data/mddarr/Dakobed/dakobed-product-service/src/main/resources/products.json"));
        JsonNode rootNode = new ObjectMapper().readTree(parser);
        Iterator<JsonNode> iter = rootNode.iterator();
        ObjectNode currentNode;

        while (iter.hasNext()) {

            currentNode = (ObjectNode) iter.next();
            double price = currentNode.path("price").asDouble();
            String productName = currentNode.path("productName").asText();
            String imageURL = currentNode.path("image_url").asText();
            String id = currentNode.path("productID").asText();

            try {
                table.putItem(new Item().withPrimaryKey("id", id, "price", price)
                        .withString("productName",productName).withString("imageURL",imageURL));
                System.out.println("PutItem succeeded: " + price + " " + productName);
            }
            catch (Exception e) {
                System.err.println("Unable to add product: " + price + " " + productName + " " + imageURL);
                System.err.println(e.getMessage());
                break;
            }
        }
        parser.close();
    }

}
