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

import { mapGetters, mapActions } from "vuex";
import router from './router'


export default {
  name: 'App',

  components: {
    
  },
  data(){
    return {
        drawer: false,

        menuItems:[

        {title:'Tweets', icon:'image-filter-hdr', route:'/tweets/' }, 
        {title:'Tabs', icon:'image-filter-hdr', route:'/tabs/' }, 

        {title:'Transcriptions', icon:'image-filter-hdr', route:'/transcriptions/' }, 
        {title:'Maestro', icon:'image-filter-hdr', route:'/maestro/' }, 

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
      ...mapActions(["setSelection"]),
      selectRoute(route){ // eslint-disable-line no-unused-vars
        this.setSelection("landing")
        router.push(route).catch(err => err)
      }

    },
    computed: {
    ...mapGetters(["allReports"]),
    ...mapGetters(["reportSelection"]),
    // mixins:[tripsMixin]
    }
};
</script>
