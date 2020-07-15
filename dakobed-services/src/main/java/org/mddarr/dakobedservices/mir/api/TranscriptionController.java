package org.mddarr.dakobedservices.mir.api;

import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBMapper;

import org.mddarr.dakobedservices.mir.models.GuitarsetTrainingExample;
import org.mddarr.dakobedservices.mir.models.MaestroTrainingExample;
import org.mddarr.dakobedservices.mir.models.PianoTranscription;
import org.mddarr.dakobedservices.mir.models.Transcription;
import org.mddarr.dakobedservices.mir.services.TranscriptionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
import java.util.List;


@RestController
@CrossOrigin
public class TranscriptionController {
    private DynamoDBMapper dynamoDBMapper;

    @Autowired
    TranscriptionService transcriptionService;

    @RequestMapping(value="transcription")
    public Transcription getTranscription() throws IOException {
        return transcriptionService.getTab();
    }

    @RequestMapping(value = "guitarset")
    public List<GuitarsetTrainingExample> getTrainingData(){
        return transcriptionService.getGuitarSetTrainingData();
    }

    @RequestMapping(value="maestro")
    public List<MaestroTrainingExample> getMaestroTrainingData(){
        return transcriptionService.getMaestroTrainingData();
    }

    @RequestMapping(value = "pianoTranscription")
    public PianoTranscription getPianoTranscription() throws IOException {
        return transcriptionService.getPianoTranscription();
    }

    @RequestMapping(value = "S3transcription")
    public Transcription getS3Transcription(@RequestParam("fileID") int fileid) throws IOException {
        return transcriptionService.getTranscriptionS3(fileid);
    }

    @RequestMapping(value="pianoTranscriptionS3")
    public PianoTranscription getPianoTranscriptonS3(@RequestParam("fileID") String fileID) throws IOException {
        return transcriptionService.getPianoTranscriptionS3(fileID);
    }

    @RequestMapping(value="maestroExample")
    public PianoTranscription getMaestroExample() throws IOException {
        return transcriptionService.getPianoTranscription();
    }


}
