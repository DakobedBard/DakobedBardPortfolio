package org.mddarr.dakobedservice.services;


import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBMapper;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBMapperConfig;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBScanExpression;
import com.amazonaws.services.dynamodbv2.model.*;
import com.fasterxml.jackson.core.JsonFactory;
import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;

import org.mddarr.dakobedservice.models.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

@Service
public class TranscriptionService {

    @Autowired
    S3Factory s3Factory;

    @Autowired
    AmazonDynamoDB amazonDynamoDB;

    String note_json_file_path = "/home/mddarr/data/Dakobed/dakobed-transcription-service/src/main/resources/transcription1.json";

    public List<MaestroTrainingExample> getMaestroTrainingData(){
        DynamoDBMapperConfig mapperConfig = new DynamoDBMapperConfig.Builder()
                .withTableNameOverride(DynamoDBMapperConfig.TableNameOverride.withTableNameReplacement("Dakobed-Maestro")).build();
        DynamoDBMapper mapper = new DynamoDBMapper(amazonDynamoDB, mapperConfig);
        List<MaestroTrainingExample> trainingExamples = mapper.scan(MaestroTrainingExample.class, new DynamoDBScanExpression());
        return trainingExamples;
    }


    public List<GuitarsetTrainingExample> getGuitarSetTrainingData(){
        DynamoDBMapperConfig mapperConfig = new DynamoDBMapperConfig.Builder()
                .withTableNameOverride(DynamoDBMapperConfig.TableNameOverride.withTableNameReplacement("Dakobed-GuitarSet")).build();
        DynamoDBMapper mapper = new DynamoDBMapper(amazonDynamoDB, mapperConfig);
        List<GuitarsetTrainingExample> trainingExamples = mapper.scan(GuitarsetTrainingExample.class, new DynamoDBScanExpression());
        return trainingExamples;
    }

    public PianoTranscription getPianoTranscription() throws IOException {
        PianoTranscription transcription = new PianoTranscription("/home/mddarr/data/Dakobed/dakobed-transcription-service/src/main/resources/test_transcription.json");
        return transcription;
    }


    public Transcription getTab() throws IOException {
        Transcription transcription = new Transcription(note_json_file_path);
        return transcription;
    }

    public PianoTranscription getPianoTranscriptionS3(String fileID) throws IOException {
        List<PianoNote> notes = new ArrayList<>();
        byte[] bytes = s3Factory.getMaestroTranscription(fileID);

        JsonParser parser = new JsonFactory().createParser(bytes);
        JsonNode rootNode = new ObjectMapper().readTree(parser);
        Iterator<JsonNode> iter = rootNode.iterator();
        ObjectNode currentNode;

        while (iter.hasNext()) {
            currentNode = (ObjectNode) iter.next();
            int beat = currentNode.path("beat").asInt();
            int measure = currentNode.path("measure").asInt();
            int midi = currentNode.path("midi").asInt();
            int duration = currentNode.path("duration").asInt();
            PianoNote note = new PianoNote(midi, beat, measure, duration);
            notes.add(note);
        }
        return new PianoTranscription(notes);
    }

    public Transcription getTranscriptionS3(int fileID) throws IOException {
        List<Note> notes = new ArrayList<>();
        byte[] a = s3Factory.getFile(fileID);

        JsonParser parser = new JsonFactory().createParser(a);
        JsonNode rootNode = new ObjectMapper().readTree(parser);
        Iterator<JsonNode> iter = rootNode.iterator();
        ObjectNode currentNode;

        while (iter.hasNext()) {
            currentNode = (ObjectNode) iter.next();
            int beat = currentNode.path("beat").asInt();
            int measure = currentNode.path("measure").asInt();
            int midi = currentNode.path("midi").asInt();
            int string = currentNode.path("string").asInt();
            Note note = new Note(midi, beat, measure, string);
            notes.add(note);
        }
        return new Transcription(notes);
    }

}


