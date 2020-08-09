package org.mddarr.dakobedordersservice.beans;

import java.util.List;

public class OrderDTO {
    List<String> products;
    List<Long> quantities;
    List<Double> prices;
    String cid;

    public List<String> getProducts() { return products; }
    public void setProducts(List<String> products) { this.products = products; }
    public List<Long> getQuantities() {  return quantities;}
    public void setQuantities(List<Long> quantities) {this.quantities = quantities; }

    public String getCustomerID() {return cid; }
    public void setCustomerID(String customerID) {this.cid = customerID;}

    public List<Double> getPrices() {
        return prices;
    }

    public void setPrices(List<Double> prices) {
        this.prices = prices;
    }

    public OrderDTO(){

    }

    public OrderDTO(List<String> products, List<Long> quantities, List<Double> prices, String customerID) {
        this.products = products;
        this.quantities = quantities;
        this.prices = prices;
        this.cid = customerID;
    }
}
