<template>
    
</template>

<script>
export default {
      methods:{
      navigate(route){
        if(route != this.$route.path){
          router.push(route)
        }
          
      }

  },

  data () {
      return {

        items: [
          { title: 'Tweets Project Description', icon: 'mdi-view-dashboard', route:'/tweetsintro' },
          { title: 'Tweets Map', icon: 'mdi-image', route:'/tweets' },


        ],

      }
    },
  
}
</script>