package org.mddarr.dakobedservices.mir.models;

import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBAttribute;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBHashKey;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBTable;


@DynamoDBTable(tableName="Dakobed-Maestro")
public class MaestroTrainingExample {
    String fileID;
    String composer;
    String title;

    @DynamoDBHashKey(attributeName = "PieceID")
    public String getFileID() {return fileID; }
    public void setFileID(String fileID) {this.fileID = fileID; }

    @DynamoDBAttribute(attributeName = "Composer")
    public String getComposer() {return composer; }
    public void setComposer(String composer) {this.composer = composer; }

    @DynamoDBAttribute(attributeName = "PieceName")
    public String getTitle() {return title; }
    public void setTitle(String title) {this.title = title; }

}