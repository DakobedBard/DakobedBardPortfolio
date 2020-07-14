package org.mddarr.dakobed.twitter;

import com.typesafe.config.Config;

public class AppConfig {

    private final String sourceTopicName;
    private final String elasticSearchURL;
    private final String tweetTopicName;
    private final String applicationId;
    private final String tweetTopic;
    public AppConfig(Config config, String[] arguments) {

        this.tweetTopic = arguments[0];

        // this.bootstrapServers = "http://kafka:9092";
//        this.schemaRegistryUrl = "http://schema-registry:8081";
        this.elasticSearchURL = "http://elasticsearch7:29200";

        this.sourceTopicName = "kafka.source.tweet."+arguments[0];
        this.tweetTopicName = arguments[0];

        this.applicationId = "my-app-v1.0.0"; //config.getString("kafka.streams.application.id");
    }

    public int getQueuCapacity(){return 100;}

    public String getSourceTopicName() {
        return sourceTopicName;
    }


    public String getTweetTopicName() {
        return tweetTopicName;
    }

    public String getApplicationId() {
        return applicationId;
    }

    public String getTweetKeyword(){return tweetTopic;}


}
