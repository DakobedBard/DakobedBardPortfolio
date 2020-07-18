import axios from 'axios';


const state = {

  guitarsetData:[],

};

const getters = {
  getGuitarsetData: state => state.guitarsetData,

};

const actions = {

  async fetchGuitarsetData({commit}){

    // const api_gateway_url = 'http://dakobedapplicationlb-24d3a274b94296e6.elb.us-west-2.amazonaws.com/guitarset'

    const api_url = window.__runtime_configuration.load_balancer_dns+'guitarset'
    axios.get(api_url).then((response) => {

        var response_string = JSON.stringify(response.data)
        var data = JSON.parse(response_string)
        console.log(data)
        commit('setGuitarSetData', data)

      }, (error) => {
        console.log(error);
      });
  },


};

const mutations = {

    setGuitarSetData: (state, guitarset) => (state.guitarsetData = guitarset),

};

export default {
  state,
  getters,
  actions,
  mutations
};
