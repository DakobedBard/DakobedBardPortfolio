package org.mddarr.dakobedservices.mir.models;

public class Note {
    int midi;
    int beat;
    int measure;
    int string;

    public Note(int midi, int beat, int measure, int string) {
        this.midi = midi;
        this.beat = beat;
        this.measure = measure;
        this.string = string;
    }

    public int getMidi() { return midi;}
    public void setMidi(int midi) {  this.midi = midi;}
    public int getBeat() {return beat;}
    public void setBeat(int beat) {  this.beat = beat; }
    public int getMeasure() {  return measure; }
    public void setMeasure(int measure) {this.measure = measure;}
    public int getString() {
        return string;
    }
    public void setString(int string) {
        this.string = string;
    }

    @Override
    public String toString() {
        return "Note{" + "midi=" + midi + ", beat=" + beat + ", measure=" + measure + ", string=" + string + '}';
    }
}