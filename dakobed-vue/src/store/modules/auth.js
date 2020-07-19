/* eslint-disable */

// import axios from 'axios';
import * as  AmazonCognitoIdentity from "amazon-cognito-identity-js";
import axios from 'axios';


const state = {
    loggedIn: false,
    cognitoInfo:{},
    loadingState:true,
    errorLoadingState:false,
    token: false

};

const getters = {
    getJwtAccessToken: state => state.token
};

const actions = {

    async setJWT({commit}, token){
        commit('setAccessToken', token)
    },


    async authentication({commit}, email, password){
        
        var poolData = {
            UserPoolId : 'us-west-2_rrVhZsufQ',
            ClientId : '633b35gtorn2odi25dotujndob'
            };
        var userPool = new AmazonCognitoIdentity.CognitoUserPool(poolData);

        var userData = {
            Username : email, 
            Pool : userPool
        };

        var authenticationData = {
            Username : email, 
            Password : password, 
        };
        var authenticationDetails = new AmazonCognitoIdentity.AuthenticationDetails(authenticationData);

        var cognitoUser = new AmazonCognitoIdentity.CognitoUser(userData);
        cognitoUser.authenticateUser(authenticationDetails, {
            onSuccess: function (result) {
                console.log('access token + ' + result.getAccessToken().getJwtToken());
                commit('setAccessToken', result.getAccessToken().getJwtToken())
            },

            onFailure: function(err) {
                alert(err);
            },

        });
      },


    async registration({commit}){

    
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






function getUserInfo(){
        var jwtToken = auth.auth.getSignInUserSession().getAccessToken().jwtToken;
        const USERINFO_URL = 'https://'+auth.auth.getAppWebDomain() + '/oauth2/userInfo';
        var requestData = {
            headers: {
                'Authorization': 'Bearer '+ jwtToken
            }
        }
        return axios.get(USERINFO_URL, requestData).then(response => { 
            return response.data;
        });
    }
    


const mutations = {
    setLoggedIn: (state, newValue) => (state.loggedIn = newValue),
    setLoggedOut:(state) => {
        state.loggedIn=False; state.cognitoInfo = {}},
    setCognitoInfo:(state, newValue) => (state.cognitoInfo= newValue),
    setAccessToken:(state, token) => (state.token = token)
};

export default {
  state,
  getters,
  actions,
  mutations
};
