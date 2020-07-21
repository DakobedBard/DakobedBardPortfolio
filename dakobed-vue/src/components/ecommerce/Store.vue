<template>
  <v-container>
    <v-layout>
      <v-flex md2>
        <BaseNavBar v-bind:items=items />

      </v-flex>
    </v-layout>
  </v-container>
    
</template>
<script>

import BaseNavBar from '../BaseNavBar'

export default {
    components:{
        BaseNavBar
    },
    data(){

        return {
            items: [
                { title: 'Events Driven Microservices Project Description', icon: 'mdi-view-dashboard', route:'/ecommerce' },
                { title: 'Ecommerce Store', icon: 'mdi-image', route:'/storefront' },

          ],
        }
    }
}
</script>