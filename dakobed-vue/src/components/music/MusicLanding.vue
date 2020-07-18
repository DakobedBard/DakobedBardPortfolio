<template>
    <v-container>

      <v-layout row>
        <v-flex md6>
          <v-card  tile flat>
            
            <v-card-title>Music Information Retrieval</v-card-title>
            <v-divider></v-divider>     
            <v-card-text>
            
            <h4>Project Discription</h4>
            <p>

                In this project I attempt to perform automatic music transcription, the process of taking raw audio of a musician playing
                and instrumentand outputting guitar tab or piano sheet music depending on the instrument.  This problem falls under the subfield
                of data science known as MIR (Music Information Retrieval).  
              </p>
              <h4> Motivation </h4>
                <p>
                  As an musician I am frequently faced with wanting to know how a particular piece of music is played.  This often occurs
                  when I watch people perform covers of songs I want to learn on Youtube.  Woulden't it be great if I could a transcription
                  of what they are playing?
                </p>
                
                <h4> Methods</h4>
                <p>
                
                I attempt to reproduce the neural
                network archticture described by Manuel Minguez Carretero in his thesis. He proposes several neural network architectures for 
                solving this problem, which he trained on the MusicNet database, an MIR dataset of piano recordings and sheet music.  In this 
                project I instead train models using the GuitarSet & the Maestro datasets for performing guitar and piano transcription.  

            </p>
            
       
            <p> 
            </p>

            <span>

            </span>
            Technologies Used
            <ul>
              <li>
                Keras deep learning library on GPU AWS instance
              </li>
              <li>
                AWS Lamda & API Gateway serverless API endpoints for deployment of the Keras model 
              </li>
            </ul>


            </v-card-text>
          </v-card>
        </v-flex>
        <v-flex md6>
          <v-card  tile flat >


          </v-card>
        </v-flex>
      </v-layout> 

    <v-layout>
      <v-flex>

      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
    
}
</script>