<template>
  <div>
    <v-card dark height="400" flat>

      <v-navigation-drawer
        v-model="drawer"
        :color="color"
        :expand-on-hover="expandOnHover"

        :right="right"
        :permanent="permanent"
        :src="bg"
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

              <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
         </v-list-item>
        </v-list>
      </v-navigation-drawer>

    </v-card>
  </div>
</template>

<script>
export default {
    
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
  }
</script>