<template>
  <v-container>
    <v-layout>
      <v-flex md2>
          <BaseNavBar v-bind:items=items />

      </v-flex>
      <v-flex  md10>
        <v-card flat >
          <v-container>
            <v-layout>
              <v-flex md6>
                <v-card flat>
                  <v-card-title>
                    Transcriptions
                  </v-card-title>
                </v-card>
                


              </v-flex>
              <v-flex md6>
                <v-btn color="primary" @click="login()">Login </v-btn>
              </v-flex>
            </v-layout>
          </v-container>

        </v-card>
        <v-card flat> 
          <v-card-text>
            <div v-if="email != false">
              
              Welcome {{email}}
            </div>
            <div v-else>
              Sign in to view and create transcriptions 
            </div>
          </v-card-text>
        </v-card>


        <!-- <v-card flat>
          
          <v-card-title>
          Transcription Service
          </v-card-title>

          <UploadFile />

        </v-card> -->
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
/* eslint-disable */

import BaseNavBar from  '../BaseNavBar'
import UploadFile from '../uploads/UploadFile'
import { mapGetters, mapActions } from "vuex";
import router from '../../router'

export default {
  methods:{
    login(){
      router.push({ name: 'register'})
    }
  },

  created(){
    console.log("The email ooutside the if is " + this.getEmail)
    if(this.getEmail != false){
      console.log("The email is " + this.getEmail)
          var email = this.getEmail
          var parsed_email = email.split('@')[0]
          console.log(parsed_email)
          this.email=parsed_email
    }else{
      this.email = false
    }


  },
  computed:{
    ...mapGetters(["getEmail"]),
  },


  components:{
    BaseNavBar,
    UploadFile
  },
  data(){

        return {
            items: [
              { title: 'Project Description', icon: 'mdi-view-dashboard', route:'/musiclanding' },
              { title: 'GuitarSet', icon: 'mdi-image', route:'/guitarset' },
              { title: 'Maestro', icon: 'mdi-help-box', route:'/maestro' },
              { title: 'Transcriber', icon: 'mdi-help-box', route:'/transcriber' },

          ],
        }
    }
}
</script>