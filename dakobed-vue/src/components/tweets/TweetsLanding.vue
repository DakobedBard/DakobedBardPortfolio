<template>
<v-container>

  <v-layout>
      <v-flex md2>
        <BaseNavBar v-bind:items=items />
      </v-flex>
      
      <v-flex md8>
        {{markers }}
        <v-card flat>
          <div id="map" ref="map"></div>
        </v-card>
      </v-flex>
    </v-layout>


  <!-- <v-layout row>
    <v-flex md7>
      <v-card tile flat >
        <v-card-text></v-card-text>
          <div id="map" ref="map">

          </div>
        </v-card>
      </v-flex>
      <v-flex md5>
        <v-card-text>What are people tweeting about at {{latSelection }}, {{ lngSelection }} ? </v-card-text>
        <div v-for="tweet of getTweets" v-bind:key="tweet.id">
         <Tweet v-bind:username="tweet.username" v-bind:content="tweet.content"/> 
        </div>
      </v-flex>
  </v-layout> 
  <v-layout>
    <v-flex>
      
    </v-flex>
  </v-layout>
     -->
</v-container>
</template>

<script>
/* eslint-disable */

import { mapGetters, mapActions } from "vuex";
import BaseNavBar from  '../BaseNavBar'
import Vue from 'vue'
// import Tweet from './Tweet'

// function   placeMarker(position, map) {
//   console.log(position)
//     var marker = new window.google.maps.Marker({
//         position: position, 
//         map: map
//     });
// }




export default {
  components:{
    BaseNavBar
  },
  props:{

  },

  created(){
    this.fetchTweets()
    
  },

  data(){
    return{
      map:null,
      marker:null,
      selection:1,
      
      latSelection:40,
      lngSelection:-98,
      zoomSelection:4,
        items: [
          { title: 'Tweets Project Description', icon: 'mdi-view-dashboard', route:'/tweetsintro' },
          { title: 'Tweets Map', icon: 'mdi-image', route:'/tweets' },
            {title: 'Tweets Landing',route:'/tweetslanding'}


        ],
      }
    
  },


  computed: {
    ...mapGetters(["getPipelineSelection"]),
    ...mapGetters(["getTweets"]),

  },
  methods:{
    ...mapActions(["setPipelineSelection"]),
    ...mapActions(["fetchTweets"]),
    placeMarker(e){
      console.log(e)
      var marker = new window.google.maps.Marker({ position: position, map: this.$map})
    }

  },


  mounted(){
    this.markers =[]
    this.$map = new window.google.maps.Map(document.getElementById('map'), {
       center: new window.google.maps.LatLng(this.latSelection, this.lngSelection),
       zoom: this.zoomSelection
     });
    // this.map = new window.google.maps.Map(this.$refs["map"],{
    //   center: {lat:this.latSelection, lng:this.lngSelection },
    //   zoom: this.zoomSelection,markers:[{ lat: -48, lng: 98 }]
    // }),

    this.$map.addListener('click', function(e) {
      console.log(e)
      placeMarker(e)
      // this.markers.push(

      //   new window.google.maps.Marker({
      //   position: position,
      //   map: map
      // })

      // )
    });

    function placeMarker(position){
      console.log("Dfdf")
      var marker = new window.google.maps.Marker({
        position: position,
        map: this.$map
      })
    }
    
    // var marker = new window.google.maps.Marker({position: { lat: -48, lng: 98 }, map: this.map});
    // console.log(marker)  
    // window.google.maps.event.addListener(this.map, 'click', function(event) {
    //   console.log(event)
      
      // console.log("The map got clicked " + Object.keys(event))
      // this.latSelection = event.latLng.lat()
      // this.lngSelection = event.latLng.lng()
      // console.log("The latlng is " + this.latSelection)
      // console.log("The latlng is " + this.lngSelection)

      // this.marker = new window.google.maps.Marker({
      //   position: { lat: lat, lng: long }, 
      //   map: this.map
      // })
      // var marker = new window.google.maps.Marker({position: { lat: this.latSelection, lng: this.lngSelection }, map: this.map});
      // console.log(marker)
    // });
    //   this.marker = new window.google.maps.Marker({
		// 			position: { lat: lat, lng: long },
		// 			map: this.map
		// })
     
  
  }
}
</script>
<style scoped>
  #map {
    height:600px;
    height: 720px;
    background:gray;
  }
</style>
