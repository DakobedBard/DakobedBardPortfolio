package org.mddarr.dakobedtwitterservice.config;


import org.apache.http.HttpHost;
import org.elasticsearch.client.RestClient;
import org.elasticsearch.client.RestHighLevelClient;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.elasticsearch.client.ClientConfiguration;
import org.springframework.data.elasticsearch.client.RestClients;
import org.springframework.data.elasticsearch.core.ElasticsearchOperations;
import org.springframework.data.elasticsearch.core.ElasticsearchRestTemplate;
import org.springframework.data.elasticsearch.repository.config.EnableElasticsearchRepositories;

@Configuration
@EnableElasticsearchRepositories(basePackages = "org.mddarr.tweetsservice.dao")
@ComponentScan(basePackages = { "org.mddarr.tweetsservice" })
public class Config {
//    @Bean
//    RestHighLevelClient client() {
//

//        ClientConfiguration config = ClientConfiguration.builder().connectedTo("https://search-dakobedes-o5fqopyonjvcuzkvpeyoezfgey.us-west-2.es.amazonaws.com","80")
//                .build();
//
//        ClientConfiguration clientConfiguration = ClientConfiguration.builder()
//
//                .connectedTo("https://search-dakobedes-o5fqopyonjvcuzkvpeyoezfgey.us-west-2.es.amazonaws.com" ) //, "localhost:9200")
//                .withBasicAuth("master-user","1!Master-user-password")
//                .build();
//
//        return RestClients.create(config).rest();
//    }

    @Bean
    RestClient client(){
        RestClient restClient = RestClient.builder(
                new HttpHost("https://search-dakobedes-o5fqopyonjvcuzkvpeyoezfgey.us-west-2.es.amazonaws.com", 80, "https")).build();
        return restClient;
    }



//    @Bean
//    public ElasticsearchOperations elasticsearchTemplate() {
//        return new ElasticsearchRestTemplate(client());
//    }

}