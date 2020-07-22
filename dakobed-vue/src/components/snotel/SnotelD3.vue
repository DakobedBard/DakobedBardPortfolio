<template>
  <v-container>
    <v-layout>
      <v-flex md2>
        <BaseNavBar v-bind:items=items />
      </v-flex>
          
      <v-flex md10>
        <v-card flat>
            <v-card-title>Snotel Data Viewer </v-card-title>
            <linechart v-bind:class="[toggleClass]" />
            
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>


<script>
/* eslint-disable */
// import * as d3 from 'd3'

import linechart from '../d3/linechart'

import BaseNavBar from '../BaseNavBar'

export default {
    components:{
        BaseNavBar,
        linechart
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
      }
    },



}
</script>