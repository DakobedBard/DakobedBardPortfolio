package org.mddarr.streaming;

import io.confluent.kafka.serializers.KafkaAvroSerializerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.common.TopicPartition;
import org.apache.kafka.common.serialization.LongDeserializer;
import org.apache.kafka.common.serialization.LongSerializer;
import org.apache.kafka.common.serialization.StringDeserializer;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.function.FlatMapFunction;
import org.apache.spark.api.java.function.PairFunction;
import org.apache.spark.streaming.Durations;
import org.apache.spark.streaming.api.java.*;
import org.apache.spark.streaming.kafka010.ConsumerStrategies;
import org.apache.spark.streaming.kafka010.KafkaUtils;
import org.apache.spark.streaming.kafka010.LocationStrategies;
import org.mddarr.avro.tweets.Tweet;
import scala.Tuple2;
import io.confluent.kafka.serializers.KafkaAvroDeserializer;
import java.util.*;
import java.util.logging.Level;
import java.util.logging.Logger;

public class KafkaSparkTweetsStream {
    public static void main(String[] args) throws InterruptedException {
        Logger.getLogger("org")
                .setLevel(Level.OFF);
        Logger.getLogger("akka")
                .setLevel(Level.OFF);

        Map<String, Object> kafkaParams = new HashMap<>();
        kafkaParams.put("bootstrap.servers", "localhost:9092");
        kafkaParams.put("key.deserializer", LongDeserializer.class);
        kafkaParams.put("value.deserializer", io.confluent.kafka.serializers.KafkaAvroDeserializer.class);
        kafkaParams.put("group.id", "use_a_separate_group_id_for_each_stream");
        kafkaParams.put("auto.offset.reset", "latest");
        kafkaParams.put("enable.auto.commit", false);
        kafkaParams.put(KafkaAvroSerializerConfig.SCHEMA_REGISTRY_URL_CONFIG, "http://localhost:8081");

        Collection<String> topics = Arrays.asList("kafka-tweets");

        SparkConf sparkConf = new SparkConf();
        sparkConf.setMaster("local[2]");
        sparkConf.setAppName("WordCountingApp");

        JavaStreamingContext streamingContext = new JavaStreamingContext(sparkConf, Durations.seconds(1));

        Map<TopicPartition, Long> fromOffsets = new HashMap<>();

//        JavaInputDStream<ConsumerRecord<Long, Tweet>> directKafkaStream = KafkaUtils.createDirectStream(
//                streamingContext,
//                LocationStrategies.PreferConsistent(),
//                ConsumerStrategies.<Long, Tweet> Subscribe(topics, kafkaParams)
//        );

        JavaInputDStream<ConsumerRecord<Long, Tweet>> tweets = KafkaUtils.createDirectStream(streamingContext,
                LocationStrategies.PreferConsistent(), ConsumerStrategies.<Long, Tweet> Subscribe(topics, kafkaParams));

        JavaDStream<Tweet> lines = tweets.map(ConsumerRecord::value);
        JavaDStream<String> tweet_content = lines.flatMap((tweet -> Arrays.asList(tweet.getTweetContent().split(" ")).iterator()));
        tweet_content.print();

        streamingContext.start();
        streamingContext.awaitTermination();

    }

}

//        JavaDStream<String> words = tweets.flatMap(
//                (FlatMapFunction<Tweet, String>) x -> Arrays.asList(x.getTweetContent().split(" ")).iterator()
//        );

//        JavaDStream<String> tweetStream = tweets.flatMap((FlatMapFunction<Tweet, String>) tweet-> tweet.getTweetContent()).iteratror();
//        JavaDStream<String> words = tweets.flatMap(
//                (FlatMapFunction<Tweet, String>) x -> Arrays.asList(x.getTweetContent().split(" ")).iterator()
//        );


//        JavaPairDStream<Long, Tweet> tweets = messages.mapToPair(record -> new Tuple2<>(record.key(), record.value()));
//        tweets.print();



//        Tweet tweet = new Tweet();
//        tweet.getTweetContent()
//      Split each line into words
//        JavaDStream<String> words = messages.flatMap((FlatMapFunction<Tweet, String>) tweet -> Arrays.asList(tweet.getTweetContent().split(" ")).iterator());
//
//        JavaPairDStream<String, Integer> pairs = words.mapToPair(
//                (PairFunction<String, String, Integer>) s -> new Tuple2<>(s, 1));

//        JavaPairInputDStream<String, String> directKafkaStream = KafkaUtils.createDirectStream(streamingContext,
//                String.class, String.class, LongDeserializer.class, KafkaAvroDeserializer.class, kafkaParams, topics);

//
//        JavaInputDStream<ConsumerRecord<Long, Tweet>> directKafkaStream = KafkaUtils.createDirectStream(
//                streamingContext,
//                LocationStrategies.PreferConsistent(),
//                ConsumerStrategies.<Long, Tweet>Assign(fromOffsets.keySet(), kafkaParams, fromOffsets)
//        );





//        JavaDStream<String> lines = results.map(tuple2 -> tuple2._2());
//
//        JavaDStream<String> words = lines.flatMap(x -> Arrays.asList(x.split("\\s+"))
//                .iterator());
//
//        JavaPairDStream<String, Integer> wordCounts = words.mapToPair(s -> new Tuple2<>(s, 1))
//                .reduceByKey((i1, i2) -> i1 + i2);
//        wordCounts.print();
//        wordCounts.foreachRDD(javaRdd -> {
//            Map<String, Integer> wordCountMap = javaRdd.collectAsMap();
//            for (String key : wordCountMap.keySet()) {
//                List<Word> wordList = Arrays.asList(new Word(key, wordCountMap.get(key)));
//                JavaRDD<Word> rdd = streamingContext.sparkContext()
//                        .parallelize(wordList);
//                System.out.println("The word is " + key);
//            }
//        });
