package org.mddarr.dakobed.twitter.runnable;


import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.apache.http.HttpHost;
import org.apache.http.auth.AuthScope;
import org.apache.http.auth.UsernamePasswordCredentials;
import org.apache.http.client.CredentialsProvider;
import org.apache.http.impl.client.BasicCredentialsProvider;
import org.apache.http.impl.nio.client.HttpAsyncClientBuilder;
import org.elasticsearch.ElasticsearchException;
import org.elasticsearch.action.admin.cluster.health.ClusterHealthRequest;
import org.elasticsearch.action.admin.cluster.health.ClusterHealthResponse;
import org.elasticsearch.action.index.IndexRequest;
import org.elasticsearch.action.index.IndexResponse;
import org.elasticsearch.client.RequestOptions;
import org.elasticsearch.client.RestClient;
import org.elasticsearch.client.RestClientBuilder;
import org.elasticsearch.client.RestHighLevelClient;
import org.elasticsearch.common.io.stream.Writeable;
import org.elasticsearch.common.xcontent.XContentType;
import org.elasticsearch.rest.RestStatus;
import org.joda.time.DateTime;

import org.mddarr.dakobed.twitter.AppConfig;
import org.mddarr.dakobed.twitter.locationparser.LocationParser;
import org.mddarr.dakobed.twitter.model.Tweet;
import twitter4j.Status;

import java.io.IOException;
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

        final CredentialsProvider credsProvider = new BasicCredentialsProvider();
        credsProvider.setCredentials(AuthScope.ANY,
                new UsernamePasswordCredentials("master-user", "1!Master-user-password"));

        RestClientBuilder builder = RestClient.builder(new HttpHost("search-dakobedes-o5fqopyonjvcuzkvpeyoezfgey.us-west-2.es.amazonaws.com", 443, "https"))
                .setHttpClientConfigCallback(new RestClientBuilder.HttpClientConfigCallback() {
                    @Override
                    public HttpAsyncClientBuilder customizeHttpClient(HttpAsyncClientBuilder httpClientBuilder) {
                        return httpClientBuilder.setDefaultCredentialsProvider(credsProvider);
                    }
                });


        RestHighLevelClient client = new RestHighLevelClient(builder);

//
//        RestHighLevelClient client = new RestHighLevelClient(
//                RestClient.builder(
//                        new HttpHost("search-dakobedes-o5fqopyonjvcuzkvpeyoezfgey.us-west-2.es.amazonaws.com", 443, "https")
//                ));

        try {
            ClusterHealthRequest req = new ClusterHealthRequest();
            ClusterHealthResponse health =   client.cluster().health(req, RequestOptions.DEFAULT);
            System.out.println(health.toString());
        }catch(Exception e){
            System.out.println(e);
        }
        while(latch.getCount() >0 ) {
            try {
                if(statusQueue.size()>0) {
                    Status status = statusQueue.poll();
                }

            } catch (Exception e) {
                System.out.println(e);
            }
        }
        close();

//        while(latch.getCount() >0 ) {
//            try {
//                if(statusQueue.size()>0) {
//                    Status status = statusQueue.poll();
//                    tweetCount += 1;
//                    Tweet tweet = statusToTweet(status, tweetCount);
//                    System.out.println("The tweetname is " + tweet.getUsername());
//
//                    IndexRequest request = new IndexRequest("tweets");
//                    String jsonString = "{" +
//                            "\"username\":\"" +  tweet.getUsername()+"\"," +
//                            "\"content\":\"" +  tweet.getContent()+"\"," +
//                            "\"lat\":\"" +  tweet.getLat()+"\"," +
//                            "\"lng\":\"" +  tweet.getLng()+"\"," +
//                            "\"location\":\""  +  tweet.getLocation() +"\""
//                            + "}";
//
//                    request.source(jsonString, XContentType.JSON);
//
//                    try {
//                        IndexResponse response = client.index(request, RequestOptions.DEFAULT);
//                        System.out.println(response);
//
//                    } catch (ElasticsearchException e) {
//                        if (e.status() == RestStatus.CONFLICT) {
//                        }
//                        System.out.println("The problem is " + jsonString);
//                    }
//
//
//                }
//
//            } catch (Exception e) {
//                System.out.println(e);
//            }
//        }
//        close();
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
