package org.mddarr.dakobedservices.snotel.models;

import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBAttribute;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBHashKey;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBRangeKey;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBTable;


@DynamoDBTable(tableName="Snotel")
public class SnotelData {
    private String location;
    private String snoteldate;
    private double snowCurrent;
    private double snowMedian;
    private double snowPctMedian;
    private double waterCurrent;
    private double waterMedian;
    private double waterPctMedian;

    @DynamoDBHashKey(attributeName="LocationID")
    public String getLocation() {return location; }
    public void setLocation(String location) { this.location = location;}

    @DynamoDBRangeKey(attributeName = "SnotelDate")
    public String getSnoteldate() { return snoteldate;}
    public void setSnoteldate(String date_) { this.snoteldate = date_; }

    @DynamoDBAttribute(attributeName = "SnowCurrent")
    public double getSnowCurrent() {return snowCurrent; }
    public void setSnowCurrent(double snowCurrent) {this.snowCurrent = snowCurrent;}

    @DynamoDBAttribute(attributeName = "SnowMedian")
    public double getSnowMedian() {return snowMedian; }
    public void setSnowMedian(double snowMedian) {this.snowMedian = snowMedian;}

    @DynamoDBAttribute(attributeName = "SnowPctMedian")
    public double getSnowPctMedian() { return snowPctMedian;}
    public void setSnowPctMedian(double snowPctMedian) {this.snowPctMedian = snowPctMedian;}


    @DynamoDBAttribute(attributeName = "WaterCurrent")
    public double getWaterCurrent() {return waterCurrent;}
    public void setWaterCurrent(double waterCurrent) {this.waterCurrent = waterCurrent;}

    @DynamoDBAttribute(attributeName = "WaterCurrentAverage")
    public double getWaterMedian() {return waterMedian;}
    public void setWaterMedian(double waterMedian) {this.waterMedian = waterMedian;}

    @DynamoDBAttribute(attributeName = "WaterPctAverage")
    public double getWaterPctMedian() {return waterPctMedian;}
    public void setWaterPctMedian(double waterPctMedian) {this.waterPctMedian = waterPctMedian; }

}

