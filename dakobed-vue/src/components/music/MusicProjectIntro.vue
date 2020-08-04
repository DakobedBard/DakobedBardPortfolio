<template>
    <v-container>

      <v-layout>
        <v-flex md2>
        <BaseNavBar v-bind:items=items />
        </v-flex>
        <v-flex md10>
          <v-card  tile flat>
            <v-card-title>Music Information Retrieval</v-card-title>
            <v-divider></v-divider>     
            <v-card-text>
              <Paragraph v-bind:title = introduct_title v-bind:text = introduction />
              <Paragraph v-bind:title = motivation_title v-bind:text = motivation />
              <Paragraph v-bind:title = methods_title v-bind:text = methods />
              <TechnologiesList v-bind:technologies=technologies />
            </v-card-text>
          </v-card>

          <GithubFooter v-bind:link = link v-bind:link_title = link_title />


        </v-flex>
      </v-layout> 
    </v-container>
    
</template>

<script>


import BaseNavBar from  '../BaseNavBar'
import GithubFooter from '../shared/GithubFooter'
import Paragraph from '../shared/Paragraph'
import TechnologiesList from '../shared/TechnologiesList'



export default {
  components:{
    BaseNavBar,
    GithubFooter,
    Paragraph,
    TechnologiesList
  },
  
  data () {
    return {
      link: '',
      link_title: 'Music Information Retrieval',
      introduct_title: 'Project Description',
      introduction:`In this project I attempt to perform automatic music transcription, the process of taking raw audio of a musician playing '\
                'and instrumentand outputting guitar tab or piano sheet music depending on the instrument.  This problem falls under the subfield' \
                of data science known as MIR (Music Information Retrieval). `,
      motivation_title:'Motivation',
      motivation: `As an musician I am frequently faced with wanting to know how a particular piece of music is played.  This often occurs
                  when I watch people perform covers of songs I want to learn on Youtube.  Woulden't it be great if I could a transcription
                  of what they are playing?`,
      methods_title: 'Methods',
      methods: `I attempt to reproduce the neural
                network archticture described by Manuel Minguez Carretero in his thesis. He proposes several neural network architectures for 
                solving this problem, which he trained on the MusicNet database, an MIR dataset of piano recordings and sheet music.  In this 
                project I instead train models using the GuitarSet & the Maestro datasets for performing guitar and piano transcription.  `,

      items: [
        { title: 'Project Description', icon: 'mdi-view-dashboard', route:'/musiclanding' },
        { title: 'GuitarSet', icon: 'mdi-image', route:'/guitarset' },
        { title: 'Transcriber', icon: 'mdi-help-box', route:'/transcriber' },
        { title: 'Transcriptions', route:'/transcriptions' }
      ],
      technologies: [
        "Keras deep learning library on AWS EC2 GPU instance",
        "AWS Serverless Application modle deploys Lambda functions & API Gateway",
        "Swagger to define the API & enable CORS",
        "AWS CloudFront to serve audio files from S3.  "
      ]

    }
  },
}
</script>