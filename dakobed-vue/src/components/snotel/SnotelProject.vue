<template>
  <v-container>
    <v-layout>
      <v-flex md2>
        <BaseNavBar v-bind:items=items />
      </v-flex>
          
      <v-flex md10>
        <v-card flat>
            <v-card  tile flat>
            
            <v-card-title>Snotel Pipeline </v-card-title>
            <v-divider></v-divider>     
            <v-card-text>
            
            <h3>Project Discription</h3>
            <p class="title font-weight-light">
                In this project I scrape stream flow & snow pack data from the USDA & insert records into DynamoDB.  Each the day, the USDA measures
                the stream flow & snowpack, and it's level relative to the median for 120 locations within Washington state.  I use an airflow scheduled
                task to scrape this data every day, and have backfilled the database to allow a user to query the data to perform analysis.  The data 
                is made available through a Spring Boot API with routes for querying the data for specific locations over a range of dates. 


            </p>
            <h3> Motivation </h3>
            <p class="title font-weight-light">
                Washington state experienced several summers recently of wildfires where smoke filled the sky throughout the state.  I became interested
                in the state of the snowpack & it's impact on agriculture and the threat of wildfires.
                </p>
            <h3> Technologies Used </h3>
            
            <ul class="title font-weight-light">
              <li>
                Beautiful Soup
              </li>
              <li>
                DynamoDB
              </li>
              <li>
                Spring Boot
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
                        <a href="https://github.com/MathiasDarr/DakobedBard/tree/master/dakobed-pipelines/dakobed-snotel">Snotel pipeline</a> 
                        
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
      
    data () {
      return {

        items: [
          { title: 'Snotel Project Description', icon: 'mdi-view-dashboard', route:'/snotel' },
          { title: 'Snotel Data', icon: 'mdi-image', route:'/snoteldata' },
        ],

      }
    },
}
</script>