<template>
  <v-container>
    <v-layout>
      <v-flex md2>
        <BaseNavBar v-bind:items=items />

      </v-flex>
            <v-flex md10>
        <v-card flat>
            <v-card  tile flat>
            
            <v-card-title>Trip Reports Project</v-card-title>
            <v-divider></v-divider>     
            <v-card-text>
            
            <h3>Project Discription</h3>
            <p class="title font-weight-medium">



              </p>
              <h3> Motivation </h3>
            <p class="title font-weight-medium">

                </p>
            <h3> Technologies Used </h3>
            
            <ul class="title font-weight-light">
              <li>
                Spring Boot
              </li>
              <li>
                Kafka Streams Spring Binder
              </li>

              <li>
                DynamoDB
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
                    <p class="title font-weight-medium">   
                        <a href="https://github.com/MathiasDarr/DakobedBard/tree/master/dakobed-events">Event Driven Microservices </a> 
          
                    </p>
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

import BaseNavBar from '../BaseNavBar'


export default {
    
    components:{
        BaseNavBar
    },
    
    data(){

        return {
            items: [
                { title: 'Trip Reports Project Description', icon: 'mdi-view-dashboard', route:'/reportsproject' },
                { title: 'Trip Reports', icon: 'mdi-image', route:'/reports' },

          ],
        }
    }
}
</script>