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
        </v-card>
        </v-flex>
      </v-layout>
  </v-container>
</template>
<script>

import LandingNavBar from './LandingNavBar'
export default {
    components:{
        LandingNavBar
    }
    
}
</script>