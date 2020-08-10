<template>
  <v-container>
    <v-layout row>
      <v-flex md2>
        <BaseNavBar v-bind:items=items />
      </v-flex>
      <v-flex md10>

      </v-flex>
    </v-layout>
  </v-container>
</template>


<script>

import BaseNavBar from '../BaseNavBar'
import Paragraph from '../shared/Paragraph'
import GithubFooter from '../shared/GithubFooter'



export default {
    components:{
        BaseNavBar
    },
    data(){
      return {

        introduction: `
        `,

        technologies:[
          "Spring Boot",
          "Spring Kafka Binder",
          "AWS RDS or DynamoDB (I've implemented both but don't want to pay for an RDS instance"
        ],
        items: [
          { title: 'Project Description', route:'/eventservices' },
          
        ],
      }
    }
    
}
</script>