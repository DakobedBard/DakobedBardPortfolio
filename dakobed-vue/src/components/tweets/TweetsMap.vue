<template>
<v-container>

  <v-layout>
      <v-flex md2>
        <BaseNavBar v-bind:items=items />
      </v-flex>
      
      <v-flex md8>
        <v-card flat>
          <v-btn @click="clickME()">CLICK ME </v-btn>
          <GmapMap
                ref="mapRef"
                :center="{lat:latSelection, lng:lngSelection}"
                :zoom="4"


                style="width: 800px; height: 600px"
            >
            <GmapMarker
                :key="index"
                v-for="(m, index) in markers"
                :position="m.position"
                :clickable="true"
                :draggable="true"
                @click="center=m.position"
            />
            </GmapMap>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>    
</template>
<script>

import BaseNavBar from  '../BaseNavBar'
export default {
 components:{
    BaseNavBar
  },
  methods:{
    clickME(){
        this.markers.push({position:{lat: 40, lng: -98}})
    },
    placeMarker(event){
        console.log("The event occurs at " + event)
    },
    somefunc(event){console.log("DFDF" + event)}

  },
  data(){
    return{
      map:null,
      marker:null,
      selection:1,
      markers:[{position:{lat: 30, lng: -95}}],
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
  mounted(){
    this.$refs.mapRef.$on('click', this.somefunc())
  }

}
</script>