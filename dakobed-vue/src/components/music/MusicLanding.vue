<template>
    <v-container>

      <v-layout>
        <v-flex md2>
          <v-card dark height="400" flat color="error">

            <v-navigation-drawer
            v-model="drawer"
            :color="color"
            :expand-on-hover="expandOnHover"

            :right="right"
            :permanent="permanent"
            :src="bg"
            absolute

          >
            <v-list
              dense
              nav
              class="py-0"
            >
              <v-divider></v-divider>

              <v-list-item
                v-for="item in items"
                :key="item.title"
                link
              >
                <v-list-item-content>
                  <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-navigation-drawer>



        </v-card>
        </v-flex>
        <v-flex  offset-xs2>
          <MusicProjectIntro />
        </v-flex>
      </v-layout> 
  
      <!-- <v-navigation-drawer
        v-model="drawer"
        :color="color"
        :expand-on-hover="expandOnHover"
        :mini-variant="miniVariant"
        :right="right"
        :permanent="permanent"
        :src="bg"
        absolute
        dark
      >
        <v-list
          dense
          nav
          class="py-0"
        >


          <v-divider></v-divider>

          <v-list-item
            v-for="item in items"
            :key="item.title"
            link
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer> -->
    


  </v-container>
</template>

<script>

import MusicProjectIntro from './MusicProjectIntro'

export default {
  components:{
    MusicProjectIntro
  },
  data () {
      return {
        drawer: true,
        items: [
          { title: 'Project Description', icon: 'mdi-view-dashboard' },
          { title: 'GuitarSet', icon: 'mdi-image' },
          { title: 'Maestro', icon: 'mdi-help-box' },
        ],
        color: 'primary',
        colors: [
          'primary',
          'blue',
          'success',
          'red',
          'teal',
        ],
      }
    },
    computed: {
      bg () {
        return this.background ? 'https://cdn.vuetifyjs.com/images/backgrounds/bg-2.jpg' : undefined
      },
    },
  }
</script>