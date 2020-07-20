<template>
  <v-container>
    <v-layout>
      <v-flex md2>
        <MusicNavBar />
      </v-flex>
      <v-flex offset-xs1 md9>
        <v-card flat>

          <v-card-title>
            Maestro Transcription Training Examples Results
          </v-card-title>

        <v-data-table
          v-model="selected"  
          :headers="headers"
          :items="getMaestroTraningData" >

        <template v-slot:item="{ item }">
            <tr @click="rowClicked(item.fileID)">
                <td>{{item.title}}</td>
                <td>{{item.composer}}</td>
            </tr>

        </template>
      </v-data-table>

        </v-card>
      </v-flex>
    </v-layout>
  </v-container>

<!-- 
    <div class="text-center">

      <v-card>

        <v-card-title>
            Maestro Transcription Training Examples
            {{ getMaestroTraningData.length }}
         </v-card-title>
      </v-card>
      
    <v-data-table
        v-model="selected"  
        :headers="headers"
        :items="getMaestroTraningData"
      > 
      <template v-slot:item="{ item }">
            <tr @click="rowClicked(item.fileID)">
                <td>{{item.title}}</td>
                <td>{{item.composer}}</td>
            </tr>
        </template>
      </v-data-table>


    </div> -->
</template>

<script>

import { mapGetters, mapActions } from "vuex";
import router from '../../../router'
import MusicNavBar from '../MusicNavBar'
export default {
    components:{
      MusicNavBar
    },
    created(){
      this.fetchMaestroTrainingData()
      
    //   axios.get("http://localhost:8081/maestro").then((response) => {

    //     var response_string = JSON.stringify(response.data)
    //     var data = JSON.parse(response_string)
    //     this.data = data

    //   }, (error) => {
    //     console.log(error);
    //   });
    },

    mounted() {
    },
    
    computed:{
      ...mapGetters(["getMaestroTraningData"])
    },

    methods:{
      ...mapActions(["fetchMaestroTrainingData"]),     
      rowClicked(fileID){
        router.push({ name: 'piano-transcription', params: { fileID: fileID } })
      },
      ...mapActions(["fetchTrainingData"]),    

  },
  props:{

  },

  data(){
    return {
      selected:[],
      trainingData: [],

      page: 1,
      
      headers: [
        {
          text: 'Training Example',
          align: 'start',
          sortable: false,
          value: 'title',
        },


      ],
    }
  }


  
}
</script>