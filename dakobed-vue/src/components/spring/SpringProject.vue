<template>
  <v-container>
    <v-layout>
      <v-flex md2>
        <BaseNavBar v-bind:items=items />
      </v-flex>
      <v-flex md 10>
        <v-card  tile flat>
            
          <v-card-title>Spring Boot API </v-card-title>
          <v-divider></v-divider>     
          <v-card-text>
            
            <h3>Project Discription</h3>
            <p class="title font-weight-light">
              In this project I have developed an API to support the other projects in this portfolio.  I had initially planned on having this 
              run in as a dockerized application on ECS Fargate instances.  However it seemed as though it was going to be too expensive to have 
              running continuously      
            </p>

            <h3> Technologies Used </h3>
              <ul class="title font-weight-light">
                <li>
                  Spring Boot
                </li>
                <li>
                  AWS Elastic Container Service 
                </li>
                <li>
                  DnamoDB 
                </li>
                <li>
                  Java ElasticSearch high level REST client 
                </li>


              </ul>
              <v-divider></v-divider>

            </v-card-text>
            
        </v-card>
         <GithubFooter v-bind:link=link v-bind:link_title= link_title />
      </v-flex>
    </v-layout>

  </v-container>    
</template>

<script>
import BaseNavBar from '../BaseNavBar'
import GithubFooter from '../shared/GithubFooter'
export default {
  created(){
    console.log("I GET CREATED")
  },
  components:{
      BaseNavBar,
      GithubFooter
  },
  data(){
    return {
      link: 'https://github.com/MathiasDarr/DakobedBard/tree/master/dakobed-services',
      link_title: 'Spring Boot ECS project',
      items: [
            { title: 'Project Description', icon: 'mdi-view-dashboard', route:'/spring' },
        ],

    }
  },


}
</script>