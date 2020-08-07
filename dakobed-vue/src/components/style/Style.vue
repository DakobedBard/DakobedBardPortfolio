<template>
  <v-container>
    <v-layout row>
      <v-flex md2>
        <BaseNavBar v-bind:items=menu_items />
      </v-flex>
      <v-flex md10>
    
        <v-layout row>
          <v-card flat>    
            <v-card-title>
              Style Transfer
            </v-card-title>
            <v-card-text>  
              <Paragraph v-bind:title = "''" v-bind:text = description />
            </v-card-text>
          </v-card>
        </v-layout>

        <v-container fluid>
          <v-layout row>
            <v-flex md4>
              <v-card tile flat >
             <v-card-text>Glacier Peak Base Image</v-card-text>
            <v-img :src="items[1].src" height="300px" width="460"></v-img>
          </v-card>
        </v-flex>
        <v-flex md4>
          <v-card  tile flat>
            <v-card-text>Monet Style Image</v-card-text>
            <v-img :src="items[0].src" height="300px" width="460"></v-img>
          </v-card>
        </v-flex>
        <v-flex md4>
          <v-card  tile flat>
            <v-card-text>Style Transfer Result</v-card-text>
            <v-img :src="items[2].src" height="300px" width="460"></v-img>
          </v-card>
        </v-flex>

      </v-layout>

            <v-layout row>
        <v-flex md4>
          <v-card tile flat >
            <v-card-text>Mount Baker Base Image</v-card-text>
            <v-img :src="items[3].src" height="300px" width="460"></v-img>
          </v-card>
        </v-flex>
        <v-flex md4>
          <v-card  tile flat>
            <v-card-text>Monet Style Image</v-card-text>
            <v-img :src="items[4].src" height="300px" width="460"></v-img>
          </v-card>
        </v-flex>
        <v-flex md4>
          <v-card  tile flat>
            <v-card-text>Style Transfer Result</v-card-text>
            <v-img :src="items[5].src" height="300px" width="460"></v-img>
          </v-card>
        </v-flex>

          </v-layout>
          <v-layout row>
            <TechnologiesList v-bind:technologies=technologies />
          </v-layout>
          <v-divider></v-divider>
          <v-layout row>
            <GithubFooter v-bind:link = link v-bind:link_title = link_title />
          </v-layout>
        </v-container>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
/* eslint-disable */

import BaseNavBar from '../BaseNavBar'
import Paragraph from '../shared/Paragraph'
import TechnologiesList from '../shared/TechnologiesList'
import GithubFooter from '../shared/GithubFooter'

export default {
    components:{
      BaseNavBar,
      Paragraph,
      TechnologiesList,
      GithubFooter
    },
    data(){
        return{
          project_title: 'Style Transfer',
          description: `I played around with style transfer.  I used the Keras library & a prebuilt model on an EC2 instance`,
          technologies: [
            "Keras",
            "EC2 GPU Instance"
          ],
          link: 'https://github.com/MathiasDarr/DakobedBard/tree/master/dakobed-style-transfer',
          link_title: 'Style Transfer Project',

          items:[
            {id:1, src:'https://dakobed-style.s3-us-west-2.amazonaws.com/sunrise.jpg'}, 
            {id:2, src:'https://dakobed-style.s3-us-west-2.amazonaws.com/style_dir/gp_base.jpg'},
            {id:3, src: 'https://dakobed-style.s3-us-west-2.amazonaws.com/result.png'},

            {id:4, src:'https://dakobed-style.s3-us-west-2.amazonaws.com/baker_base.jpg'}, 
            {id:5, src:'https://dakobed-style.s3-us-west-2.amazonaws.com/monet_style.jpg'},
            {id:6, src: 'https://dakobed-style.s3-us-west-2.amazonaws.com/_at_iteration_9.png'}
            ],  
          menu_items:[
            { title: 'Style Transfer', route:'/style'}
          ]
        }
    }
}
</script>