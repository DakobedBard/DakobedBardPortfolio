package org.mddarr.dakobedordersservice.port;

import org.mddarr.orders.event.dto.Order;


/**
 * Created by <a href="mailto:pasquale.paola@gmail.com">Pasquale Paola</a> on 09/09/19.
 */
public interface OrderServicePublish {
    void sendOrder(Order order);
}
