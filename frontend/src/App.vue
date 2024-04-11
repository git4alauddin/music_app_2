<template>
  <navbar />
  <body>
    <router-view></router-view>
  </body>
  
  

  
  
</template>
<script>
import { RouterLink, RouterView } from 'vue-router'
import {ref} from 'vue'
import navbar from "@/components/navbar.vue"
import { useRoute, useRouter } from 'vue-router';

export default {
  name: 'App',
  components: {
    navbar,
    RouterLink,
    RouterView,
  
  },
}

</script>


<style>

</style>

