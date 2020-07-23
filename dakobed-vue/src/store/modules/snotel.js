import axios from 'axios';

const state = {
  locations: [],
  queryData:[]

};

const getters = {
  getLocations: state => state.locations,
  getQueryData: state => state.queryData
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

    async querySnotelData({commit}){
        var url = window.__runtime_configuration.load_balancer_dns+'snotel_dates?id=Blewett Pass&sdate=20140102&edate=20140104'  
        axios.get(url).then((response) => {
          var response_string = JSON.stringify(response.data)
          var data = JSON.parse(response_string)
          commit('setQueryData', data)
      })
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
    setQueryData: (state, queryData) => (state.queryData = queryData ),


};

export default {
  state,
  getters,
  actions,
  mutations
};
