package org.mddarr.dakobedordersservice.services;


import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBMapper;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBMapperConfig;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBQueryExpression;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBScanExpression;
import com.amazonaws.services.dynamodbv2.document.*;
import com.amazonaws.services.dynamodbv2.document.spec.QuerySpec;
import com.amazonaws.services.dynamodbv2.document.utils.ValueMap;
import com.amazonaws.services.dynamodbv2.model.AttributeValue;
import com.amazonaws.services.dynamodbv2.model.ReturnConsumedCapacity;
import com.amazonaws.services.dynamodbv2.model.Select;
import org.joda.time.DateTime;
import org.joda.time.DateTimeZone;
import org.mddarr.dakobedordersservice.beans.OrderDTO;
import org.mddarr.dakobedordersservice.models.OrderDocument;
import org.mddarr.dakobedordersservice.models.OrderEntity;
import org.mddarr.dakobedordersservice.models.OrderRequest;
import org.mddarr.dakobedordersservice.models.OrderResponse;
import org.mddarr.dakobedordersservice.port.OrderServicePublish;
import org.mddarr.orders.event.dto.Order;
import org.mddarr.orders.event.dto.OrderState;
import org.mddarr.products.Product;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

import java.util.*;

@Service
public class OrderService {
    @Autowired
    AmazonDynamoDB amazonDynamoDB;

    @Autowired
    OrdersAvroProducer producer;


    @Autowired
    KafkaTemplate<String, Product> kafkaTemplateProduct;
    private static final Logger logger = LoggerFactory.getLogger(OrderService.class);

    public OrderResponse postOrder(OrderRequest orderRequest){
        DynamoDB dynamoDB = new DynamoDB(amazonDynamoDB);
        Table table = dynamoDB.getTable("Dakobed-Orders");
        DateTime date = new DateTime();
        String dateString = date.toString();
        Item order = new Item().withPrimaryKey("CustomerId",orderRequest.getCustomerID())
                .withString("OrderId", dateString )
                .withNumber("OrderCreationDate", 12)
                .withList("productIDs", orderRequest.getProducts())
                .withString("OrderStatus", "PROCESSING");
        try {
            table.putItem(order);
            System.err.println("added product: " +  " " + orderRequest.getProducts());
            return new OrderResponse("PROCESSING");
        }
        catch (Exception e) {
            System.err.println("Unable to add product: " + " " + orderRequest.getProducts());
            System.err.println(e.getMessage());
            return new OrderResponse("FAILED");

        }
    }

    @Autowired
    private OrderServicePublish orderServicePublish;
    //
    public OrderEntity createOrder(OrderDTO orderDTO){
        UUID uuid; // = UUID.randomUUID();
        List<Order> orders = new ArrayList<Order>();
        List<String> order_ids = new ArrayList<>();
        Order order;

        Double total = 0.0;
        for(int i = 0; i < orderDTO.getProducts().size(); i++){
            uuid = UUID.randomUUID();
            order_ids.add(uuid.toString());
            DateTime date = new DateTime();
            order = new Order(uuid.toString(),orderDTO.getCustomerID(), OrderState.PENDING, orderDTO.getProducts().get(i), orderDTO.getQuantities().get(i), orderDTO.getPrices().get(i), date);
            producer.sendOrder(order);
            logger.info("Order with id "+order.getId()+" sent to orders topic");
            total += orderDTO.getPrices().get(i);
        }

        uuid = UUID.randomUUID();
        OrderEntity orderEntity = new OrderEntity();
        return orderEntity;
    }

    public List<OrderEntity> getOrders(){

        DynamoDBMapperConfig mapperConfig = new DynamoDBMapperConfig.Builder()
                .withTableNameOverride(DynamoDBMapperConfig.TableNameOverride.withTableNameReplacement("Dakobed-Orders")).build();
        DynamoDBMapper mapper = new DynamoDBMapper(amazonDynamoDB, mapperConfig);
        DynamoDBScanExpression scanExpression = new DynamoDBScanExpression();
        List <OrderEntity> orders = mapper.scan(OrderEntity.class, scanExpression);
        return orders;
    }

    public OrderEntity getOrderByID(String id){
        DynamoDBMapper mapper = new DynamoDBMapper(amazonDynamoDB);
        OrderEntity order = mapper.load(OrderEntity.class, id );
        return order;
    }


    public List<OrderEntity> getCustomersOrders(String customerID){
        DynamoDBMapper mapper = new DynamoDBMapper(amazonDynamoDB);

        Map<String, AttributeValue> eav = new HashMap<String, AttributeValue>();
        eav.put(":customerId", new AttributeValue().withS(customerID));

        DynamoDBQueryExpression<OrderEntity> queryExpression = new DynamoDBQueryExpression<OrderEntity>()
                .withKeyConditionExpression("CustomerId = :customerId").withExpressionAttributeValues(eav);

        List<OrderEntity> orders = mapper.query(OrderEntity.class, queryExpression);
        return orders;
    }

