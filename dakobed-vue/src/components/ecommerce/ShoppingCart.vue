<template>
  <v-container>
    <v-layout>
      <v-flex md6 offset-3>
        <v-card>
          {{products }}
        </v-card>

        <v-card class="mx-auto" max-width="800" tile flat>
            
            <v-subheader><h2>Shopping Cart</h2></v-subheader>
                <v-card flat class="pa-3" v-for="product in products" :key="product.id" >
                    {{product.id}}
                </v-card>
        </v-card>


      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {

    created(){
        let productIDs = Array.from( this.getCart.keys() );
        let quantities = Array.from(this.getCart.values())
        console.log("products " + productIDs )
        console.log("quantities " + quantities )
        const products = [] 
        // console.log(products)
        for (var i = 0; i < [productIDs.length]; i++) {
            products.push({id:productIDs.indexOf(i), quantity:quantities.indexOf(i)})
        }
        products.forEach(data => console.log("product ID " + data.id + " and the quantities  " + data.quantity))

    },

    data () {
     return {

        products:[]
     }
  },
    computed:{
        ...mapGetters(["getCart"]),
    },
    methods:{
        ...mapActions(["changeProductCartCount"]),
    }
}

</script>
