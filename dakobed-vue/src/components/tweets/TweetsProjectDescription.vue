<template>
  <v-container>
    <v-layout>
      <v-flex md2>
        <BaseNavBar v-bind:items=items />
      </v-flex>
      
      <v-flex md10>
        <v-card flat>
            <v-card  tile flat>
            
            <v-card-title>Tweets Pipeline & Querying Service Project</v-card-title>
            <v-divider></v-divider>     
            <v-card-text>
            
            <h3>Project Discription</h3>
            <p class="title font-weight-light">
                In this project I include a multithreaded Java program to stream tweets using the twitter4j library and to push them into an Elasticsearch 
                index.  To allow users to query the tweets, I expose Spring Boot API endpoints to query the Elasticsearch index with location (lat & long) and
                keyword query parameters using the high level Java REST Elasticsearch client.  While testing I used docker to host Elasticsearch.  Eventually
                I started to use the AWS manged Elasticsearch service.  
                
                   Using the google maps Javascript API I allow users to query
                the tweets interactively.    


              </p>
              <h3> Motivation </h3>
            <p class="title font-weight-light">
                    I initially intended it to be used as a tool to be used to track what people were tweeting about with respect to the primary elections.  Now that
                    the primaries have passed, the focus has shifted in seeing what people are tweeting about with respect to the most relevent issue of today, the 
                    coronovirus.  
                </p>
            <h3> Technologies Used </h3>
            
            <ul class="title font-weight-light">
              <li>
                Spring Boot
              </li>
              <li>
                Elasticsearch Java high level REST client
              </li>

              <li>
                Google maps Javascript API
              </li>
              <li>
                Vue JS
              </li>
            </ul>

            <v-divider></v-divider>     
            <span>
 
            </span>
            <v-layout>
                <v-flex md1>
                    <v-img :src="'https://dakobed.s3-us-west-1.amazonaws.com/github.png'" height="60px" width="60"></v-img>
                </v-flex>
                <v-flex md8>
                    <p class="title font-weight-medium">
                    Github Links
                    </p>
                    <ul class="title font-weight-light">
                      <li>
                        <a href="https://github.com/MathiasDarr/DakobedBard/tree/master/dakobed-pipelines/dakobed-twitter">Tweets Elasticsearch pipeline</a> 
                        
                      </li>
        
                    </ul>
                </v-flex>
            </v-layout>

            



            </v-card-text>
          </v-card>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>

import BaseNavBar from  '../BaseNavBar'


export default {
    components:{
      BaseNavBar      
    },
    data(){

      return {
        items: [
          { title: 'Tweets Project Description', icon: 'mdi-view-dashboard', route:'/tweetsintro' },
          { title: 'Tweets Map', icon: 'mdi-image', route:'/tweets' },
          {title: 'Tweets Landing',route:'/tweetslanding'}


        ],
      }
    }

}

</script>