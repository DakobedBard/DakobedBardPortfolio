import axios from 'axios';


const state = {
  notes: [],
  lines:[],
  nmeasures:-1,
  guitarsetData:[],
  maestroTrainingData:[],
  pianoLines:[]

};

const getters = {
  getGuitarsetData: state => state.guitarsetData,
  getNotes: state => state.notes,
  getLines:state => state.lines,
  getNMeasures: state => state.getNMeasures,
  getMaestroTraningData: state => state.maestroTrainingData,
  getPianoLines: state => state.pianoLines
};

const actions = {

  async fetchMaestroTrainingData({commit}){
    axios.get(window.__runtime_configuration.load_balancer_dns+"maestro").then((response) => {
      var response_string = JSON.stringify(response.data)
      var data = JSON.parse(response_string)
      commit('setMaestroTrainingData', data)
  
    }, (error) => {
      console.log(error);
    });
  },

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

  async getS3Transcription({commit}, fileID){

    // axios.get("https://dakobed-guitarset.s3-us-west-2.amazonaws.com/fileID" + fileID + "/" + fileID + "transcription.json").then((response) => {
      axios.get("https://dakobed-guitarset.s3-us-west-2.amazonaws.com/fileID" + fileID+"/transcription.json").then((response) => {
      var response_string = JSON.stringify(response.data)
      var notes = JSON.parse(response_string)

      var nnotes = notes.length
      var notesArray = []
      var i ;
      var note;
      for (i = 0; i < nnotes; i++) {
        note = notes[i]
        notesArray.push([note.measure, note.beat, Math.floor(note.midi), note.string])
      } 
      commit('setNotes', notesArray)

    }, (error) => {
      console.log(error);
    });

  },


};

const mutations = {
    setMaestroTrainingData: (state, trainingData) => (state.maestroTrainingData = trainingData),
    setGuitarSetData: (state, guitarset) => (state.guitarsetData = guitarset),
    setNotes: (state, notes) => {
      state.notes = notes

      var nmeasures = notes[notes.length -1][0] 
      var measures_per_line = 3
      var nlines = Math.floor(nmeasures/measures_per_line)
      if(nmeasures % 4 != 0){
          nlines +=1
      }
      var lines = []
      var i
      var current_note_index = 0;
      var lowest_measure = 0;
      var highest_measure = measures_per_line;
      var current_measure = 0;
      for(i =0; i < nlines; i++){
        var line = []
        while(current_measure >= lowest_measure && current_measure < highest_measure && current_note_index < notes.length ) {
            current_measure = notes[current_note_index][0]
            current_note_index+=1
            line.push(notes[current_note_index])   
        } 
        lines.push({id:i, notes:line})
        lowest_measure += measures_per_line
        highest_measure += measures_per_line
      }
      state.nmeasures = nmeasures
      state.lines = lines

    },
};

export default {
  state,
  getters,
  actions,
  mutations
};
