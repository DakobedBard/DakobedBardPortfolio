<template>
<v-container>
  <v-layout row>
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
         <!-- <Tweet v-bind:username="tweet.username" v-bind:content="tweet.content"/>  -->
        </div>


      </v-flex>
  </v-layout> 
  <v-layout>
    <v-flex>
      
    </v-flex>
  </v-layout>
    
</v-container>
</template>
<script>


import { mapGetters, mapActions } from "vuex";
// import Tweet from './Tweet'



export default {
  components:{
    // Tweet
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
      markers:[],
      latSelection:40,
      lngSelection:-98,
      zoomSelection:4
    }
  },


  computed: {
    ...mapGetters(["getPipelineSelection"]),
    ...mapGetters(["getTweets"]),

  },
  methods:{
    ...mapActions(["setPipelineSelection"]),
    ...mapActions(["fetchTweets"]),
    placeMarker(location) {
      this.marker = new window.google.maps.Marker({
        position: location, 
        map: this.map
      });
    },
    addListener(){

    }
  },
  mounted(){
    this.map = new window.google.maps.Map(this.$refs["map"],{
      center: {lat:this.latSelection, lng:this.lngSelection },
      zoom: this.zoomSelection,markers:[{ lat: -48, lng: 98 }]
    }),

    this.addEventListener()
    
    var marker = new window.google.maps.Marker({position: { lat: -48, lng: 98 }, map: this.map});
    console.log(marker)  
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
