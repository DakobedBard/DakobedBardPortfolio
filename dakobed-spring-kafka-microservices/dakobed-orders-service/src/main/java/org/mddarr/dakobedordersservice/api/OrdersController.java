package org.mddarr.dakobedordersservice.api;

import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBMapper;

import org.mddarr.dakobedordersservice.models.OrderDocument;
import org.mddarr.dakobedordersservice.models.OrderEntity;
import org.mddarr.dakobedordersservice.models.OrderRequest;
import org.mddarr.dakobedordersservice.models.OrderResponse;
import org.mddarr.dakobedordersservice.services.OrderService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpHeaders;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Date;
import java.util.List;


@RestController
public class OrdersController {

    private DynamoDBMapper dynamoDBMapper;
    @Autowired
    private OrderService orderService;
    @Autowired
    private AmazonDynamoDB amazonDynamoDB;


//    @RequestMapping(value="orders")
//    public List<OrderEntity> getProduct(){
//        List<OrderEntity> orders = orderService.getOrders();
//        for(int i =0; i < orders.size();i++){
//            System.out.println("The orders have " + orders.get(i).getProductIDs().size() + " products");
//
//        }
//        return orders;
//    }


//    @RequestMapping(value = "detail")
//    public OrderEntity orderDetail(@RequestParam("id") String id){
//        return orderService.getOrderDetail(id);
//    }
    @RequestMapping("detail")
    public List<OrderEntity> getOrderDetailByDate(@RequestParam("id") String id, @RequestParam("date") String date){
//        orderService.getOrderByCustomer(id);
        return orderService.customerOrdersAfterDate(id, date);
    }

    @RequestMapping("customer-orders")
    public List<OrderEntity> getCustomersOrders(@RequestParam("id") String id){
        return orderService.getCustomersOrders(id);
    }
//
    @PostMapping("post-order")
    public ResponseEntity<OrderResponse> postOrder(@RequestBody OrderRequest orderRequest){
        OrderResponse resp = orderService.postOrder(orderRequest);
        HttpHeaders headers = new HttpHeaders();
        return ResponseEntity.accepted().headers(headers).body(resp);
    }


//    @RequestMapping("order")
//    public void getOrderByCustomer(@RequestParam("id") String id){
//        orderService.getOrderByID(id);
//    }
//
//
//    @RequestMapping("date-detail")
//    public long getDate(@RequestParam("date") long date){
//        return date;
//    }

//    @RequestMapping("date")
//    public String getDate(@RequestParam("date") long date){
//        Date d = new Date(date);
//        return d.toString();
//    }


}
