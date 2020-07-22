/* eslint-disable */

import axios from 'axios';


const state = {
  products: [],

};

const getters = {
  getProducts: state => state.products,

};

const actions = {

  async fetchProducts({commit}){
    axios.get('http://localhost:8085/products').then((response) => {
      commit('setProducts', response.data)
    }, (error) => {
      console.log(error);
    });
  } 


};

const mutations = {
    setProducts: (state, products) => (state.products = products)
};

export default {
  state,
  getters,
  actions,
  mutations
};
