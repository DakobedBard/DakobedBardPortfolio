<template>
  <div>

            <!-- <v-flex xs2 md3 offset-sm1 v-for="item in items" v-bind:key=item.src>
         
    
              <v-card >
                  <v-img :src="item.src" height="200px" width="100"></v-img>
                  what
              </v-card>
              
          </v-flex>
    <v-container fluid>
     <v-layout row>
        <v-flex md9>



          <v-flex xs12 md6 v-for="image in items" v-bind:key=image.id>
            <v-card >
              <v-img :src="image.src" height="400px" width="500"></v-img>
            </v-card>
          </v-flex>
          
          {{}} -->
          <!-- <div v-if="gallerySelection === 'gallery'">
            <Gallery />
          </div>
          <div v-if="gallerySelection === 'style'">
            <StyleTransfer />
          </div>
          <div v-if="gallerySelection === 'upload'">
            <UploadImage />
          </div>
          <div v-if="gallerySelection === 'landscapes'">
            <LandScapes />
          </div>
           -->
        <!-- </v-flex>
        <v-flex md3>

        <v-card flat class="mx-auto" max-width="400">
          <v-list :flat="flat"> <v-list-item-group  v-model="model" :multiple="multiple" :mandatory="mandatory "
            color="grey">
            <v-list-item v-for="item in menuItems" :key="item.title"  @click="selectMenuItem(item.selection)">
              <v-list-item-icon>
                <v-icon v-text="item.title"></v-icon>
              </v-list-item-icon>
          
              <v-list-item-content>
                <v-list-item-title v-text="item.text"></v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>

            </v-list>
          </v-card>
  
        </v-flex>
      </v-layout> 
    </v-container> -->

  </div>
</template>

<script>

// import StyleTransfer from './StyleTransfer'

// import UploadImage from '../uploads/UploadImage'
import { mapGetters, mapActions } from "vuex";


export default {

    components:{
        // StyleTransfer,

        // UploadImage
    },
    data () {

      return {
        selection:'gallery',
        items:[
        {id:1, src:'https://dakobed-style.s3-us-west-2.amazonaws.com/sunrise.jpg'}, 
        {id:2, src:'https://dakobed-style.s3-us-west-2.amazonaws.com/style_dir/gp_base.jpg'},
        {id:3, src: 'https://dakobed-style.s3-us-west-2.amazonaws.com/result.png'},

        {id:4, src:'https://dakobed-style.s3-us-west-2.amazonaws.com/baker_base.jpg'}, 
        {id:5, src:'https://dakobed-style.s3-us-west-2.amazonaws.com/monet_style.jpg'},
        {id:6, src: 'https://dakobed-style.s3-us-west-2.amazonaws.com/_at_iteration_9.png'}
        ],  
        menuItems:[
          {selection:'style',title:'Style Transfer'},

        ],
      directions: ['t', 'b', 'l', 'r', 's', 'e', 'x', 'y', 'a'],
      paddingSizes: ['auto', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
      marginSizes: [
        'auto',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
        'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'n10', 'n11', 'n12',
      ],
      paddingDirection: 'a',
      paddingSize: '2',
      marginDirection: 'a',
      marginSize: '2',
      playgroundText: 'Use the controls above to try out the different spacing helpers',
      model: 1,
      multiple: false,
      mandatory: false,
      flat: false,
      dense: false,
      count: 4,
      
      }
    },

    
    methods:{
        ...mapActions(["setGallerySelection"]),
        
        selectMenuItem(selection){

          this.setGallerySelection(selection)
        },
        // changeSelection(item_selection){
        //     this.selection = item_selection
        //     console.lo
        // },
    },
    computed: {
      ...mapGetters(["gallerySelection"])
    }
  }
</script>

<style>
  .spacing-playground .v-select .v-input__prepend-outer, .spacing-playground .v-select .v-input__append-outer{
    margin-top: 0.55rem;
    margin-right: 0.2rem;
  }
</style>