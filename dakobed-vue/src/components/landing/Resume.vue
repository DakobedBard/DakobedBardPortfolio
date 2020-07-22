<template>
  <v-container>
      <v-layout row>
        <v-flex md2>
            <LandingNavBar />
        </v-flex>

        <v-flex md10>
        <v-card flat>
            <v-card-title>
                Resume

            </v-card-title>
            <a href="https://dakobed.s3-us-west-1.amazonaws.com/Resume.pdf">Resume PDF</a>

        </v-card>
        </v-flex>
      </v-layout>
  </v-container>
</template>

<script>

import LandingNavBar from './LandingNavBar'
// import pdf from 'vue-pdf'

export default {
    components:{
        LandingNavBar,
        // pdf
    }
    
}
</script>