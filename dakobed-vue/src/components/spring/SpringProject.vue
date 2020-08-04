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
                  Keras deep learning library on AWS EC2 GPU instance
                </li>
                <li>
                  AWS Lamda & API Gateway serverless API endpoints for deployment of the Keras model 
                </li>
              </ul>
              <v-divider></v-divider>
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
                         <a href="https://www.w3schools.com">Music Information Retrieval</a> 
                      </li>
        
                    </ul>
                </v-flex>
              </v-layout>
            </v-card-text>
          </v-card>
      </v-flex>
    </v-layout>
  </v-container>    
</template>

<script>
import BaseNavBar from '../BaseNavBar'
export default {
  components:{
      BaseNavBar
  },
  data(){
    return {

      items: [
            { title: 'Project Description', icon: 'mdi-view-dashboard', route:'/spring' },

        ],

    }
  },


}
</script>