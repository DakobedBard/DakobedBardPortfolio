<template>
  <div>
    <v-container>
      <v-card flat>
        <v-layout>
          <v-flex  md5 offset-sm1>
            <v-card-title >Neural Style Transfer</v-card-title>
          </v-flex>

      <v-container fluid grid-list-md>
            <!-- xs = 600px full screen (12) -->
            <!-- md = 600px or more. half of the screen (6) -->
            <v-layout row wrap>

              <v-flex xs2 md3 offset-sm1 v-for="item in items" v-bind:key=item.id>
              </v-flex>
              {{reportID}}
                <!-- <v-flex xs12 md6 v-for="image in results" v-bind:key=image.id>
                    <v-card >
                        <v-img :src="image.images.fixed_height_small.url" height="200px"></v-img>
                    </v-card>
                </v-flex> -->
            </v-layout>
        </v-container>

<!-- <img src="https://dakobed-style.s3-us-west-2.amazonaws.com/sunrise.jpg" width="300" height="200"> -->
<!-- <img src="https://dakobed-style.s3-us-west-2.amazonaws.com/style_dir/gp_base.jpg" width="300" height="200">

<img src="https://dakobed-style.s3-us-west-2.amazonaws.com/result.png" width="300" height="200"> -->


        <v-divider></v-divider>
        <v-flex xs112 md4  offset-sm3>
        </v-flex>
        <v-divider></v-divider>
        </v-layout>
          <v-flex  md8 offset-sm1>
            <UploadImage button_title="Base"/>
          </v-flex>
        <v-layout>
          <v-flex  md8 offset-sm1>
            <div v-if="baseImageSelection != -2">
              <UploadImage button_title="Style"/>
            </div>
          </v-flex>
        </v-layout>
        <v-layout>
          <v-flex  md8 offset-sm1>
            <div v-if="baseImageSelection != -2 && styleImageSelection != -2">
              <v-btn raised class="primary mt4" @click="onStyleSubmit" > Submit Style Transfer </v-btn>
          </div>
          </v-flex>
        </v-layout>

      </v-card>      
    </v-container>
  </div>
</template>

<script>
import axios from 'axios'
import UploadImage from '../uploads/UploadImage'
import { mapGetters, mapActions } from "vuex";
import uploadsMixin from '../../mixins/uploadsMixin'

export default {
  created(){

  },

    components:{
      UploadImage
    },

    data(){
      return {
    
        reportID:-1,
        imageUrl:'',
        filename:''
        // imageURL:'https://dakobed.s3-us-west-1.amazonaws.com/stuart.jpg'
      }
    },

  methods:{
        ...mapActions(["setBaseImageSelection"]),
        ...mapActions(["setStyleImageSelection"]),
        onCreateReport(){
          if(!this.formIsValid){
            return
          }
        },
        onFileSelected(event){
            this.selectedFile = event.target.files[0]
        },
        onFilePicked(event){
          const files = event.target.files
          let filename = files[0].name;
          if (filename.lastIndexOf('.') <= 0){
            return alert('please add a valid file')
          }

          this.readImageFile(files[0])
        },

        readImageFile(filename){
          const fileReader = new FileReader();
          fileReader.addEventListener('load',() => {
            this.imageUrl = fileReader.result
          })
          fileReader.readAsDataURL(filename)
          console.log(filename)
        },

        onPickFile(){
          this.$refs.fileInput.click()
        },


        onStyleSubmit(){
          this.uploadPost(this.baseImageSelection, 'base_image')
          this.uploadPost(this.styleImageSelection, 'style_image')
        },

        onUpload(){
          const fd = new FormData()
          fd.append('file', this.selectedFile, this.selectedFile.name, fd)
          axios.post('http://localhost:8083/files',fd)
                    .then(res => {
              console.log(res)
            });
        }
    },
    computed:{
        ...mapGetters(["styleImageSelection"]),
        ...mapGetters(["baseImageSelection"]),
    formIsValid () {
        return this.title !== '' &&
          this.location !== '' &&
          this.imageUrl !== '' &&
          this.description !== ''
      },
        submittableDateTime () {
        const date = new Date(this.date)
        if (typeof this.time === 'string') {
          let hours = this.time.match(/^(\d+)/)[1]
          const minutes = this.time.match(/:(\d+)/)[1]
          date.setHours(hours)
          date.setMinutes(minutes)
        } else {
          date.setHours(this.time.getHours())
          date.setMinutes(this.time.getMinutes())
        }
        return date
      }
    },
    mixins: [uploadsMixin]

}
</script>
