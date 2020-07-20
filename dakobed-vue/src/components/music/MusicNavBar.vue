<template>
  <div>
    <v-card dark height="400" flat>

      <v-navigation-drawer
        absolute >

        <v-list
          dense
          nav
          class="py-0">

    <v-divider></v-divider>

              <v-list-item
                v-for="item in items"
                :key="item.title"
                link >

              <v-list-item-content @click="navigate(item.route)">

              <v-list-item-title>{{ item.title }}</v-list-item-title>

          </v-list-item-content>
         </v-list-item>
        </v-list>
      </v-navigation-drawer>

    </v-card>
  </div>
</template>

<script>

import router from '../../router'

export default {
 
  methods:{
      navigate(route){
          router.push(route)
      }

  },

  data () {
      return {
        drawer: true,
        items: [
          { title: 'Project Description', icon: 'mdi-view-dashboard', route:'/musiclanding' },
          { title: 'GuitarSet', icon: 'mdi-image', route:'/guitarset' },
          { title: 'Maestro', icon: 'mdi-help-box', route:'/maestro' },
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
  }
</script>