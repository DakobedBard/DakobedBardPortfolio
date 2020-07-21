<template>

  <v-container>
        
    <v-layout row>
        <v-flex md8>
          
          <v-card  tile flat>
            <v-card-text>
     
            <p class="title font-weight-medium">
                Hello, I am Mathias
            </p>
            
            <p class="title font-weight-light"> I am a software/data/cloud engineer pursuing new oppertunities in the Seattle area and remotely.  As evidenced by the projects in my Portfolio
            and the many technologies which I have first hand experience with.  I have a passion for learning and challenging my self to learn new technologies.  
            My primary programming languages are Python & Java, but also have experience with others such as javascript & C++.  For the past several years I have 
            been becoming more and more proficient with AWS cloud computing, having made extensive use for this projects
            </p>


            <h3> Technologies Used</h3>

            <p class="title font-weight-light">
              This static portfolio website is hosted in an S3 bucket.  The backend Spring Boot API is running as a dockerized container running on an AWS Elastic
              Container Service Fargate instance.

             
            </p>
            <span class="title font-weight-medium">
              This project makes used of the following technologies

            </span>
            <ul class="title font-weight-light"> 
              <li>
                Vue JS, Vuex, Vuetify
              </li>
              <li>
                Spring Boot
              </li>
              <li>
                AWS S3, ECS, Cognito, Kinesis Firehose, Lambda

                
              </li>
            </ul>


            </v-card-text>
          </v-card>
        </v-flex>

        <v-flex md4>
          <v-card  tile flat >
            <v-img :src="'https://s3-us-west-2.amazonaws.com/dalinar-mir.com/profile.jpg'" height="700px" width="560"></v-img>

          </v-card>
        </v-flex>
      </v-layout>
</v-container>

</template>
<script>
export default {
    
}
</script>