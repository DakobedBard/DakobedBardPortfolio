import Vuex from 'vuex';
import Vue from 'vue';
import transcriptions from './modules/transcriptions';
import tweets from './modules/tweets'
import auth from './modules/auth'


// Load Vuex
Vue.use(Vuex);

// Create store
export default new Vuex.Store({
  modules: {
    transcriptions,
    tweets,
    auth
  }
});
