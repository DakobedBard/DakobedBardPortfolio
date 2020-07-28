<template>
<div>
  <v-container>
    <v-layout>
      <v-flex>
        <v-card flat class="pa-3" v-for="report in allReports" :key="report.id" >
          <v-container dark>
            <v-layout row>
              <v-flex xs5 sm4 md3>
                <v-img class="white--text align-end" height="200px" v-bind:src="report.imageURL">
                </v-img>                
              </v-flex>
              <v-flex xs7 sm8 md9>
                <v-card-title>
                    <div>
                        <h4 class = "white00text mb-0 text-left" > {{report.name}}
                        <div class="text-left grey--text "> {{ report.region }}</div> </h4>
                        <v-flex >
                            <div class="caption grey--text">Posted on {{report.date}}</div>
                        </v-flex>

                        <v-flex >
                            <p class="font-weight-light grey--text"> {{report.report}}</p>
                        </v-flex>
                        <div> 
                          <!-- <v-btn text small  > Read More </v-btn> -->
                           <v-btn text small v-on:click="selectReport(report.id)" > Read More </v-btn>
                        </div>
                    </div>
                </v-card-title>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card> 
      </v-flex>
    </v-layout>

    <v-btn @click="onPostReport()">Post Trip Report</v-btn>
  </v-container>

  
  </div>
</template>

<script>

import { mapGetters, mapActions } from "vuex";

export default {
    created(){
        // this.getReports()
        this.fetchReports();
    },
    
    data(){
        return {
            reportID:-1,
            reports: []
        }
    },
    methods:{
      ...mapActions(["fetchReports"]),
      ...mapActions(["setSelection"]),

      selectReport(id){
        console.log("whata")
        this.reportID = id
        this.setSelection(id)
        // this.$emit('select-report', this.reportID)
      },
      onPostReport(){
        this.setSelection("post")
      }
    },
    computed: {
    ...mapGetters(["allReports"]),
    ...mapGetters(["reportSelection"]),
    }
}
</script>