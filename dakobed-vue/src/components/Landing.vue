<template>
  <v-container>
      <v-layout row>
        <v-flex md2>

        </v-flex> 
        <v-flex md10>
          <div class="title font-weight-medium">
            <v-layout row>
              <LandingIntro />
            </v-layout> 
          </div>
        </v-flex>
      </v-layout> 
      
      <v-layout row>
        <v-flex md6>
          <v-card  tile flat>
            
            <!-- <div v-if="getLoggedIn">
              <h2> Welcome {{ getUserEmail() }} </h2>
            </div>
            <div v-else>
              Welcome anonymous user, sign in !
            </div> -->
          </v-card>
        </v-flex>

      </v-layout>





  </v-container>
</template>

<script>

import { mapGetters } from "vuex";
import  LandingIntro  from './landing/LandingIntro'
// import axios from 'axios';
// import * as  AmazonCognitoIdentity from "amazon-cognito-identity-js";
// import { CognitoAuth } from 'amazon-cognito-auth-js'
export default {
  
  components:{

    LandingIntro
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