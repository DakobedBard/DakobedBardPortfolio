<template>
  <v-container>
  
    <v-layout>
      <v-flex md2>
        <MusicNavBar />
      </v-flex>
    <v-flex offset-xs1 md8>


      <v-card flat>
        <v-card-title>
            GuitarSet Transcription Training Examples
        </v-card-title>
        <v-data-table
          v-model="selected"  
          :headers="headers"
          :items="getGuitarsetData" > 

        <template v-slot:item="{ item }">
            <tr @click="rowClicked(item.fileID)">
                <td>{{item.title}}</td>
            </tr>
        </template>
        </v-data-table>
      </v-card>
 
    <router-view></router-view>
    
    </v-flex>
    </v-layout>
  </v-container>
</template>

<script>

import { mapGetters, mapActions } from "vuex";
import router from '../../../router'
import MusicNavBar from '../MusicNavBar'


export default {
    created(){
      this.fetchGuitarsetData()
    },
    
    components:{
      MusicNavBar
    },

    mounted() {

    },
    
    computed:{
      ...mapGetters(["getGuitarsetData"])
    },

    methods:{
      // ...mapActions(["getS3Transcription"]),     
      rowClicked(fileID){
        router.push({ name: 'transcription_detail', params: { fileID: fileID } })
      },
      ...mapActions(["fetchGuitarsetData"]),    

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