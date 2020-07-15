<template>
<v-container fluid="">
  <v-layout>
      <v-flex>
          <v-card dark>
              {{username}}
              
              
              {{content}}
          </v-card>
      </v-flex>
  </v-layout>
</v-container>
    
</template>

<script>
export default {
    
     props:{
      username: String,
      content: String
  },


}
</script>