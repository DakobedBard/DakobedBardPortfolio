<template>
  <v-container>
    <v-layout row>
      <v-flex md2>

      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import BaseNavBar from '../BaseNavBar'
export default {
    data(){
        return{
            items:[{ title: 'Project Description', route:'/style' }]
        }
    }
}
</script>