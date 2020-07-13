package org.mddarr.dakobedservice.api;

import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBMapper;

import org.mddarr.dakobedservice.models.GuitarsetTrainingExample;
import org.mddarr.dakobedservice.models.MaestroTrainingExample;
import org.mddarr.dakobedservice.models.PianoTranscription;
import org.mddarr.dakobedservice.models.Transcription;
import org.mddarr.dakobedservice.services.TranscriptionService;
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

    @RequestMapping(value = "guitarset")
    public List<GuitarsetTrainingExample> getTrainingData(){
        return transcriptionService.getGuitarSetTrainingData();
    }


}
