import Vuex from 'vuex';
import Vue from 'vue';
import reports from './modules/reports';


// Load Vuex
Vue.use(Vuex);

// Create store
export default new Vuex.Store({
  modules: {
    reports,
  }
});
