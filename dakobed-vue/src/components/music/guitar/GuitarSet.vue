<template>
  <v-container>
  
    <v-layout>
      <v-flex md2>
        <BaseNavBar v-bind:items=items />
      </v-flex>
    <v-flex md10>

      <v-card flat>
        <v-layout >
        <!-- <v-card-title>
            GuitarSet Transcription Training Examples
        </v-card-title> -->
        <v-card>  
          
          <v-flex >
            GuitarSet Transcription Training Examples
          </v-flex>
          <v-flex md 4>
            <v-btn color="primary"> Login </v-btn>
          </v-flex>
          </v-card>
        </v-layout>
        
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
import BaseNavBar from  '../../BaseNavBar'



export default {
    created(){
      this.fetchGuitarsetData()
    },
    
    components:{
      BaseNavBar
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
        

        items: [
              { title: 'Project Description', icon: 'mdi-view-dashboard', route:'/musiclanding' },
              { title: 'GuitarSet', icon: 'mdi-image', route:'/guitarset' },
              { title: 'Maestro', icon: 'mdi-help-box', route:'/maestro' },
              { title: 'Transcriber', icon: 'mdi-help-box', route:'/transcriber' },

          ],

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