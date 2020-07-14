import Vue from 'vue'
import Router from 'vue-router'
import GalleryMenu from './components/gallery/GalleryMenu'
import Landing from './components/Landing'

import TranscriptionList from './components/TranscriptionList'

// import googlemap from './components/pipelines/tweets/googlemap'
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
      path: '/transcriptions',
      component: TranscriptionList
    },


    {
      path: '/gallery',
      component: GalleryMenu
    },

  ]
})
