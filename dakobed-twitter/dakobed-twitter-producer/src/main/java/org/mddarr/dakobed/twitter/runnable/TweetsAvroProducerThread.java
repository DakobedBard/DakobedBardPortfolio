package org.mddarr.dakobed.twitter.runnable;


import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.LongSerializer;
import org.joda.time.DateTime;
//import org.mddarr.avro.tweets.Tweet;
import org.mddarr.dakobed.twitter.AppConfig;
import org.mddarr.dakobed.twitter.locationparser.LocationParser;

import twitter4j.Status;

import java.util.ArrayList;
import java.util.Properties;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.CountDownLatch;


public class TweetsAvroProducerThread implements Runnable {
    LocationParser locationParser;
    private final Log log = LogFactory.getLog(getClass());

    private final AppConfig appConfig;
    private final String targetTopic;
//    private final KafkaProducer<Long, Tweet> kafkaProducer;
    private final CountDownLatch latch;

    private int recordCount;

    private final ArrayBlockingQueue<Status> statusQueue;

    public TweetsAvroProducerThread(AppConfig appConfig,
                                    ArrayBlockingQueue<Status> statusQueue,
                                    CountDownLatch latch){
        this.locationParser = new LocationParser();
        this.statusQueue = statusQueue;
        this.appConfig = appConfig;
        this.latch = latch;
//        this.kafkaProducer = createKafkaProducer(appConfig);
        this.targetTopic = appConfig.getTweetTopicName();
        this.recordCount +=1;
    }
//
//    public KafkaProducer<Long, Tweet> createKafkaProducer(AppConfig appConfig){
//        Properties properties = new Properties();
//        properties.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, appConfig.getBootstrapServers());
//        properties.put(ProducerConfig.ACKS_CONFIG, "all");
//        properties.put(ProducerConfig.RETRIES_CONFIG, Integer.MAX_VALUE);
//        properties.put(ProducerConfig.MAX_IN_FLIGHT_REQUESTS_PER_CONNECTION, 5);
//        properties.put(ProducerConfig.ENABLE_IDEMPOTENCE_CONFIG, true);
//        properties.put(ProducerConfig.COMPRESSION_TYPE_CONFIG, "snappy");
//        properties.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, LongSerializer.class.getName());
//        properties.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, KafkaAvroSerializer.class.getName());
//        properties.put(KafkaAvroSerializerConfig.SCHEMA_REGISTRY_URL_CONFIG, appConfig.getSchemaRegistryUrl());
//        return new KafkaProducer<>(properties);
//    }

    public void run() {

        int tweetCount = 0;

//        while(latch.getCount() >0 ) {
//            try {
//                if(statusQueue.size()>0){
//                    Status status = statusQueue.poll();
//                    tweetCount +=1;
//                    Tweet tweet = statusToTweet(status, tweetCount);
//                    kafkaProducer.send(new ProducerRecord<>("kafka-tweets", tweet));
//                    if(tweet.getLocation() != null){
//                        kafkaProducer.send(new ProducerRecord<>("kafka-tweets", tweet));
//                        log.info("Location " + tweet.getLocation());
//                    }
//                }else{
//                    Thread.sleep(200);
//                }
//            } catch (Exception e) {
//                System.out.println(e);
//            }
//        }
        close();
    }


    public void close(){
            log.info("Closing Producer");
//            kafkaProducer.close();
            latch.countDown();
    }

//    public Tweet statusToTweet(Status status, int id){

//        Tweet.Builder tweetBuilder = Tweet.newBuilder();
//        tweetBuilder.setScreename(status.getUser().getScreenName());
//        tweetBuilder.setName(status.getUser().getName());
//        tweetBuilder.setLocation(status.getUser().getLocation());
//
//        tweetBuilder.setTweetContent(status.getText());
//        tweetBuilder.setTweetTime(new DateTime(status.getCreatedAt()));
//        tweetBuilder.setId(id);
//        tweetBuilder.setLng(-12.0);
//        tweetBuilder.setLat(12.0);

//        ArrayList<Double> coords = locationParser.parseLocation(status.getUser().getLocation());
//        tweetBuilder.setLat(coords.get(0));
//        tweetBuilder.setLng(coords.get(1));
//
//        return tweetBuilder.build();
//    }


}
