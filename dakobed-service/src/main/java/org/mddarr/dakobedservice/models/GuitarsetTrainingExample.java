package org.mddarr.dakobedservice.models;


import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBAttribute;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBHashKey;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBTable;

@DynamoDBTable(tableName="Dakobed-GuitarSet")
public class GuitarsetTrainingExample {
    String fileID;
    String title;

    @DynamoDBHashKey(attributeName="PieceID")
    public String getFileID() {return fileID; }
    public void setFileID(String fileID) { this.fileID = fileID;}

    @DynamoDBAttribute(attributeName = "PieceName")
    public String getTitle() { return title;}
    public void setTitle(String date_) { this.title = date_; }


}
