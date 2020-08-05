<template>
  <v-container>
    <v-layout row>
      <v-flex md2>

      </v-flex> 
      <v-flex md10>
        <div class="title font-weight-medium">
          <v-layout row>
            <v-flex md8>
              <v-card  tile flat>
                <v-card-text>
                  <v-card-title>
                    Mathias Darr
                  </v-card-title>
                  <v-card-subtitle>
                      {{ title }}
                  </v-card-subtitle>
                  <v-divider></v-divider>
                  <Paragraph v-bind:title = "''" v-bind:text = porfolio_introduction />
                  
                  <TechnologiesList v-bind:technologies=technologies />
                  <GithubFooter v-bind:link = link v-bind:link_title = link_title />
                </v-card-text>
              </v-card>
            </v-flex>

            <v-flex md4>
              <v-card  tile flat >
                <v-img :src="'https://s3-us-west-2.amazonaws.com/dalinar-mir.com/profile.jpg'" height="700px" width="560"></v-img>
              </v-card>
            </v-flex>
          </v-layout>
        
        </div>
      </v-flex>
    </v-layout> 
  </v-container>
</template>

<script>

import { mapGetters } from "vuex";

import GithubFooter from '../components/shared/GithubFooter'
import TechnologiesList from './shared/TechnologiesList'
import Paragraph from './shared/Paragraph'

// import axios from 'axios';
// import * as  AmazonCognitoIdentity from "amazon-cognito-identity-js";
// import { CognitoAuth } from 'amazon-cognito-auth-js'
export default {
  
  components:{
    GithubFooter,
    TechnologiesList,
    Paragraph
  },

  methods:{
    getUserEmail(){
        var jwtDecode = require('jwt-decode');
        var decoded_token = jwtDecode(this.getIdToken)
        return decoded_token.email.split('@')[0]
    }
  },
  created(){
    var name = "mddarr@gmail.com"
    var split = name.split("@")
    console.log("Welcome " + split[0])
    console.log("welcome..")

  },
  data(){
    return {
      title: 'Software, Data & Cloud Engineer.',

      porfolio_introduction:`I am an engineer in the Seattle area looking for new oppertunities.  This portfolio project is a compilation
      of what I have deemed to be my best work.  Some of the projects included are running live in the AWS cloud, while others not due to budget constraints. 
      `,

      introduction_title: 'Bio',
      technologies: [
        "Vuejs, Vuetify, Vuex, Axios, D3js",
        "Sring Boot",
        "Keras Deep Learning Library",
        "Librosa Audio Processing Library",
        "PySpark, AWS EMR, Airflow",
        "Kafka Streams, Kafka Connect",
        "AWS Serverless Application Model, API Gateway, Lambda, Simple Queue Service, Cognito",
        "AWS EC2, DynamoDB, S3",
        "AWS Elastic Container Service, Elastic Container Repository",
        "ElasticSearch",
        ""
      ],
      link:'https://github.com/MathiasDarr/DakobedBard/tree/master/dakobed-vue',
      link_title: 'Vue Application',
    }
  },
  computed: {
    ...mapGetters(["getLoggedIn","getJwtAccessToken", "getIdToken"]),

  },
}
</script>