<template>
  <v-container>
    <v-layout row>
        <v-flex md8>
          <v-card  tile flat>
            <v-card-text>

            <v-card-title>
                Mathias Darr
            
            </v-card-title>
            <v-card-subtitle>
                Fullstack Software, Data & Cloud Engineer
            </v-card-subtitle>
            <v-divider></v-divider>
            </v-card-text>
          </v-card>
        </v-flex>

        <v-flex md4>
          <v-card  tile flat >
            <v-img :src="'https://s3-us-west-2.amazonaws.com/dalinar-mir.com/profile.jpg'" height="700px" width="560"></v-img>
          </v-card>
        </v-flex>
      </v-layout>
</v-container>

</template>
<script>
export default {
    
}
</script>