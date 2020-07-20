<template>
  <v-container>
    <v-layout>
      <v-flex md2>
        <MusicNavBar />
      </v-flex>
      <v-flex  md10>
        <v-card flat>
          
          <v-card-title>
          Transcription Service
          </v-card-title>

          <UploadAudio />

        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>

import MusicNavBar from './MusicNavBar'
import UploadAudio from '../uploads/UploadAudio'


export default {
    
  components:{
    MusicNavBar,
    UploadAudio
  },

}
</script>