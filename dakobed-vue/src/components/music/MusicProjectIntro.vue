<template>
    <v-container>

      <v-layout>
        <v-flex md2>
        <MusicNavBar />
        </v-flex>
        <v-flex md10>
          <v-card  tile flat>
            
            <v-card-title>Music Information Retrieval</v-card-title>
            <v-divider></v-divider>     
            <v-card-text>
            
            <h3>Project Discription</h3>
            <p>
                In this project I attempt to perform automatic music transcription, the process of taking raw audio of a musician playing
                and instrumentand outputting guitar tab or piano sheet music depending on the instrument.  This problem falls under the subfield
                of data science known as MIR (Music Information Retrieval).  
              </p>
              <h3> Motivation </h3>
                <p>
                  As an musician I am frequently faced with wanting to know how a particular piece of music is played.  This often occurs
                  when I watch people perform covers of songs I want to learn on Youtube.  Woulden't it be great if I could a transcription
                  of what they are playing?
                </p>
                
                <h3> Methods</h3>
                <p>
                I attempt to reproduce the neural
                network archticture described by Manuel Minguez Carretero in his thesis. He proposes several neural network architectures for 
                solving this problem, which he trained on the MusicNet database, an MIR dataset of piano recordings and sheet music.  In this 
                project I instead train models using the GuitarSet & the Maestro datasets for performing guitar and piano transcription.  
            </p>

            <h3> Technologies Used </h3>
            <ul>
              <li>
                Keras deep learning library on AWS EC2 GPU instance
              </li>
              <li>
                AWS Lamda & API Gateway serverless API endpoints for deployment of the Keras model 
              </li>
            </ul>
            <v-divider></v-divider>
            <v-layout>
                <v-flex md1>
                    <v-img :src="'https://dakobed.s3-us-west-1.amazonaws.com/github.png'" height="60px" width="60"></v-img>
                </v-flex>
                <v-flex md8>
                    Github Links

                    <ul>
                      <li>
                         <a href="https://www.w3schools.com">Music Information Retrieval</a> 
                      </li>
        
                    </ul>
                </v-flex>
            </v-layout>



            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout> 
    </v-container>
    
</template>

<script>


import MusicNavBar from './MusicNavBar'


export default {
  components:{
    MusicNavBar
  },
}
</script>