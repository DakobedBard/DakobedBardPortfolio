<template>
  <v-container>
    <v-layout row>
      <v-flex md2>
        <BaseNavBar v-bind:items=items />
      </v-flex>
      
      <v-flex md10>
        <v-card flat>
            <v-card  tile flat>
            
            <v-card-title>Snotel Data Explorer </v-card-title>
            
            <v-divider></v-divider>     
            
            <v-card-text>
            </v-card-text>
          
          </v-card>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>

import BaseNavBar from  '../BaseNavBar'


export default {

    components:{
        BaseNavBar
        },

    data () {
      return {

        items: [
          { title: 'Snotel Project Description', icon: 'mdi-view-dashboard', route:'/snotel' },
          { title: 'Snotel Data', icon: 'mdi-image', route:'/snoteldata' },
        ],

      }
    },
}
</script>