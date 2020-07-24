/* eslint-disable */

import axios from 'axios';


const state = {
  tweets: [],

};

const getters = {
  getUploadedFile: state => state.tweets,

};

const actions = {
    
    // async uploadFile({commit}){
        
    //     var api_url = 'https://vzmta1umza.execute-api.us-west-2.amazonaws.com/v1/upload'
    //     axios.post('http://localhost:8081/tweets').then((response) => {
    
        
    //     var api_url = 2

    //     commit('getTweets', tweetsArray)

    //     }, (error) => {
    //     console.log(error);
    //     });
    // } 


};

const mutations = {
    setUploadedFile: (state, tweets) => (state.tweets = tweets)
};

export default {
  state,
  getters,
  actions,
  mutations
};
