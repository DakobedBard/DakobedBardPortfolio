package org.mddarr.dakobedordersservice.models;

import java.util.List;

public class OrderRequest {

    List<String> products;
    String customerID;

    public OrderRequest(){}
    public OrderRequest(List<String> products, String customerID) {
        this.products = products;
        this.customerID = customerID;
    }

    public List<String> getProducts() {
        return products;
    }
    public void setProducts(List<String> products) {
        this.products = products;
    }
    public String getCustomerID() {
        return customerID;
    }
    public void setCustomerID(String customerID) {
        this.customerID = customerID;
    }


}
