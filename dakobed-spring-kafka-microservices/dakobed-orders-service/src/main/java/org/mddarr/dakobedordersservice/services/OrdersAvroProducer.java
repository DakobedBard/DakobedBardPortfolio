package org.mddarr.dakobedordersservice.services;

import org.mddarr.dakobedordersservice.port.OrderServicePublish;
import org.mddarr.orders.event.dto.Order;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

@Service
public class OrdersAvroProducer implements OrderServicePublish {
    @Autowired
    private KafkaTemplate<String, Order> kafkaTemplateOrder;
    private static final Logger logger = LoggerFactory.getLogger(OrdersAvroProducer.class);

    @Override
    public void sendOrder(Order order) {
        logger.info("Send order  {}", order);
        kafkaTemplateOrder.send("orders", order);
    }
}
