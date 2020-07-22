import axios from 'axios';

const state = {
  locations: [],

};

const getters = {
  getLocations: state => state.locations,

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
    

    // async fetchLocations({ commit }) {
    //     const SNOTEL_IP = process.env('')
    //     console.log("SNOTEL IP " + SNOTEL_IP)
    //     const response = await axios.get('http://localhost:8085/products/');
    //     commit('setLocations', response.data);
    // },

  };

const mutations = {
    setLocations: (state, locations) => (state.locations = locations),

};

export default {
  state,
  getters,
  actions,
  mutations
};
