package org.mddarr.dakobedordersservice.models;

public class ProductDocument {

    private String id;
    private String productName;
    private String imageURL;
    private Double price;
    private String brand;

    public ProductDocument(){}
    public ProductDocument(String productName, String imageURL) {
        this.productName = productName;

        this.imageURL = imageURL;
    }

    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

    public String getId() {
        return id;
    }
    public void setId(String Id) {
        this.id = Id;
    }
    public String getProductName() {
        return productName;
    }
    public void setProductName(String productName) {
        this.productName = productName;
    }
    public String getImageURL() {
        return imageURL;
    }
    public void setImageURL(String imageURL) {
        this.imageURL = imageURL;
    }
    public Double getPrice() {
        return price;
    }
    public void setPrice(Double price) {
        this.price = price;
    }
}
