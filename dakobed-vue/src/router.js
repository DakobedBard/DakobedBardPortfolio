import Vue from 'vue'
import Router from 'vue-router'
// import GalleryMenu from './components/gallery/GalleryMenu'
import Landing from './components/Landing'


import Register from './components/auth/Register'

import MaestroTranscriptions from './components/music/piano/MaestroTranscriptions'
import TranscriptionDetail from './components/music/guitar/TranscriptionDetail'

import TranscriptionList from './components/music/TranscriptionList'

import Transcriber from './components/music/Transcriber'
import MusicProjectIntro from './components/music/MusicProjectIntro'
import GuitarSet from './components/music/guitar/GuitarSet'
import Transcription from './components/music/Transcription'


// import StyleTransferProjectDescription from './components/gallery/StyleTransferProjectDescription'
// import Transfer from './components/gallery/Transfer'
// import StyleTransferProject from './components/style/StyleTransferProject'

import TweetsProject from './components/tweets/TweetsProject'
// import TweetsMap from './components/tweets/TweetsMap'
import TweetsLanding from './components/tweets/TweetsLanding'


import SnotelProject from './components/snotel/SnotelProject'
import LocationList from './components/snotel/LocationList'
// import SnotelD3 from './components/snotel/SnotelD3'
import LocationDetail from './components/snotel/LocationDetail'



import ECommerceIntro from './components/ecommerce/ECommerceIntro'
import Store from './components/ecommerce/Store'
import ProductDetail from './components/ecommerce/ProductDetail'
import ShoppingCart from './components/ecommerce/ShoppingCart'



import ReportsLanding from './components/reports/ReportsLanding'
import ReportsProject from './components/reports/ReportsProject'

import GoogleMap from './components/maps/GoogleMap'
import SpringProject from './components/spring/SpringProject'

import KafkaProject from './components/kafkaservices/KafkaProject'

import Style from './components/style/Style'

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
      path: '/landing',
      component: Landing
    },

    // {
    //   path:'/transfer',
    //   component: Transfer
    // },


    {
      name: 'transcription',
      path: '/transcription/:id',
      component: Transcription

    },

    {
      path: '/transcriptions',
      component: TranscriptionList
    },


    {
      path: '/style',
      component: Style
    },

    {
      path: '/ecommerce',
      component: ECommerceIntro
    },

    {
      path: '/storefront',
      component: Store
    },

    {
      path:'/eventservices',
      component: KafkaProject
    },

    { 
      path: '/product/:id',
      component: ProductDetail 
    },

    {
      path:'/cart',
      component: ShoppingCart
    },

    // {
    //   path: '/tweets',
    //   component: GoogleMap
    // },
    {
      path:'/tweets',
      component: TweetsProject
    },

    {
      path:'/tweetslanding',
      component: TweetsLanding
    },


    {
      name:'transcription_detail',
      path: '/transcription_detail/:fileID/:title',
      component: TranscriptionDetail
    },

    {
      path: '/maestro',
      component: MaestroTranscriptions
    },
    {
      path:'/register',
      name:'register',
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
      path: '/transcriptions',
      component: TranscriptionList

    },


    {
      path:'/guitarset',
      component: GuitarSet
    },

    {
      path:'/snotel',
      component: SnotelProject
    },

    {
      path:'/snoteldata',
      component: LocationList
    },
    // {
    //   path: '/snoteld3',
    //   component: SnotelD3
    // },

    { path: '/location/:id', 
        name:'location_detail',
        component: LocationDetail,
        props: true
    },
    

    {
      path:'/reports',
      component: ReportsLanding
    },
    {
      path:'/reportsproject',
      component: ReportsProject
    },
    {
      path:'/map',
      component: GoogleMap
    },
    {
      path: '/spring',
      component: SpringProject
    }


  ]
})
