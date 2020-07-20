<template>
  <v-container>
      <v-layout row>
        <v-flex md6>
          <v-card  tile flat>
            


            <div v-if="getLoggedIn">
              <h2> Welcome {{ getUserEmail() }} </h2>
            </div>
            <div v-else>
              Welcome anonymous user, sign in !
            </div>
          </v-card>
        </v-flex>

      </v-layout> 
        <v-layout row>
        
        <v-flex md6>
          
          <v-card  tile flat>
            <v-card-text>
            <v-divider></v-divider>
            <p>
                Hello, I am Mathias
            </p>
            
            <p> I am a software/data/cloud engineer pursuing new oppertunities in the Seattle area and remotely.  As evidenced by the projects in my Portfolio
            and the many technologies which I have first hand experience with.  I have a passion for learning and challenging my self to learn new technologies.  
            My primary programming languages are Python & Java, but also have experience with others such as javascript & C++.  For the past several years I have 
            been becoming more and more proficient with AWS cloud computing, having made extensive use for this projects
            </p>

            <span>

            </span>
            I am logged in {{ getLoggedIn }}
            </v-card-text>
          </v-card>
        </v-flex>
        <v-flex md6>
          <v-card  tile flat >
            <v-img :src="'https://s3-us-west-2.amazonaws.com/dalinar-mir.com/profile.jpg'" height="700px" width="560"></v-img>

          </v-card>
        </v-flex>
      </v-layout> 

    <v-layout>
      <v-flex>

      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";
// import axios from 'axios';
// import * as  AmazonCognitoIdentity from "amazon-cognito-identity-js";
// import { CognitoAuth } from 'amazon-cognito-auth-js'
export default {
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
    if(this.getLoggedIn){

      console.log("logg")

    }else{
      console.log("NOO")
    }
  },
  data(){
    return {

    }
  },
  computed: {
    ...mapGetters(["getLoggedIn","getJwtAccessToken", "getIdToken"]),

  },
}
</script>