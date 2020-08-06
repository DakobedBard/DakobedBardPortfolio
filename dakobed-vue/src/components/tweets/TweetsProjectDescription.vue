<template>
    <v-container>

      <v-layout>
        <v-flex md2>
        <BaseNavBar v-bind:items=items />
        </v-flex>
        <v-flex md10>

          <v-layout row>
            <v-flex md8>
              <v-card  tile flat>
                <v-card-text>
                  <v-card-title>
                    Tweets Pipeline & analysis
                  </v-card-title>
                  <v-divider></v-divider>
                  <Paragraph v-bind:title = "''" v-bind:text = introduction />

                </v-card-text>
              </v-card>
            </v-flex>
            
            <v-flex md4>
              <v-card  tile flat >
              </v-card>
            </v-flex>
          </v-layout>

          <v-layout row>
            <TechnologiesList v-bind:technologies=technologies />
            </v-layout>
          <v-layout row>
            <GithubFooter v-bind:link = link v-bind:link_title = link_title />
          </v-layout>

        </v-flex>
  
      </v-layout> 
    </v-container>


  <!-- <v-container>
    <v-layout>
      <v-flex md2>
        <BaseNavBar v-bind:items=items />
      </v-flex>
      
      <v-flex md10>
        <v-card flat>
          <Paragraph v-bind:title = "''" v-bind:text = porfolio_introduction />
            
            <v-card-title>Tweets Pipeline & Querying Service Project</v-card-title>
            <v-divider></v-divider>     
            <v-card-text>
            

              <h3> Motivation </h3>
            <p class="title font-weight-light">
                    I initially intended it to be used as a tool to be used to track what people were tweeting about with respect to the primary elections.  Now that
                    the primaries have passed, the focus has shifted in seeing what people are tweeting about with respect to the most relevent issue of today, the 
                    coronovirus.  
                </p>

            <v-divider></v-divider>     

        
          </v-card-text>

        </v-card>
        <v-layout row>
            <TechnologiesList v-bind:technologies=technologies />
        </v-layout>
        <v-layout row>
            <GithubFooter v-bind:link = link v-bind:link_title = link_title />
        </v-layout>


      </v-flex>
    </v-layout>
  </v-container>     -->
</template>
<script>

import BaseNavBar from  '../BaseNavBar'
import Paragraph from '../shared/Paragraph'
import GithubFooter from '../shared/GithubFooter'
import TechnologiesList from '../shared/TechnologiesList'


export default {
    components:{
      BaseNavBar,
      Paragraph,
      GithubFooter,
      TechnologiesList     
    },
    data(){

      return {
        introduction: `In this project I include a multithreaded Java program to stream tweets using the twitter4j library and to push them into an Elasticsearch 
                index.  To allow users to query the tweets, I expose Spring Boot API endpoints to query the Elasticsearch index with location (lat & long) and
                keyword query parameters using the high level Java REST Elasticsearch client.  While testing I used docker to host Elasticsearch.  Eventually
                I started to use the AWS manged Elasticsearch service.`,



        link: "https://github.com/MathiasDarr/DakobedBard/tree/master/dakobed-twitter",
        link_title:"Virus Tweets Project",
        items: [
          { title: 'Tweets Project Description', icon: 'mdi-view-dashboard', route:'/tweetsintro' },
        ],
        technologies: [
          "Java & twitter4j library",
          "ElasticSearch Java highlevel REST client & python client",
          "Airflow",
          "Spark & NLTK nlp library",
          "AWS EMR"
        ],


      }
    }

}

</script>