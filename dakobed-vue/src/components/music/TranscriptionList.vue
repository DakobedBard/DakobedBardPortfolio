<template>
  <v-container>
    <v-layout>
        <v-flex md 8>
        <v-card flat class="pa-3" v-for="transcription in getUsersTranscriptions" :key="transcription.id" >
          <v-container dark>
            <v-layout row>
              <v-flex xs7 sm8 md9>
                <v-card-title>
                    <div>
                    <v-flex >
                            <p class="font-weight-light grey--text"> {{transcription.title}}</p>
                        </v-flex>
                        <div> 
                          <!-- <v-btn text small  > Read More </v-btn> -->
                           <v-btn text small v-on:click="selectTranscription(transcription.id)" > View Transcription </v-btn>
                        </div>
                    </div>
                </v-card-title>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card> 

        </v-flex>
    </v-layout>
  </v-container>
</template>


<script>
/* eslint-disable */
import { mapGetters, mapActions } from "vuex";
import router from '../../router'
export default {

    methods:{
        ...mapActions(["fetchUsersTranscriptions"]),
        selectTranscription(id){
            router.push('/')
        },
    },

    props:{
        email: String
    },
    computed:{
    ...mapGetters(["getUsersTranscriptions"]),
    }
}
</script>