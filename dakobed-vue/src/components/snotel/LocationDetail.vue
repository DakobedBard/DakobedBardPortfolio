<template>
  <v-container>
    <v-layout>
    
        
    
      <v-flex md2>
        <BaseNavBar v-bind:items=items  />
      </v-flex>
    
      <v-flex md10>
          <v-card flat>
            <v-card-title>
                Snotel Data Explorer for {{ location }}
            </v-card-title>
          </v-card>

        <v-layout row>
            <v-flex offset-1 md2>
                <DatePicker @clicked="onClickChild" v-bind:start=true v-bind:label="start_date" v-bind:fromDateVal="start_date_init"/>
            </v-flex>

            <v-flex offset-2 md2>
                <DatePicker @clicked="onClickChild" v-bind:start=false  v-bind:label="end_date" v-bind:fromDateVal="end_date_init" />
            </v-flex>

            <v-flex offset-2 md2>
                <v-btn color="primary" @click="queryData()">
                    Query Data
                </v-btn>
            </v-flex>
        </v-layout>



    
        <v-divider></v-divider>


        <!-- Reducxed median data {{getReducedSnowMedian.slice(0,2) }} -->

        <!-- first 2 elmeents of data {{ getReducedSnowCurrent.slice(0,2) }}
 -->

        <!-- <v-divider></v-divider>
        Reduced data {{getReducedSnowCurrent.slice(0,2) }} -->

        <!-- first 2 elmeents of data {{ getReducedSnowMedian.slice(0,2) }} -->

        <div v-if="getReducedSnowCurrent.length > 0 ">
            <v-card flat>
                <v-card-title>
                    Snowpack at {{ location }} from {{ sdate }} to {{ edate }}

                </v-card-title>
                <linechart v-bind:class="[toggleClass]" v-bind:data="getReducedSnowCurrent" />
            </v-card>            
        </div>




        <div v-if="getReducedSnowMedian.length > 0">
            <v-card flat>
                <v-card-title>
                    Median Snowpack at {{ location }} 
                </v-card-title>
                <linechart v-bind:class="[toggleClass]" v-bind:data="getReducedSnowMedian" />
            </v-card>            
        </div>
        

      </v-flex>
    </v-layout>
  </v-container>
</template>


<script>
/* eslint-disable */
// import * as d3 from 'd3'

import Linechart from './Linechart'
import BaseNavBar from '../BaseNavBar'
import DatePicker from '../shared/DatePicker'
import { mapGetters, mapActions } from "vuex";
export default {
    components:{
        BaseNavBar,
        Linechart,
        DatePicker
    },
  
    created(){
        this.location = this.$route.params.id
    },

    mounted(){
        this.play()

    },


    methods:{

        ...mapActions(["querySnotelData", "reset_arrays"]),
        onClickChild (date_value, start) {

            if(start){
                this.sdate = date_value
            }else{
                this.edate = date_value
            }
        },
        queryData(){
            this.reset_arrays()
            var query = {location:this.location, sdate: this.sdate, edate: this.edate}
            this.querySnotelData(query)
        },


        play() {
            // toggle classes to animate the line draw
            this.toggleClass == "ani1"
            ? (this.toggleClass = "ani2")
            : (this.toggleClass = "ani1");
        },

        parseQueryData(){

        }

    },

    computed:{
        ...mapGetters(["getReducedSnowCurrent", "getReducedSnowMedian"])
        // ...mapGetters(["getWaterMedian", "getWaterCurrent","getSnowCurrent", "getSnowMedian", "getReducedSnowCurrent" ])
    },
    data () {
        return {

            toggleClass: "ani1",
            loadData:{},
            items: [
                { title: 'Snotel Project Description', icon: 'mdi-view-dashboard', route:'/snotel' },
                { title: 'Snotel Data', icon: 'mdi-image', route:'/snoteldata' },
            ],
            sdate: '20140101',
            edate: '20150101',


            start_date:'Start Date',
            end_date: 'End Date',
            start_date_init: "2014-01-01",
            end_date_init: "2015-01-01",




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