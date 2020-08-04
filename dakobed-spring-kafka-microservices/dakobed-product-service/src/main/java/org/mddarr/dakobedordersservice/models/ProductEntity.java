package org.mddarr.dakobedordersservice.models;


import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBAttribute;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBHashKey;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBIgnore;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBTable;

import java.util.Set;

@DynamoDBTable(tableName="Dakobed-Products")
public class ProductEntity {

    private String id;
    private String productName;
    private String imageURL;
    private Double price;

    @DynamoDBHashKey(attributeName="id")
    public String getId() { return id; }
    public void setId(String id) {this.id = id; }

    @DynamoDBAttribute(attributeName="productName")
    public String getProductName() {return productName; }
    public void setProductName(String productName) { this.productName = productName; }

    @DynamoDBAttribute(attributeName="imageURL")
    public String getImageURL() { return imageURL; }
    public void setImageURL(String imageURL) { this.imageURL = imageURL; }

    @DynamoDBAttribute(attributeName = "price")
    public Double getPrice() { return price; }
    public void setPrice(Double price) { this.price = price; }
}