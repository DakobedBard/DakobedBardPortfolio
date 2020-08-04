package org.mddarr.dakobedordersservice.models;


public class OrderDocument {

    private String id;
    private String customerID;
    private String order_time;

    public String getId() {
        return id;
    }
    public void setId(String id) {
        this.id = id;
    }

    public OrderDocument(){}

    public OrderDocument(String customerID, String order_date) {
        this.customerID = customerID;
        this.order_time = order_date;
    }

    public String getCustomerID() {
        return customerID;
    }

    public void setCustomerID(String customerID) {
        this.customerID = customerID;
    }

    public String getOrder_date() {
        return order_time;
    }

    public void setOrder_date(String order_date) {
        this.order_time = order_date;
    }



}
