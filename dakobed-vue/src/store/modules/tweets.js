import axios from 'axios';


const state = {
  tweets: [],

};

const getters = {
  getTweets: state => state.tweets,

};

const actions = {

  async fetchTweets({commit}){
    axios.get('http://localhost:8081/tweets').then((response) => {
      
      var response_string = JSON.stringify(response.data)
      var tweets = JSON.parse(response_string)
      // console.log("The notes array is " + notes.coronavirusconstructor == Array)
      // var a = typeof notes
      // console.log("the type of notes is " + a)
      // console.log(notes[0].midi)
      console.log("The length of the tweets response array is " + tweets.length)
      var tweetsArray = []
      var i ;
      var tweet;
      for (i = 0; i < tweets.length; i++) {
        // console.log(notes[i])
        tweet = tweets[i]
        tweetsArray.push({'username':tweet.username, 'content':tweet.content})
      } 
      console.log("THe length of the tweets arra yis " + tweetsArray.length)
      commit('getTweets', tweetsArray)

    }, (error) => {
      console.log(error);
    });
  } 


};

const mutations = {
    getTweets: (state, tweets) => (state.tweets = tweets)
};

export default {
  state,
  getters,
  actions,
  mutations
};
