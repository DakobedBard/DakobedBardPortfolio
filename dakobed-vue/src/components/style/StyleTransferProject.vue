<template>
  <v-container>
    <v-layout row>
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
        return{
            items:[
              { title: 'Project Description', route:'/style'},
              { title: 'Style Transfer', route:'/styletransfer'}
            ]
        }
    }
}
</script>