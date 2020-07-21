import Vue from 'vue'
import Router from 'vue-router'
// import GalleryMenu from './components/gallery/GalleryMenu'
import Landing from './components/Landing'
import MaestroTranscriptions from './components/music/piano/MaestroTranscriptions'
import TranscriptionList from './components/music/guitar/TranscriptionList'

import TranscriptionDetail from './components/music/guitar/TranscriptionDetail'
import TweetsLanding from './components/tweets/TweetsLanding'
import Register from './components/auth/Register'
import Transcriber from './components/music/Transcriber'
import MusicProjectIntro from './components/music/MusicProjectIntro'

import GuitarSet from './components/music/guitar/GuitarSet'

import StyleTransferProjectDescription from './components/gallery/StyleTransferProjectDescription'

import TweetsProjectDescription from './components/tweets/TweetsProjectDescription'


import SnotelProject from './components/snotel/SnotelProject'
import Resume from './components/landing/Resume'
Vue.use(Router)

export default new Router({
  mode:'history',
  base: process.env.BASE_URL,
  routes: [

    {
      path: '/',
      component: Landing
    },

    {
      path: '/resume',
      component: Resume
    },

    {
      path: '/landing',
      component: Landing
    },

    {
      path: '/transcriptions',
      component: TranscriptionList
    },

    {
      path: '/gallery',
      component: StyleTransferProjectDescription
    },

    {
      path: '/tweets',
      component: TweetsLanding
    },
    {
      path:'/tweetsintro',
      component: TweetsProjectDescription
    },


    {
      name:'transcription_detail',
      path: '/transcription_detail/:fileID',
      component: TranscriptionDetail
    },

    {
      path: '/maestro',
      component: MaestroTranscriptions
    },
    {
      path:'/register',
      component: Register
    },
    {
      path:'/transcriber',
      component: Transcriber
    },
    
    {
      path:'/musiclanding',
      component: MusicProjectIntro
    },

    {
      path:'/guitarset',
      component: GuitarSet
    },
    {
      path:'/snotel',
      component: SnotelProject

    }


  ]
})
