<template>
  <v-container>
    <v-layout row>
      <v-flex md2>
        <BaseNavBar v-bind:items=items />
      </v-flex>
      <v-flex md10>
        <v-card flat>
            
          <v-card-title>Spring Boot API </v-card-title>
          <v-divider></v-divider>     
          <v-card-text>

              <v-layout row>
              <v-flex md4>
                <Paragraph v-bind:title=introdution_title v-bind:text = introdution />
              <v-divider></v-divider>
              <TechnologiesList v-bind:technologies=technologies />
              <v-divider></v-divider>
              <GithubFooter v-bind:link=link v-bind:link_title= link_title />
              </v-flex>
              <v-flex md8>
                <ImageComponent :image_src="spring_ecs_diagram" v-bind:caption="'Application Architecture'" v-bind:height="'600px'" v-bind:width="'2200px'" />
              </v-flex>
            </v-layout>
          </v-card-text>
            
        </v-card>
         
      </v-flex>
    </v-layout>

  </v-container>    
</template>

<script>
/* eslint-disable */
import BaseNavBar from '../BaseNavBar'
import GithubFooter from '../shared/GithubFooter'
import Paragraph from '../shared/Paragraph'
import TechnologiesList from '../shared/TechnologiesList'
import ImageComponent from '../shared/ImageComponenet'
export default {
  created(){

  },
  components:{
      BaseNavBar,
      GithubFooter,
      Paragraph,
      TechnologiesList,
      ImageComponent
  },
  data(){
    return {
      link: 'https://github.com/MathiasDarr/DakobedBard/tree/master/dakobed-ecs-services',
      link_title: 'Spring Project',
      items: [
        { title: 'Project Description', icon: 'mdi-view-dashboard', route:'/spring' },
      ],
      

      introdution: `In this project I have developed a Spring Boot API to support the other projects in this portfolio.  I had initially planned on having this 
              portfolio project's backend run as a dockerized application on ECS Fargate instances.  However it seemed as though it was going to be too expensive to  
              run continuously, and I decided to use a serverless API instead.`,
      introduction_title: `Project Introduction`,
      
      architecture:``,
      
      spring_ecs_diagram: 'https://dakobedbard.s3-us-west-2.amazonaws.com/spring_ecs_diagram.png',

      technologies: [
        "Spring Boot",
        "AWS Elastic Container Service, Elastic Container Repository",
        "AWS CloudFormation for launching stack of resources including VPC with a public & and private subnet",
        "DynamoDB",
        "Java ElasticSearch high level REST client"
      ]

    }
  },


}
</script>