<template>
  <v-container>
    <v-layout row wrap>


          <v-flex md6 offset-1>

          </v-flex>
          <v-flex md3 offset-1>

            <v-card  tile flat >
    
              <v-btn icon>
                <router-link to="/cart">
                <v-icon  >mdi-cart</v-icon>
                </router-link>
              </v-btn>
        
            </v-card>
          </v-flex>

          <v-flex xs2 md3 offset-sm1 v-for="item in allProducts" v-bind:key=item.id>
            <ProductCard v-bind:productID="item.id" v-bind:productName="item.productName" 
            v-bind:imageURL="item.imageURL" v-bind:productPrice="item.price"/>
              <v-card >
                  <v-img :src="item.imageURL" height="200px" width="100"></v-img>
                  what
              </v-card>
              
          </v-flex>
      </v-layout>
  </v-container>
</template>
<script>

export default {
    
}
</script>