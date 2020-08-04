package org.mddarr.dakobedservices.config;


import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import org.apache.http.HttpHost;
import org.apache.http.auth.AuthScope;
import org.apache.http.auth.UsernamePasswordCredentials;
import org.apache.http.client.CredentialsProvider;
import org.apache.http.impl.client.BasicCredentialsProvider;
import org.apache.http.impl.nio.client.HttpAsyncClientBuilder;
import org.elasticsearch.client.RestClient;
import org.elasticsearch.client.RestClientBuilder;
import org.elasticsearch.client.RestHighLevelClient;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.elasticsearch.core.ElasticsearchOperations;
import org.springframework.data.elasticsearch.core.ElasticsearchRestTemplate;
import org.springframework.data.elasticsearch.repository.config.EnableElasticsearchRepositories;

@Configuration
@EnableElasticsearchRepositories(basePackages = "org.mddarr.tweetsservice.dao")
@ComponentScan(basePackages = { "org.mddarr.tweetsservice" })
public class Config {

    @Value("${es_host}")
    String es_host;

    @Value("${es_port}")
    String es_port;

    @Value("${amazon.dynamodb.endpoint}")
    private String dynamoDbEndpoint;

    @Value("${amazon.aws.accessKey}")
    private String awsAccessKey;

    @Value("${amazon.aws.secretKey}")
    private String awsSecretKey;


    @Bean
    public AmazonS3 generateS3Client() {
        AmazonS3 s3Client = AmazonS3ClientBuilder.standard().build() ;
        return s3Client;
    }
    @Bean
    public AmazonDynamoDB amazonDynamoDB(){
        AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard()
                .withRegion("us-west-2")
                .build();
        return client;
    }

//    @Bean
//    public AWSCredentials amazonAWSCredentials() {
//        return new BasicAWSCredentials(awsAccessKey, awsSecretKey);
//    }

    @Bean
    RestHighLevelClient client(){

        String scheme;
        if(es_host=="localhost"){
            scheme ="http";
        }else{
            scheme = "https";
        }
        final CredentialsProvider credsProvider = new BasicCredentialsProvider();
        credsProvider.setCredentials(AuthScope.ANY,
                new UsernamePasswordCredentials("master-user", "1!Master-user-password"));

        RestClientBuilder builder = RestClient.builder(new HttpHost(es_host, Integer.parseInt(es_port), "http"))
                .setHttpClientConfigCallback(new RestClientBuilder.HttpClientConfigCallback() {
                    @Override
                    public HttpAsyncClientBuilder customizeHttpClient(HttpAsyncClientBuilder httpClientBuilder) {
                        return httpClientBuilder.setDefaultCredentialsProvider(credsProvider);
                    }
                });
        RestHighLevelClient client = new RestHighLevelClient(builder);
        return client;
    }


    @Bean
    public ElasticsearchOperations elasticsearchTemplate() {
        return new ElasticsearchRestTemplate(client());
    }

}