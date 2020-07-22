<template>
  <v-container>
    <v-layout>
      <v-flex md2>
        <BaseNavBar v-bind:items=items />
      </v-flex>
          
      <v-flex md10>
        <v-card flat>
            <v-card-title>Snotel Data Viewer </v-card-title>
            <div id="my_dataviz"></div>


        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>


<script>

import * as d3 from 'd3'
import BaseNavBar from '../BaseNavBar'

export default {
  components:{
        BaseNavBar
  },
  created(){
      console.log("Created the d3js component ")
  },
  methods:{
      async fetchData(){
          let data = await d3.json("./tweets.json")
          this.loadData = data
      }
  },
  data () {
      return {
          loadData:{},
          items: [
            { title: 'Snotel Project Description', icon: 'mdi-view-dashboard', route:'/snotel' },
            { title: 'Snotel Data', icon: 'mdi-image', route:'/snoteldata' },
            {title: 'Snotel D3 Data Viewer ', route :'/snoteld3'}
          ],

      }
    },

    mounted(){

        // // set the dimensions and margins of the graph
        // var margin = {top: 10, right: 30, bottom: 30, left: 60},
        //     width = 460 - margin.left - margin.right,
        //     height = 400 - margin.top - margin.bottom;

        // // append the svg object to the body of the page
        // var svg = d3.select("#my_dataviz")
        // .append("svg")
        //     .attr("width", width + margin.left + margin.right)
        //     .attr("height", height + margin.top + margin.bottom)
        // .append("g")
        //     .attr("transform",
        //         "translate(" + margin.left + "," + margin.top + ")");

    }


}
</script>