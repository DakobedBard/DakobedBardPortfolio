package org.mddarr.dakobedservice.models;

public class PianoNote {
    int midi;
    int beat;
    int measure;
    double duration;

    public PianoNote(int midi, int beat, int measure, double duration) {
        this.midi = midi;
        this.beat = beat;
        this.measure = measure;
        this.duration = duration;
    }

    public int getMidi() { return midi;}
    public void setMidi(int midi) {  this.midi = midi;}
    public int getBeat() {return beat;}
    public void setBeat(int beat) {  this.beat = beat; }
    public int getMeasure() {  return measure; }
    public void setMeasure(int measure) {this.measure = measure;}
    public double getDuration() {
        return duration;
    }
    public void setDuration(double duration) {
        this.duration = duration;
    }

    @Override
    public String toString() {
        return "Note{" + "midi=" + midi + ", beat=" + beat + ", measure=" + measure + ", duration=" + duration + '}';
    }


}
