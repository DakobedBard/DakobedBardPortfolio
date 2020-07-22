<template>
  <v-container>
    <v-layout>
      <v-flex md2>
        <BaseNavBar v-bind:items=items  />
      </v-flex>
          
      <v-flex md10>
        <v-card flat>
            <v-card-title>Snotel Data Viewer </v-card-title>
            <linechart v-bind:class="[toggleClass]" v-bind:data="data" />
            
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>


<script>
/* eslint-disable */
// import * as d3 from 'd3'

import Linechart from '../d3/Linechart'

import BaseNavBar from '../BaseNavBar'

export default {
    components:{
        BaseNavBar,
        Linechart
    },
  
    created(){
        console.log("Created the d3js component ")
    },

    mounted(){
        this.play()

    },


    methods:{
        play() {
            // toggle classes to animate the line draw
            this.toggleClass == "ani1"
            ? (this.toggleClass = "ani2")
            : (this.toggleClass = "ani1");
        },

    },
    data () {
        return {
            toggleClass: "ani1",
            loadData:{},
            items: [
                { title: 'Snotel Project Description', icon: 'mdi-view-dashboard', route:'/snotel' },
                { title: 'Snotel Data', icon: 'mdi-image', route:'/snoteldata' },
                {title: 'Snotel D3 Data Viewer ', route :'/snoteld3'}
            ],
            data: [
                {
                day: "01-11-2016",
                count: 80
                },
                {
                day: "02-12-2016",
                count: 250
                },
                {
                day: "03-13-2016",
                count: 150
                },
                {
                day: "04-14-2016",
                count: 496
                },
                {
                day: "05-15-2016",
                count: 140
                },
                {
                day: "06-16-2016",
                count: 380
                },
                {
                day: "07-17-2016",
                count: 140
                },
                {
                day: "08-17-2016",
                count: 240
                },
                {
                day: "09-18-2016",
                count: 100
                },
                {
                day: "10-18-2016",
                count: 260
                },
                {
                day: "11-18-2016",
                count: 100
                },
                {
                day: "12-18-2016",
                count: 150
                }
            ],
      }
    },



}
</script>