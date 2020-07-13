package org.mddarr.dakobedsnotelservice.model;

import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBHashKey;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBRangeKey;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBTable;


@DynamoDBTable(tableName="BasinLocations")
public class Location {
    private String location;
    private int elevation;

    @DynamoDBHashKey(attributeName="LocationID")
    public String getLocation() {return location; }
    public void setLocation(String location) { this.location = location;}

    @DynamoDBRangeKey(attributeName = "Elevation")
    public int getElevation() { return elevation;}
    public void setElevation(int elevation) { this.elevation = elevation;

    }
}
