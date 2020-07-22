import Vue from 'vue'
import Router from 'vue-router'
// import GalleryMenu from './components/gallery/GalleryMenu'
import Landing from './components/Landing'


import Register from './components/auth/Register'

import MaestroTranscriptions from './components/music/piano/MaestroTranscriptions'
import TranscriptionList from './components/music/guitar/TranscriptionList'
import TranscriptionDetail from './components/music/guitar/TranscriptionDetail'

import Transcriber from './components/music/Transcriber'
import MusicProjectIntro from './components/music/MusicProjectIntro'
import GuitarSet from './components/music/guitar/GuitarSet'

import StyleTransferProjectDescription from './components/gallery/StyleTransferProjectDescription'
import Transfer from './components/gallery/Transfer'


import TweetsProjectDescription from './components/tweets/TweetsProjectDescription'
import TweetsLanding from './components/tweets/TweetsLanding'


import SnotelProject from './components/snotel/SnotelProject'
import SnotelDataExplorer from './components/snotel/SnotelDataExplorer'
import SnotelD3 from './components/snotel/SnotelD3'
import LocationDetail from './components/snotel/LocationDetail'



import ECommerceIntro from './components/ecommerce/ECommerceIntro'
import Store from './components/ecommerce/Store'
import ProductDetail from './components/ecommerce/ProductDetail'
import ShoppingCart from './components/ecommerce/ShoppingCart'



import ReportsLanding from './components/reports/ReportsLanding'
import ReportsProject from './components/reports/ReportsProject'



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

    {
      path:'/transfer',
      component: Transfer
    },

    {
      path: '/transcriptions',
      component: TranscriptionList
    },

    {
      path: '/styletransfer',
      component: StyleTransferProjectDescription
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
      path: '/product/:id',
      component: ProductDetail 
    },

    {
      path:'/cart',
      component: ShoppingCart
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
    },

    {
      path:'/snoteldata',
      component: SnotelDataExplorer
    },
    {
      path: '/snoteld3',
      component: SnotelD3
    },

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
    }


  ]
})
