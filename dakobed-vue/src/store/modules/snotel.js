/* eslint-disable */

import axios from 'axios';

const state = {
  locations: [],
  queryData:[],
  snowMedian:[],
  snowCurrent:[],
  waterCurrent:[],
  waterMedian:[],
  parsedSnowCurrent:[],
  reducedSnowCurrent: [],
  reducedSnowMedian:[]
};

const getters = {
    // getLocations: state => state.locations,
    // getQueryData: state => state.queryData,
    // getWaterMedian: state => state.waterMedian,
    // getWaterCurrent: state => state.waterCurrent,
    // getSnowCurrent: state => state.snowCurrent,
    // getSnowMedian: state => state.snowMedian,
    // getParsedSnowCurrent: state => state.parsedSnowCurrent,
    getReducedSnowCurrent: state => state.reducedSnowCurrent,
    getReducedSnowMedian: state => state.reducedSnowMedian
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

    reset_arrays({commit}){
      var data_obj = {current:[], median:[]}
      commit('setQueryData', data_obj)
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

          // var snowCurrent = []
          // var snowMedian = []
          // var waterCurrent = []
          // var waterMedian = []
          var date
          var i;
          var reducedSnowCurrent = [];
          var reducedSnowMedian = [];
          for (i = 0; i < data.length; i=i+14) {
            date = data[i].snotelDate.slice(4,6) +'-' + data[i].snotelDate.slice(6,8) +'-' + data[i].snotelDate.slice(0,4)
            reducedSnowCurrent.push({day:date, count: parseInt(data[i].snowCurrent) });
            reducedSnowMedian.push({day:date, count: parseInt(data[i].snowMedian) })
            // snowCurrent.push({day:date, count: parseInt(element.snowCurrent) })
            // snowMedian.push({day:date, count: element.snowMedian})
            // waterMedian.push({day:date, count: element.waterMedian})
            // waterCurrent.push({day:date, count: element.waterCurrent})
          }
          var data_obj = {current: reducedSnowCurrent, median:reducedSnowMedian}
          commit('setQueryData',data_obj)
          // data.forEach(element => {
              
          //     date = element.snotelDate.slice(0,4)+'-' + element.snotelDate.slice(4,6) +'-' + element.snotelDate.slice(6,8) 
          //     snowCurrent.push({day:date, count: parseInt(element.snowCurrent) })
          //     snowMedian.push({day:date, count: element.snowMedian})
          //     waterMedian.push({day:date, count: element.waterMedian})
          //     waterCurrent.push({day:date, count: element.waterCurrent})
          //   });
          
          // var reducedSnowCurrent = [];
          // for (i = 0; i < snowCurrent.length; i=i+4) {
          //   reducedSnowCurrent.push(snowCurrent[i]);
          // }

          // commit('setQueryData', snowCurrent, snowMedian, waterCurrent, waterMedian, reducedSnowCurrent)



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
    setQueryData: (state, data_object) => {
      state.reducedSnowCurrent = data_object.current
      state.reducedSnowMedian = data_object.median
    },


};

export default {
  state,
  getters,
  actions,
  mutations
};
