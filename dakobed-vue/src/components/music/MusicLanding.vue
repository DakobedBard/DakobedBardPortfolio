<template>
    <v-container>

      <v-layout>
        <v-flex md2>

        <MusicNavBar />
        </v-flex>
        <v-flex  offset-xs2>
          <MusicProjectIntro />
        </v-flex>
      </v-layout> 
  
  </v-container>
</template>

<script>

import MusicProjectIntro from './MusicProjectIntro'

import MusicNavBar from './MusicNavBar'

export default {
  components:{
    MusicProjectIntro,
    MusicNavBar
  },
  data () {
      return {
        drawer: true,
        items: [
          { title: 'Project Description', icon: 'mdi-view-dashboard' },
          { title: 'GuitarSet', icon: 'mdi-image' },
          { title: 'Maestro', icon: 'mdi-help-box' },
        ],

      }
    },
  }
</script>