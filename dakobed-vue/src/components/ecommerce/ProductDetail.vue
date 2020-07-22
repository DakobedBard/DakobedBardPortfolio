<template>
  <div>

    <v-container fluid>
        <template>
          <v-card
            color="grey lighten-4 " flat  tile>
            <v-toolbar flat extended >
              <!-- <v-app-bar-nav-icon></v-app-bar-nav-icon> -->
              <!-- <v-app-bar-nav-icon class ="grey--text">
              </v-app-bar-nav-icon> -->

              <v-spacer></v-spacer>

         <v-toolbar-items class = "hidden-xs-only">

         </v-toolbar-items>

            </v-toolbar>
          </v-card>
        </template>
      <v-layout row wrap>


          <v-flex md6 offset-1>

          </v-flex>
          <v-flex md3 offset-1>

            <v-card  tile flat >
    
              <v-btn icon>
                <v-icon @click="selectRoute('/cart')">mdi-cart</v-icon>
              </v-btn>
        
            </v-card>
          </v-flex>
          <v-flex md4>
           <v-card  tile flat >
            <v-flex>
                <v-card-text> <h1>{{ productName }} </h1> </v-card-text>
            </v-flex>
  
              <v-card-text> <h3> $ {{ price }} </h3> </v-card-text>
            </v-card>           
                  
            <v-btn rounded class="error mt4" @click="addToCart()" > Add to Cart </v-btn>
          
            </v-flex>
           
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import { mapActions } from "vuex";
import router from '../../router'
export default {
    created(){
        this.id = this.$route.params.id
        console.log('The id is: ' + this.$route.params.id);
        this.addDeleteItem({id:this.id,quantity: 1})
    },

    data () {
     return {
       
       productName: "Atmos 65",
       price:"180.00",
       id: this.$route.params.id,
       quantity:1
     }
  },
  methods:{
    ...mapActions(["addDeleteItem"]),
    addToCart(){
      this.addDeleteItem(this.id, this.quantity)
    },
    selectRoute(route){ // eslint-disable-line no-unused-vars
          router.push(route).catch(err => err)
    }
    
  }


}
</script>