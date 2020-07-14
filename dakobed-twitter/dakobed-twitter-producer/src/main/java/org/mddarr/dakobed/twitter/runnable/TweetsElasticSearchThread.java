package org.mddarr.dakobed.twitter.runnable;


import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.apache.http.HttpHost;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.LongSerializer;
import org.elasticsearch.ElasticsearchException;
import org.elasticsearch.action.index.IndexRequest;
import org.elasticsearch.action.index.IndexResponse;
import org.elasticsearch.client.RequestOptions;
import org.elasticsearch.client.RestClient;
import org.elasticsearch.client.RestHighLevelClient;
import org.elasticsearch.common.xcontent.XContentType;
import org.elasticsearch.rest.RestStatus;
import org.joda.time.DateTime;

import org.mddarr.dakobed.twitter.AppConfig;
import org.mddarr.dakobed.twitter.locationparser.LocationParser;
import org.mddarr.dakobed.twitter.model.Tweet;
import twitter4j.Status;

import java.util.Properties;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.CountDownLatch;

public class TweetsElasticSearchThread implements Runnable{
    LocationParser locationParser;
    private final Log log = LogFactory.getLog(getClass());
    private final AppConfig appConfig;

    private final CountDownLatch latch;

    private int recordCount;

    private final ArrayBlockingQueue<Status> statusQueue;

    public TweetsElasticSearchThread(AppConfig appConfig,
                                    ArrayBlockingQueue<Status> statusQueue,
                                    CountDownLatch latch){
        this.locationParser = new LocationParser();
        this.statusQueue = statusQueue;
        this.appConfig = appConfig;
        this.latch = latch;
        this.recordCount +=1;
    }

    public void run() {
        int tweetCount = 0;




        RestHighLevelClient client = new RestHighLevelClient(
                RestClient.builder(
                        new HttpHost("localhost", 29200, "http"),
                        new HttpHost("localhost", 9201, "http")));






        while(latch.getCount() >0 ) {
            try {
                if(statusQueue.size()>0) {
                    Status status = statusQueue.poll();
                    tweetCount += 1;
                    Tweet tweet = statusToTweet(status, tweetCount);
                    System.out.println("The tweetname is " + tweet.getUsername());

                    IndexRequest request = new IndexRequest("tweets");
                    String jsonString = "{" +
                            "\"username\":\"" +  tweet.getUsername()+"\"," +
                            "\"content\":\"" +  tweet.getContent()+"\"," +
                            "\"lat\":\"" +  tweet.getLat()+"\"," +
                            "\"lng\":\"" +  tweet.getLng()+"\"," +
                            "\"location\":\""  +  tweet.getLocation() +"\""
                            + "}";

                    request.source(jsonString, XContentType.JSON);

                    try {
                        IndexResponse response = client.index(request, RequestOptions.DEFAULT);
                        System.out.println(response);

                    } catch (ElasticsearchException e) {
                        if (e.status() == RestStatus.CONFLICT) {
                        }
                        System.out.println("The problem is " + jsonString);
                    }


                }

            } catch (Exception e) {
                System.out.println(e);
            }
        }
        close();
    }

    public void close(){
        log.info("Closing Producer");
        latch.countDown();
    }

    public Tweet statusToTweet(Status status, int id){
        Tweet tweet = new Tweet();
        tweet.setUsername(status.getUser().getScreenName());
        tweet.setLocation(status.getUser().getLocation());
        tweet.setContent(status.getText());
        tweet.setLat(-12.0);
        tweet.setLng(12.0);
        return tweet;
    }
}
