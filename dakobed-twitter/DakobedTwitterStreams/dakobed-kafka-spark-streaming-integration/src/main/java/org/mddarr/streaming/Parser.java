package org.mddarr.streaming;

import org.junit.jupiter.api.Test;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;

public class Parser {

    HashMap<String, Set<String>> stopwords;

    public Parser() throws IOException {
        String[] languages = {"english.txt","spanish.txt","italian.txt", "french.txt"};
        stopwords = givenFileNameAsAbsolutePath_whenUsingClasspath_thenFileData(languages);
    }


    private  String readFromInputStream(InputStream inputStream) throws IOException {
        StringBuilder resultStringBuilder = new StringBuilder();
        try (BufferedReader br  = new BufferedReader(new InputStreamReader(inputStream))) {
            String line;
            while ((line = br.readLine()) != null) {
                resultStringBuilder.append(line).append("\n");
            }
        }
        return resultStringBuilder.toString();
    }
    public Parser(String[] languages){

    }


    public HashMap<String, Set<String>> givenFileNameAsAbsolutePath_whenUsingClasspath_thenFileData(String[] languages) throws IOException {
        Class clazz = Parser.class;
        HashMap<String, Set<String>> stop_words_map= new HashMap<>();
        for(String language:languages){
            InputStream inputStream = clazz.getResourceAsStream(language);
            String data = readFromInputStream(inputStream);
            String[] words = data.split("\n");
            stop_words_map.put(language, new HashSet<>(Arrays.asList(words)));
        }
        return stop_words_map;
    }


//    public static void main(String[] args) throws IOException {
//        String[] languages = {"english.txt","spanish.txt","italian.txt", "french.txt"};
//        List<Set<String>> stop_words = givenFileNameAsAbsolutePath_whenUsingClasspath_thenFileData(languages);
//
//        Set<String> first = stop_words.get(0);
//        for (String s : first) {
//            System.out.println(s);
//        }

//        System.out.println(givenFileNameAsAbsolutePath_whenUsingClasspath_thenFileData());
//    }



}
