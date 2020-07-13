import axios from 'axios';

const state = {
  loadedReports: [],
  reportSelection:"landing",
  currentReport:-1,
  reportThumbnail:-2
};

const getters = {
  allReports: state => state.loadedReports,
  getCurrentReport: state => state.currentReport,
  reportSelection: state => state.reportSelection,
  getReportThumbail: state => state.reportThumbnail
  // gallerySelection: state => state.selection,
};

const actions = {
  async fetchReports({ commit }) {
    const response = await axios.get('localhost:8080/reports?userID=mddarr@gmail.com');
    commit('setReports', response.data);
  },

  async getReport({ commit }, id) {
    const response = await axios.get('http://localhost:8080/reports/detail/?id='+id)
    .catch((error) => console.log(error));
    commit('setReportSelection', response.data);
  },

  async setSelection({ commit }, selection) {

    commit('setSelection', selection)
  },

  async setReportThumbnail({ commit }, image) {

    commit('setReportThumbnail', image)
  },

  async postTripreport({commit}, payload){
      axios.post('http://localhost:8083/reports/post',payload).then((response) => {
        const reportID = response.id  
      commit('createReport',{
        ...payload,
        id:reportID
      })
          console.log(response);
        }, (error) => {
          console.log(error);
        });
    } 
  };

const mutations = {
  setReports: (state, reports) => (state.loadedReports = reports),
  setSelection: (state, id) => (state.reportSelection = id),
  setReportSelection: (state, report) => (state.currentReport = report),
  setReportThumbnail: (state, image) => (state.reportThumbnail = image),
  createReport (state, payload) {
    state.loadedReports.push(payload)
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
