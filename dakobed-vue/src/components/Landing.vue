<template>
  <v-container>

      <v-layout row>
        <v-flex md6>
          <v-card  tile flat>
            <v-card-text>
            <p> I am a software/data/cloud engineer pursuing new oppertunities in the Seattle area and remotely.  As evidenced by the projects in my Portfolio
            and the many technologies which I have first hand experience with.  I have a passion for learning and challenging my self to learn new technologies.  
            My primary programming languages are Python & Java, but also have experience with others such as javascript & C++.  For the past several years I have 
            been becoming more and more proficient with AWS cloud computing, having made extensive use for this projects
            </p>

            <span>
                
            </span>


            </v-card-text>
          </v-card>
        </v-flex>
        <v-flex md6>
          <v-card  tile flat >
            <v-img :src="'https://s3-us-west-2.amazonaws.com/dalinar-mir.com/profile.jpg'" height="700px" width="560"></v-img>

          </v-card>
        </v-flex>
      </v-layout> 

    <v-layout>
      <v-flex>
          Mathias Portfolio



      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>

export default {
    data(){
      return {

      }
    },


}
</script>