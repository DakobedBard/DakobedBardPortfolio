<template>
  <v-container>
    <v-layout>
      <v-flex md2>
        <BaseNavBar v-bind:items=items />
      </v-flex>
      <v-flex md10>
        <v-card flat>
          <v-card-text>
            <v-card-title>
              Tweets Kafka Spark Pipeline
            </v-card-title>
            <Paragraph v-bind:title="'Project Description'" v-bind:text = introduction />
            <Paragraph v-bind:title="'Tweets Analysis'" v-bind:text = analysis />
            <Paragraph v-bind:title=kafka_tile v-bind:text = kafka_pipeline />

            <TechnologiesList v-bind:technologies = technologies /> 
            <v-layout row>
                <GithubFooter v-bind:link = link v-bind:link_title = link_title />
            </v-layout>
          </v-card-text>
        </v-card>
        
      </v-flex>  
    </v-layout>


  </v-container>
</template>

<script>

// import BaseNavBar from '../BaseNavBar'
import Paragraph from '../shared/Paragraph'
import TechnologiesList from '../shared/TechnologiesList'
import GithubFooter from '../shared/GithubFooter'
import BaseNavBar from '../BaseNavBar'

export default {
    components:{
        TechnologiesList,
        Paragraph,
        GithubFooter,
        BaseNavBar
    },

    data(){
        return{
            items: [
                { title: 'Tweets Project', route:'/tweets' },          
            ],
            introduction: `In this project I include a multithreaded Java program to stream tweets using the twitter4j library and to push them into an Elasticsearch 
                index.  To allow users to query the tweets, I expose Spring Boot API endpoints to query the Elasticsearch index with location (lat & long) and
                keyword query parameters using the high level Java REST Elasticsearch client.  I made use of Apache Airflow to write the twets to parquet files and
                write to S3 every hour`,
            methods: ``,

            kafka_tile: 'Kafka Spark Streaming Pipeline',
            kafka_pipeline: `I make use of Kafka to push tweets into a Kakfa topic.  From here I process them with Spark streaming.
            
            
            `,

            analysis: `I performed natural language processing with Spark & the NLTK library to develop a K means clustering model.  To run this model on the full dataset,
                I made use of Amazons Elastic Map Reduce service (EMR).
            `,
            
            link_title: 'Tweets Pipeline',
            link:'https://github.com/MathiasDarr/DakobedBard/tree/master/dakobed-twitter',
            technologies: [
                "Java & twitter4j library",
                "ElasticSearch Java highlevel REST client & python client",
                "Airflow",
                "Spark & NLTK nlp library",
                "AWS EMR",
                "Kafka & Spark Streaming",
                "Parquet, Avro"
            ],

        }
    }
}
</script>