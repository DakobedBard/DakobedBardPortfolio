<template>
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


    </div>
</template>

<script>

import { mapGetters, mapActions } from "vuex";
import router from '../../../router'

export default {
    
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
    components:{
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