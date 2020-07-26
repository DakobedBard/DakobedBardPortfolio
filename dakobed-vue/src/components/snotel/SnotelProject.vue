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

            <v-layout row>
              <v-flex md5>
                <v-card  tile flat>
                  <v-card-text>
                <p class="title font-weight-light">
                    In this project I scrape stream flow & snow pack data from the USDA & insert records into DynamoDB.  Each day, the USDA measures
                    the stream flow & snowpack, and it's level relative to the median for 120 locations within Washington state.  I use an airflow scheduled
                    task to scrape this data every day, and have backfilled the database to allow a user to query the data to perform analysis.  The data 
                    is made available through an API (implemented & deployed as Spring Boot application running on ECS Fargate as well a serverless API using
                    AWS API Gateway * lambda) with routes for querying the data for specific locations over a range of dates. 
                </p>

                  </v-card-text>
                </v-card>
              </v-flex>
              <v-flex md7>
                <v-card tile flat>
                  <v-img :src="'https://dakobed.s3-us-west-1.amazonaws.com/snotel.png'"></v-img>
                </v-card>
              </v-flex>
            </v-layout>
            <v-layout row>
              <v-flex md 12>
                <v-card tile flat>
                  <v-card-text>
                    <h3> Motivation </h3>
                  
                  <p class="title font-weight-light">
                      Washington state experienced several summers recently of wildfires where smoke filled the sky throughout the state.  I became interested
                      in the state of the snowpack & it's impact on agriculture and the threat of wildfires.  The drought year of 2015 was of particular interest 
                      to me. 
                  </p>

                  </v-card-text>
                </v-card>
              </v-flex>
            </v-layout>
            <v-layout>
                <v-flex md5>
                  <v-card tile flat>
                    <v-card-text> 
                      <h3> Data Analysis </h3>
                  
                      To analyze the data, I queried DynamoDB & saved the data to json files for each location & each year, then implmented functions that created
                      a PySpark dataframe from a selection of locations & years.  

                      As an example of the data, I include a screenshot of the Spark Dataframe showing data for Lyman Lake in 2015 in early June.  What these numbers show is a staggering
                      lake of snowpack (which I recall because I was there in late June)


                  <p class="title font-weight-light">
                      To get a better feel for what the data meant, I performed data anlaysis using PySpark & Spark SQL.  The questions I asked of the data included
                      <ul>
                        <li>
                          For a given location and a given year, how many days was the current snow level at less than 50% of the median value (or another arbitrary value) 
     
                        </li>  
                        <li>
                          For a given location and year, what is the average percent of median of the snow level.  
                        </li>
                      </ul>  
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
                      PySpark & Spark SQL
                    </li>

                    <li>
                      API Gateway & Lambda
                    </li>                    

                    <li>
                      Spring Boot
                    </li>
                    <li>
                      Docker
                    </li>
                    <li>
                      Vue.js  & D3.js
                    </li>
                  </ul>
                  </v-card-text>
                </v-card>
              </v-flex>
              <v-flex md7>
    
                <v-card tile flat>
                  <v-img :src="'https://dakobed.s3-us-west-1.amazonaws.com/data.png'" height="300px"></v-img>
                </v-card>

              </v-flex>
            </v-layout> 


            <v-divider></v-divider>
            <v-layout>
                <v-flex md1>
                    <v-img :src="'https://dakobed.s3-us-west-1.amazonaws.com/github.png'" height="60px" width="60"></v-img>
                </v-flex>
                <v-flex md8>
                    <div class="title font-weight-medium">
                        Github Link: 
                        <a href="https://github.com/MathiasDarr/DakobedBard/tree/master/dakobed-pipelines/dakobed-snotel">Snotel pipeline</a> 
                    </div>

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