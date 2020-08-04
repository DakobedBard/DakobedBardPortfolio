package org.mddarr.dakobedordersservice.models;

public class OrderResponse {
    private String state;
    public OrderResponse(){}

    public OrderResponse(String state) { this.state = state; }
    public String getState() {return state; }
    public void setState(String state) {this.state = state;}
}
