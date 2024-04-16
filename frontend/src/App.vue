<template>
  <navbar />
  <body>
    <router-view></router-view>
  </body>
  <player />
  
  

  
  
</template>
<script>
import { RouterLink, RouterView } from 'vue-router'
import {ref} from 'vue'
import navbar from "@/components/NavBar.vue"
import player from "@/components/player.vue"
import { useRoute, useRouter } from 'vue-router';

export default {
  name: 'App',
  components: {
    navbar,
    player,
    RouterLink,
    RouterView,
  
  },
}

</script>


<style>

</style>

