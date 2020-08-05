<template>
  <v-container>
    <v-layout>
      <v-flex md2>
        <BaseNavBar v-bind:items=items />
      </v-flex>
          
      <v-flex md10>
        <v-card flat>
          <v-card-title>Snotel Pipeline </v-card-title>
          <v-divider></v-divider>     
          <v-card-text>
            
            
            <v-layout row>
              <v-flex md5>
                <Paragraph v-bind:title=introduction_title v-bind:text = introduction />
                <Paragraph v-bind:title=motviation_title v-bind:text = motivation />
              </v-flex>
              <v-flex md7>
              <ImageComponent :image_src="snotel_map_image" v-bind:caption="' Washington State Snotel Map'" v-bind:height="'600px'" v-bind:width="'900px'" />


              </v-flex>
            </v-layout>

            
            <v-layout row>
              <v-flex md5>
                <Paragraph v-bind:title=archticture_title v-bind:text = archtiecture />
              </v-flex>
              <v-flex md7>
                <ImageComponent :image_src="snotel_diagram" v-bind:caption="' Serverlss Application Architecture'" v-bind:height="'600px'" v-bind:width="'900px'" />
              </v-flex>
            </v-layout>

            <v-layout row>
              <v-flex md6>
                <Paragraph v-bind:title=analysis_title v-bind:text = analysis />
              </v-flex>
              <v-flex md5 offset-1>
                <ImageComponent :image_src="spark_dataframe_image" v-bind:caption="' Spark SQL dataframe 2015 snowpack Lyman Lake'" v-bind:height="'300px'" />
              </v-flex>
            </v-layout>
            
            <TechnologiesList v-bind:technologies = technologies />
            <v-divider></v-divider>
            <GithubFooter v-bind:link=link v-bind:link_title=link_title />

          
            </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>

</template>


<script>

import GithubFooter from '../shared/GithubFooter'
import BaseNavBar from  '../BaseNavBar'
import Paragraph from '../shared/Paragraph'
import TechnologiesList from '../shared/TechnologiesList'
import ImageComponent from '../shared/ImageComponenet'


export default {
    components:{
        BaseNavBar,
        GithubFooter,
        Paragraph,
        TechnologiesList,
        ImageComponent
        
    },
      
    data () {
      return {
        link:'https://github.com/MathiasDarr/DakobedBard/tree/master/dakobed-snotel',
        link_title: 'Snotel Pipeline',
        items: [
          { title: 'Snotel Project Description', icon: 'mdi-view-dashboard', route:'/snotel' },
          { title: 'Snotel Data', icon: 'mdi-image', route:'/snoteldata' },
          
        ],

      introduction:` In this project I scrape stream flow & snow pack data from the USDA & insert records into DynamoDB.  Each day, the USDA measures
          the stream flow & snowpack, and it's level relative to the median for 120 locations within Washington state.  I use an airflow scheduled
          task to scrape this data every day, and have backfilled the database to allow a user to query the data to perform analysis.  The data 
          is made available through an API (implemented & deployed as Spring Boot application running on ECS Fargate as well a serverless API using
          AWS API Gateway * lambda) with routes for querying the data for specific locations over a range of dates. `,

      introduction_title: 'Project Desrption',
      motviation_title: 'Motivation',
      motivation:`Washington state experienced several summers recently of wildfires where smoke filled the sky throughout the state.  I became interested
        in the state of the snowpack & it's impact on agriculture and the threat of wildfires.  The drought year of 2015 was of particular interest to me. `,
      methods_title: 'Methods',
      analysis: ` To analyze the data, I queried DynamoDB & saved the data to json files for each location & each year, then implmented functions that created
        a PySpark dataframe from a selection of locations & years.  As an example of the data, I include a screenshot of the Spark Dataframe showing data for Lyman 
        Lake in 2015 in early June.  What these numbers show is a staggering lake of snowpack (which I recall because I was there in late June)`,
      analysis_title: 'Analysis',

      archticture_title: 'Query Service Archtiecture',
      archtiecture : `
        I expose this data to be queried by location through a serverless API with a lambda function making a query to DynamoDB.  The API is defined using
        swagger which also enables CORS to allow requests from the browser.  I had initially been using postgres, but something about writing a query such
        as SELECT * FROM snotel_table WHERE location = 'Lyman Lake' seemed inefficient.  It seemed as though a noSQL database would be far more efficient for supporting
        a query by the primary/hash key (location ID) & a range/sort key (date of measurement)    

      `,
      snotel_map_image: 'https://dakobed.s3-us-west-1.amazonaws.com/snotel.png',
      snotel_diagram: 'https://s3-us-west-2.amazonaws.com/dalinar-mir.com/snotel_diagram.png',
      spark_dataframe_image: 'https://dakobed.s3-us-west-1.amazonaws.com/data.png',


      technologies: [
        "Beautiful Soup",
        "AWS Serverless Application Model to define & deploy Lambda function & API Gateway",
        "Swagger to define API & enable CORS",
        "Vue.js & D3",
        "PySpark & Spark SQL"
        ]

      }
    },
}
</script>