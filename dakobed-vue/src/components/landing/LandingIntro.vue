<template>

  <v-container>
        
    <v-layout row>
        <v-flex md8>
          
          <v-card  tile flat>
            <v-card-text>
     
            <p class="title font-weight-medium">
                Mathias Darr
            </p>
            
            <p class="title font-weight-light"> 
              Software/Data/Cloud Engineer
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
            <v-divider></v-divider>
          <h3>

          </h3>
          <div class="title font-weight-medium"> 
            <a href="https://dakobed.s3-us-west-1.amazonaws.com/Resume.pdf">Resume </a>
          </div>


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