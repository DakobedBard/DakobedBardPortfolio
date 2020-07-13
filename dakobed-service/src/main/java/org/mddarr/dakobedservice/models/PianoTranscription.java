package org.mddarr.dakobedservice.models;

import com.fasterxml.jackson.core.JsonFactory;
import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class PianoTranscription {

    public List<PianoNote> notes;

    public PianoTranscription(String transcription_file_path) throws IOException {
        notes = new ArrayList<>();
        JsonParser parser = new JsonFactory().createParser(new File(transcription_file_path));
        JsonNode rootNode = new ObjectMapper().readTree(parser);
        Iterator<JsonNode> iter = rootNode.iterator();
        ObjectNode currentNode;

        while (iter.hasNext()) {
            currentNode = (ObjectNode) iter.next();
            int beat = currentNode.path("beat").asInt();
            int measure = currentNode.path("measure").asInt();
            int midi = currentNode.path("midi").asInt();
            double duration = currentNode.path("duration").asDouble();
            PianoNote note = new PianoNote(midi, beat, measure, duration);
            notes.add(note);
        }
    }

    public PianoTranscription(List<PianoNote> notes){
        this.notes = notes;
    }

}
