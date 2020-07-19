<template>
  <v-app>
    <nav>
    <div>
      <v-toolbar dark prominent  height="340px" src="https://dakobed.s3-us-west-1.amazonaws.com/panorama.jpg">

      </v-toolbar>
    </div>

      <v-toolbar flat dark class="py-0 mt">
        
        <v-app-bar-nav-icon class ="grey--text" @click="drawer = !drawer"></v-app-bar-nav-icon>
          <v-toolbar-title class="grey--text">
            <span class="font-weight-light">Dakobed</span>
            <span>Bard</span>
          </v-toolbar-title>
          <v-spacer></v-spacer>
      <v-toolbar-items class = "hidden-xs-only">
        <v-btn  v-for="item in menuItems" :key="item.title" @click="selectRoute(item.route)" class ="grey--text" >
        <!-- <v-btn  v-for="item in menuItems" :key="item.title" :to= "item.route" class ="grey--text" > -->
          <v-icon left >
          </v-icon>
          {{item.title}}
        </v-btn>
      </v-toolbar-items>
      
      <v-spacer></v-spacer>
      </v-toolbar>
    </nav>

    <router-view></router-view>
  </v-app>
</template>

<script>

import router from './router'
import { mapGetters } from "vuex";
import axios from 'axios';



export default {
  name: 'App',

  components: {
    
  },
  created(){

  
    
  },
  data(){
    return {
        drawer: false,

        menuItems:[

          {title:'Landing', icon:'image-filter-hdr', route:'/' }, 
          {title:'Gallery', icon:'image-filter-hdr', route:'/gallery/' },  
          {title:'Music', icon:'image-filter-hdr', route:'/music/' }, 
          // {title:'Tweets', icon:'image-filter-hdr', route:'/tweets/' }, 
          {title:'Transcriptions', icon:'image-filter-hdr', route:'/transcriptions/' }, 
          {title:'Maestro', icon:'image-filter-hdr', route:'/maestro/' }, 
          // {title:'Registration', icon:'image-filter-hdr', route:'/register/' }, 

        ],

        color: 'primary',
        colors: [
          'primary',
          'blue',
          'success',
          'red',
          'teal',
        ],
        right: false,
        permanent: false,
        miniVariant: false,
        expandOnHover: false,
        background: false,
      }
    },
    methods: {

      selectRoute(route){ // eslint-disable-line no-unused-vars
        router.push(route).catch(err => err)
      },
      getUserInfo(){
        var jwtToken = this.getJwtAccessToken
        const USERINFO_URL = process.env.VUE_APP_COGNITO_APP_DOMAIN+ '/oauth2/userInfo';
        var requestData = {
            headers: {
                'Authorization': 'Bearer '+ jwtToken
            }
        }
        return axios.get(USERINFO_URL, requestData).then(response => { 
            return response.data;
        });
    }
    

    },
    computed: {
      ...mapGetters(["getLoggedIn", "getJwtAccessToken"]),

    },
    mounted(){
      if(this.getLoggedIn == true){
        console.log("WHAATT")
        this.menuItems.push( {title:'Logout', icon:'image-filter-hdr', route:'/' })
      }else{
        console.log("WHAATT")
        this.menuItems.push( {title:'Login', icon:'image-filter-hdr', route:'/register/' })
      }
    }
};
</script>