    public List<OrderEntity> getOrderByCustomer(String customerID){
        QuerySpec querySpec = new QuerySpec().withConsistentRead(true).withScanIndexForward(true)
                .withReturnConsumedCapacity(ReturnConsumedCapacity.TOTAL);
        DynamoDB dynamoDB = new DynamoDB(amazonDynamoDB);
        Table table = dynamoDB.getTable("Dakobed-Orders");
        Index index = table.getIndex("OrderCreationDateIndex");

        querySpec.withKeyConditionExpression("CustomerId = :v_custid")
                .withValueMap(
                        new ValueMap().withString(":v_custid", customerID));

//        querySpec.withSelect(Select.ALL_PROJECTED_ATTRIBUTES);
        querySpec.withSelect(Select.ALL_ATTRIBUTES);


        ItemCollection<QueryOutcome> items = index.query(querySpec);
        Iterator<Item> iterator = items.iterator();

        System.out.println("Query: printing results...");
        List<OrderEntity> orders = new ArrayList<>();
        while (iterator.hasNext()) {
            Item item = iterator.next();
            String cid = item.get("CustomerId").toString();
            String oid = item.get("OrderId").toString();
            String order_status = item.get("OrderStatus").toString();
            OrderEntity order = new OrderEntity();
            order.setOrderId(oid);
            order.setCustomerId(cid);
            order.setOrderStatus(order_status);
            orders.add(order);

            System.out.println(iterator.next().toJSONPretty());
        }
        return orders;
    }


    public List<OrderEntity> customerOrdersAfterDate(String customerID, String orderDate){
        DynamoDBMapper mapper = new DynamoDBMapper(amazonDynamoDB);

        Map<String, AttributeValue> eav = new HashMap<String, AttributeValue>();
        eav.put(":customerId", new AttributeValue().withS(customerID));
        eav.put(":orderId", new AttributeValue().withS(orderDate));

        DynamoDBQueryExpression<OrderEntity> queryExpression = new DynamoDBQueryExpression<OrderEntity>()
                .withKeyConditionExpression("CustomerId = :customerId and OrderId > :orderId").withExpressionAttributeValues(eav);

        List<OrderEntity> latestOrders = mapper.query(OrderEntity.class, queryExpression);


        return latestOrders;
    }

    public void getOrderByCustomerAfterDatee(String customerID){

        QuerySpec querySpec = new QuerySpec().withConsistentRead(true).withScanIndexForward(true)
                .withReturnConsumedCapacity(ReturnConsumedCapacity.TOTAL);
        DynamoDB dynamoDB = new DynamoDB(amazonDynamoDB);
        Table table = dynamoDB.getTable("Dakobed-Orders");
        Index index = table.getIndex("OrderCreationDateIndex");

        querySpec.withKeyConditionExpression("CustomerId = :v_custid") //  and OrderId >= :v_orddate")
                .withValueMap(
                        new ValueMap().withString(":v_custid", customerID)); //.withNumber(":v_orddate", 20160638));

        querySpec.withSelect(Select.ALL_PROJECTED_ATTRIBUTES);

        ItemCollection<QueryOutcome> items = index.query(querySpec);
        Iterator<Item> iterator = items.iterator();

        System.out.println("Query: printing results...");

        while (iterator.hasNext()) {
            System.out.println(iterator.next().toJSONPretty());
        }
    }


//    public void getOrdersByCustomer(String customerID){
//        DynamoDB dynamoDB = new DynamoDB(amazonDynamoDB);
//        Table table = dynamoDB.getTable('Dakobed-Orders');
//        Index index = table.getIndex(indexName);
//
//        querySpec.withKeyConditionExpression("CustomerId = :v_custid and OrderCreationDate >= :v_orddate")
//                .withValueMap(
//                        new ValueMap().withString(":v_custid", "bob@example.com").withNumber(":v_orddate", 20150131));
//
//        querySpec.withSelect(Select.ALL_PROJECTED_ATTRIBUTES);
//
//        ItemCollection<QueryOutcome> items = index.query(querySpec);
//        Iterator<Item> iterator = items.iterator();
//
//        System.out.println("Query: printing results...");
//
//        while (iterator.hasNext()) {
//            System.out.println(iterator.next().toJSONPretty());
//        }
//    }



    public OrderEntity getOrderDetail(String id){
        OrderEntity order = new OrderEntity();
        order.setOrderId(id);
        DynamoDBMapper mapper = new DynamoDBMapper(amazonDynamoDB);
        DynamoDBQueryExpression<OrderEntity> queryExpression = new DynamoDBQueryExpression<OrderEntity>()
                .withHashKeyValues(order);
        List<OrderEntity> itemList = mapper.query(OrderEntity.class, queryExpression);

        for (int i = 0; i < itemList.size(); i++) {
            System.out.println(itemList.get(i).getCustomerId());
            System.out.println(itemList.get(i).getOrderId());
        }
        return itemList.get(0);
    }

}
