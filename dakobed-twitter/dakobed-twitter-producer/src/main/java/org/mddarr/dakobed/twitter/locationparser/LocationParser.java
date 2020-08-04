package org.mddarr.dakobed.twitter.locationparser;

import java.sql.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class LocationParser {

    ArrayList<City> cities;
    Map<String, ArrayList<Double>> statesMapCoords;
    public  LocationParser(){
        cities = initCitiesArray();
        statesMapCoords = initStatesMap();
    }

    private String parseState(String location){
        String lowercaseLocation = location.toLowerCase();
        US arr[] = US.values();
        String state = "";
        String abrev;
        for (US col : arr)
        {
            state = col.toString().toLowerCase();
            abrev = col.getANSIAbbreviation().toLowerCase();
            int containtsStateName = lowercaseLocation.indexOf(abrev);

            if(containtsStateName >= 0) {
                System.out.println("State:" + state);
                return state.toLowerCase();
            }
            if(containsAbreviation(location, abrev)){
                return state.toLowerCase();
            }
        }
        return null;
    }

    public ArrayList<Double> parseLocation(String location){
        ArrayList<Double> coords = new ArrayList<Double>();
        String state = parseState(location);
        ArrayList<City> citiesList = parseCity(location);

        if(state == null){
            if(citiesList.size() == 0){                      // We don't have a state or a city, return null null
                coords.add(null);
                coords.add(null);
                return coords;
            }else{                                           // No state and multiple matches on city
                return getCitiesCoordinates(citiesList);
            }

        }else{                                               // We have a state
            if(citiesList.size() == 0){                      // We have  a state but no city, return coords of state
                return getStatesCoordinates(state.toLowerCase());
            }else{                                           // We have a state and multiple matches on city
                return getCitiesCoordinates(citiesList, state.toLowerCase());
            }
        }
    }



    public ArrayList<Double> getStatesCoordinates(String state){
        return statesMapCoords.get(state);
    }

    public ArrayList<Double> getCitiesCoordinates(ArrayList<City> citiesList){
        ArrayList<Double> coords = new ArrayList<Double>();

        if(citiesList.size() == 1){
            City city = citiesList.get(0);
            coords.add(city.lat);
            coords.add(city.lng);
            return coords;
        }else{

        }
        return coords;
    }

    public ArrayList<Double> getCitiesCoordinates(ArrayList<City> citiesList, String state){
        ArrayList<Double> coords = new ArrayList<Double>();

        if(citiesList.size() == 1 && citiesList.get(0).state == state ){
            City cityMatch = citiesList.get(0);
            coords.add(cityMatch.lat);
            coords.add(cityMatch.lng);
            return coords;
        }else{
            for(City city : citiesList){
                if(city.state == state){
                    coords.add(city.lat);
                    coords.add(city.lng);
                    return coords;
                }
            }
        }
        return null;
    }


    private Map<String, ArrayList<Double>> generateStateMapCoords(ArrayList<State> statesList){
        Map<String, ArrayList<Double>> coordsMap = new HashMap<>();
        ArrayList<Double> coords ; // = new ArrayList<Double>()\
        for (State state: statesList){
            coords = new ArrayList<Double>();
            coords.add(state.lat);
            coords.add(state.lng);
            coordsMap.put(state.state.toLowerCase(), coords);
        }
        return coordsMap;
    }



    private Boolean containsAbreviation(String location, String abreviation){
        int containtsStateAbv = location.indexOf(" " + abreviation);
        if(containtsStateAbv >= 0){
            return true;
        }
        return false;
    }

    public ArrayList<City> parseCity(String location){
        String lowercaseLocation = location.toLowerCase();
        String lowerCaseCity;

        ArrayList<City> citiesList = new ArrayList<>();

        for (City city: cities)
        {
            lowerCaseCity = city.city.toLowerCase();
            int containsCityName = lowercaseLocation.indexOf(lowerCaseCity);
            if(containsCityName >= 0) {
                //System.out.println("We have a match with " + lowerCaseCity);
                citiesList.add(city);
            }
        }
        String city = null;
        return citiesList;
    }


    public String generateCoordinatesString(String location, ArrayList<Double> coords){
        if(coords != null){
            return "Location: " + location + " has coordinates of lat:  " + coords.get(0) +" and lng: " + coords.get(1);
        }
        else{
            return "Location: " + location + " was unable to be to find coordinates";
        }
    }



    private  Map<String, ArrayList<Double>>  initStatesMap(){
        ArrayList<State> statesList = new ArrayList<>();
        String queryString = "SELECT abr, lat, lng, state FROM states";
        State state;

        try (Connection conn = DriverManager.getConnection(
                "jdbc:postgresql://localhost:5432/locationsDB", "postgres", "postgres")) {
            if (conn != null) {
                System.out.println("Connected to the database!");
                Statement st = conn.createStatement();
                ResultSet rs = st.executeQuery(queryString);

                while(rs.next()){
                    state = new State(rs.getString("state"), rs.getDouble("lat"), rs.getDouble("lng"));
                    statesList.add(state );
                }
            } else {
                System.out.println("Failed to make connection!");
            }
        } catch (SQLException e) {
            System.err.format("SQL State: %s\n%s", e.getSQLState(), e.getMessage());
        } catch (Exception e) {
            e.printStackTrace();
        }

        Map<String, ArrayList<Double>> coordsMap = generateStateMapCoords(statesList);
        return coordsMap;
    }

    private ArrayList<City> initCitiesArray(){
        ArrayList<City> citiesList = new ArrayList<City>();
        String queryString = "SELECT city, state_name, county_name, lat,lng,population FROM cities_g75k";
        City city;
        try (Connection conn = DriverManager.getConnection(
                "jdbc:postgresql://localhost:5432/locationsDB", "postgres", "postgres")) {
            if (conn != null) {
                System.out.println("Connected to the database!");
                Statement st = conn.createStatement();
                ResultSet rs = st.executeQuery(queryString);
                int count = 0;
                while(rs.next()){
                    count++;
                    city = new City(rs.getString("city"), rs.getString("state_name"), rs.getString("county_name")
                            , rs.getDouble("lat"), rs.getDouble("lng"), rs.getInt("population"));
                    citiesList.add(city);
                }
            } else {
                System.out.println("Failed to make connection!");
            }
        } catch (SQLException e) {
            System.err.format("SQL State: %s\n%s", e.getSQLState(), e.getMessage());
        } catch (Exception e) {
            e.printStackTrace();
        }

        return citiesList;
    }



}
