package org.mddarr.dakobedordersservice.processors;

import io.confluent.kafka.serializers.AbstractKafkaAvroSerDeConfig;
import io.confluent.kafka.streams.serdes.avro.SpecificAvroSerde;
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.streams.KeyValue;
import org.apache.kafka.streams.kstream.Joined;
import org.apache.kafka.streams.kstream.KStream;
import org.apache.kafka.streams.kstream.KTable;
import org.mddarr.orders.event.dto.Order;
import org.mddarr.orders.event.dto.OrderState;
import org.mddarr.orders.event.dto.ValidatedOrder;
import org.mddarr.products.Product;
import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Service;

import java.util.Collections;
import java.util.Map;
import java.util.function.BiFunction;
import java.util.function.Function;

@Service
public class ProductStreamProcessor {
    @Bean
    public Function<KStream<String, Order>, KStream<String, Order>> orders() {

        return (orderStream) -> orderStream;
    }

//    @Bean
//    public BiFunction<KStream<String, Order>, KTable<String, Product>, KStream<String, ValidatedOrder>> ordersprocess() {
//
//        return (orderStream, productTable) ->{
//
//            final Map<String, String> serdeConfig = Collections.singletonMap(
//                    AbstractKafkaAvroSerDeConfig.SCHEMA_REGISTRY_URL_CONFIG, "http://localhost:8081");
//
//            final SpecificAvroSerde<Order> orderSerde = new SpecificAvroSerde<>();
//            orderSerde.configure(serdeConfig, false);
//
//            final SpecificAvroSerde<Product> keyProductSerde = new SpecificAvroSerde();
//            keyProductSerde.configure(serdeConfig, true);
//
//            final SpecificAvroSerde<Product> valueProductSerde = new SpecificAvroSerde<>();
//            valueProductSerde.configure(serdeConfig, false);
//
//            final SpecificAvroSerde<ValidatedOrder> validatedOrderSpecificAvroSerde = new SpecificAvroSerde<>();
//            validatedOrderSpecificAvroSerde.configure(serdeConfig, false);
//
//            // join the orders with product
//            final KStream<String, Order> ordersByProductId =
//                    orderStream.map((key, value) -> KeyValue.pair(value.getProductID(), value));
//
//            final KStream<String, ValidatedOrder> joinedProducts = ordersByProductId
//                    .join(productTable, (order, product) -> {
//                        System.out.println("debugging this shit");
//                        System.out.println("The product ID is " + product.getId() + " and the quantity is " + order.getQuantity() + "and the stock is " + product.getStock());
//                        return  new ValidatedOrder(order.getId(), "b", order.getQuantity() > product.getStock() ? OrderState.OUT_OF_STOCK : OrderState.STOCKED, 5l, 5.3);
//                    }, Joined.with(Serdes.String(), orderSerde, valueProductSerde));
//
//            return joinedProducts;
//        };
//    }
    public class OrdersProduct{
        String orderID;
        String productID;
        Long quantity;
        Double price;
        OrderState state;

        public OrdersProduct(String orderID, String productID, Long quantity, Long stock, Double price) {
            this.orderID = orderID;
            this.productID = productID;
            this.quantity = quantity;
            this.price = price;
            this.state = quantity > stock ? OrderState.OUT_OF_STOCK : OrderState.STOCKED;
        }

        public Double getPrice() {
            return price;
        }

        public void setPrice(Double price) {
            this.price = price;
        }

        public OrderState getState() {
            return state;
        }

        public void setState(OrderState state) {
            this.state = state;
        }

        public String getOrderID() { return orderID;}
        public void setOrderID(String orderID) { this.orderID = orderID;}
        public String getProductID() { return productID;}
        public void setProductID(String productID) {this.productID = productID; }
        public Long getQuantity() {return quantity;}
        public void setQuantity(Long quantity) { this.quantity = quantity;}
    }
}
