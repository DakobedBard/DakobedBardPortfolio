<template>
  <v-container>
    <v-layout>
      <v-flex md2>
        <BaseNavBar v-bind:items=items />
      </v-flex>
          
      <v-flex md10>
        <v-card flat>
          <v-card-title>Snotel Data Explorer </v-card-title>

            <v-card-subtitle>
                Select a location to view & query the snotel data for that location

            </v-card-subtitle>

          <v-layout>
            <v-flex md4 >
              <v-text-field 
                style="text-align:right"
                v-model="search"
                append-icon="mdi-magnify"
                label="Search"
                single-line
                hide-details>
          </v-text-field>
            </v-flex>
          </v-layout>

          


          
          <v-data-table dark 
              :headers="headers"
              :items="getLocations"
              :search="search"
              @click:row="locationClick">
            
          <template v-slot:default>
          <thead style="height:1000px">
              <tr>
                <th class="text-left">Location</th>
                <th class="text-left">Elevation</th>
                <th class="text-left">Region</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="location in getLocations" :key="location.location" >
                <td>{{ location.elevation }}</td>
                <td> {{ location.elevation  }} </td>
                <td> Wenatchee </td>
              </tr>
            </tbody>
          </template>
          </v-data-table>
        </v-card>


            <v-divider></v-divider>     


        
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
/* eslint-disable */
import BaseNavBar from  '../BaseNavBar'
import { mapGetters, mapActions } from "vuex";
import router from '../../router'
export default {

  created(){
    this.fetchLocations()
  },

  components:{
        BaseNavBar
        },

  data () {
      return {
        search: '',
        headers: [
          {
            align: 'start',
            sortable: false,
            value: 'name',
          },
          { text: 'Name', value: 'location' },
          { text: 'Elevation', value: 'elevation' },

        ],
        items: [
          { title: 'Snotel Project Description', icon: 'mdi-view-dashboard', route:'/snotel' },
          { title: 'Snotel Data', icon: 'mdi-image', route:'/snoteldata' },

        ],

      }
    },
    computed:{
        ...mapGetters(["getLocations"]),
    },
    methods:{
        ...mapActions(["fetchLocations"]),
        locationClick(location){
          console.log("Clicked on the location " + location.location)
          // const id = location.location_id
          // const name = location.location
          router.push({ name: 'location_detail', params: { id:location.location, location_name: location.location } })
      },
    }
}
</script>