/* eslint-disable */

import axios from 'axios';

const state = {
  locations: [],
  queryData:[],
  snowMedian:[],
  snowCurrent:[],
  waterCurrent:[],
  waterMedian:[]

};

const getters = {
    getLocations: state => state.locations,
    getQueryData: state => state.queryData,
    getWaterMedian: state => state.waterMedian,
    getWaterCurrent: state => state.waterCurrent,
    getSnowCurrent: state => state.snowCurrent,
    getSnowMedian: state => state.snowMedian
};

const actions = {
  

    async fetchLocations({commit}){
        axios.get(window.__runtime_configuration.load_balancer_dns+"locations").then((response) => {
          var response_string = JSON.stringify(response.data)
          var data = JSON.parse(response_string)
          commit('setLocations', data)
      
        }, (error) => {
          console.log(error);
        });
      },

    async querySnotelData({commit}, query){
        var sdate = query.sdate.split('-')
        var parsedSDate = sdate[0] + sdate[1] + sdate[2]

        var edate = query.edate.split('-')
        var parsedEDate = edate[0] + edate[1] + edate[2]
        var location = query.location

        console.log(query.location)
        var url = window.__runtime_configuration.snotelAPI +'/snotel?location='+ location+'&sdate='+parsedSDate+'&edate='+parsedEDate    

        axios.get(url).then((response) => {
          var response_string = JSON.stringify(response.data.body)
          var data = JSON.parse(response_string)

          var snowCurrent = []
          var snowMedian = []
          var waterCurrent = []
          var waterMedian = []
          data.forEach(element => {
              snowCurrent.push({date:element.snotelDate, snowCurrent: element.snowCurrent })
              snowMedian.push({date:element.snotelDate, snowMedian: element.snowMedian})
              waterMedian.push({date:element.snotelDate, waterMedian: element.waterMedian})
              waterCurrent.push({date:element.snotelDate, snowMedian: element.waterCurrent})
            });


          commit('setQueryData', snowCurrent, snowMedian, waterCurrent, waterMedian)


        },(error) =>{
          console.log(error);
        }
      )
    }
    

    // async fetchLocations({ commit }) {
    //     const SNOTEL_IP = process.env('')
    //     console.log("SNOTEL IP " + SNOTEL_IP)
    //     const response = await axios.get('http://localhost:8085/products/');
    //     commit('setLocations', response.data);
    // },

  };

const mutations = {
    setLocations: (state, locations) => (state.locations = locations),
    setQueryData: (state, snowCurrent, snowMedian, waterCurrent, waterMedian) => {
      state.snowMedian = snowMedian,
      state.snowCurrent = snowCurrent,
      state.waterCurrent = waterCurrent,
      state.waterMedian = waterMedian
      
    },


};

export default {
  state,
  getters,
  actions,
  mutations
};
