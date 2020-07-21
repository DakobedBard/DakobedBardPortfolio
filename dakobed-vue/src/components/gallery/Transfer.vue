<template>
  <v-container>
    <v-layout row>
      <v-flex md2>

        <StyleTransferNavBar />
      
      </v-flex>
      <v-flex md10>
      </v-flex>
    </v-layout>
  </v-container>
    
</template>

<script>

import StyleTransferNavBar from './StyleTransferNavBar'

export default {
    
    components:{
        StyleTransferNavBar
    }
}
</script>