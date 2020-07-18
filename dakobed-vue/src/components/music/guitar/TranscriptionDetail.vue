<template>
  <div>
      Transcription Detail {{fileID}}

    <!-- <audio id="audio" controls>
      <source  id="audioSource" src="" type="audio/wav">
    </audio> -->
      <v-card flat class="pa-3" v-for="line in getLines" :key="line.id" >
        <TabLine  v-bind:notes="line.notes"/>
  
      </v-card>

  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import TabLine from './TabLine'


export default {
  created(){
    this.fileID = this.$route.params.fileID
    this.getS3Transcription(this.fileID)
  },
  
  methods:{
    ...mapActions(["fetchTranscription"]),
    ...mapActions(["getS3Transcription"]),

  },


  props:{
      // fileID:Number
  },

  data(){
    return {
        audioURL:"http://d3rak0tzwsp682.cloudfront.net/fileID3/3audio.wav",
        transcriptionurl:"http://d3rak0tzwsp682.cloudfront.net/fileID" + this.fileID + "/transcription.json"
    }
  },
  computed: {
    ...mapGetters(["getNotes"]),
    ...mapGetters(["getLines"])

  },
  components:{
    TabLine
  },
  mounted(){

    // var audio = document.getElementById('audio');

    // var source = document.getElementById('audioSource');
    // source.src = "http://d3rak0tzwsp682.cloudfront.net/fileID" + this.fileID + "/audio.wav"

    // audio.load(); //call this to just preload the audio without playing
    // audio.play(); //call this to play the song right away
  }
  
}
</script>

