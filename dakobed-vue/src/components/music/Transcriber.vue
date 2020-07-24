<template>
  <v-container>
    <v-layout>
      <v-flex md2>
          <BaseNavBar v-bind:items=items />

      </v-flex>
      <v-flex  md10>
        <v-card flat>
          
          <v-card-title>
          Transcription Service
          </v-card-title>

          <UploadFile />

        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
/* eslint-disable */

import BaseNavBar from  '../BaseNavBar'
import UploadFile from '../uploads/UploadFile'


export default {
    
  components:{
    BaseNavBar,
    UploadFile
  },
  data(){

        return {
            items: [
              { title: 'Project Description', icon: 'mdi-view-dashboard', route:'/musiclanding' },
              { title: 'GuitarSet', icon: 'mdi-image', route:'/guitarset' },
              { title: 'Maestro', icon: 'mdi-help-box', route:'/maestro' },
              { title: 'Transcriber', icon: 'mdi-help-box', route:'/transcriber' },

          ],
        }
    }
}
</script>