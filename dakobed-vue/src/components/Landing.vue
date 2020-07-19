<template>
  <v-container>

      <v-layout row>
        <v-flex md6>
          <v-card  tile flat>
            <v-card-text>
            <p>
                Hello, I am Mathias
            </p>
            
            <v-divider></v-divider>
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
      getUserInfo(){
        var jwtDecode = require('jwt-decode');
        
        console.log(jwtDecode(this.getIdToken))
        // var jwtToken = this.getJwtAccessToken
        // var authData = {
        //   ClientId : process.env.VUE_APP_COGNITO_CLIENT_ID,
        //   AppWebDomain: process.env.VUE_APP_COGNITO_APP_DOMAIN,
        //   TokenScopesArray :['openid', 'email'],
        //   RedirectUriSignIn :'/',
        //   RedirectUriSignOut: '/',
        //   UserPoolId: process.env.VUE_APP_COGNITO_USERPOOL_ID
        // }
        // var auth = new CognitoAuth(authData)
        // var jwtToken = auth.getSignInUserSession().getAccessToken().jwtToken;

        // get the decoded payload and header
        // var decoded = jwt.decode(this.getIdToken);
        // console.log(decoded.header);
        // console.log(decoded.payload) 

        // const USERINFO_URL = process.env.VUE_APP_COGNITO_APP_DOMAIN+ '/oauth2/userInfo';
        // var requestData = {
        //     headers: {
        //         'Authorization': 'Bearer '+ jwtToken
        //     }
        // }
        // return axios.get(USERINFO_URL, requestData).then(response => { 
        //     return response.data;
        // });
    }
  },
  created(){
    console.log("welcome..")
    if(this.getLoggedIn){
      console.log("logg")
      this.getUserInfo()

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