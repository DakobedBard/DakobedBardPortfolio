<template>
    <v-layout>
        <v-flex md1>
            <v-img :src="'https://dakobed.s3-us-west-1.amazonaws.com/github.png'" height="60px" width="60"></v-img>
        </v-flex>
        <v-flex md8>
            <div class="title font-weight-medium">
                Github Link: 
                <a href="https://github.com/MathiasDarr/DakobedBard/tree/master/dakobed-pipelines/dakobed-snotel">{{ link_title}}</a> 
            </div>

        </v-flex>
    </v-layout>
</template>


<script>
export default {
    props:{
        link: String,
        link_title:String
    }
}
</script>