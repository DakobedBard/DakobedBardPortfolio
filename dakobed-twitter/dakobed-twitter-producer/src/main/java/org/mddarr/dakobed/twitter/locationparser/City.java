package org.mddarr.dakobed.twitter.locationparser;

public class City {
    String city;
    String county;
    String state;
    double lat;
    double lng;
    int population;
    public City(String city_, String state_, String county_, double lat_, double lng_, int pop ){
        city = city_;
        county = county_;
        state = state_;
        lat = lat_;
        lng = lng_;
        population = pop;
    }
}
