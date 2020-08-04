package org.mddarr.dakobedservices.mir.services;

import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.model.Bucket;
import com.amazonaws.services.s3.model.S3Object;
import com.amazonaws.services.s3.model.S3ObjectInputStream;
import com.amazonaws.util.IOUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.io.File;
import java.io.IOException;
import java.util.List;

@Service
public class S3Factory {

    @Autowired
    AmazonS3 amazonS3Client;

    @Value("dakobed-guitarset")
    String defaultBucketName;

    public List<Bucket> getAllBuckets() {
        return amazonS3Client.listBuckets();
    }

    public void uploadFile(File uploadFile) {
        amazonS3Client.putObject(defaultBucketName, uploadFile.getName(), uploadFile);
    }

    public byte[] getMaestroTranscription(String fileID){
        S3Object obj = amazonS3Client.getObject("dakobed-maestro", "fileID" + fileID + "/transcription.json");
        S3ObjectInputStream stream = obj.getObjectContent();
        try {
            byte[] content = IOUtils.toByteArray(stream);
            obj.close();
            return content;
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public byte[] getFile(int fileID) {
        S3Object obj = amazonS3Client.getObject("dakobed-guitarset", "fileID" + fileID + "/transcription.json");
        S3ObjectInputStream stream = obj.getObjectContent();
        try {
            byte[] content = IOUtils.toByteArray(stream);
            obj.close();
            return content;
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }






}