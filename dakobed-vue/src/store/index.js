import Vuex from 'vuex';
import Vue from 'vue';
import transcriptions from './modules/transcriptions';




// Load Vuex
Vue.use(Vuex);

// Create store
export default new Vuex.Store({
  modules: {
    transcriptions,
  }
});
