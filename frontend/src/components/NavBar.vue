<template>
  <nav class="navbar navbar-expand-md">
    <router-link class="navbar-brand" to="/"
      ><img src="#" style="width: 50px"
    /></router-link>
    <button
      class="navbar-toggler"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#navbarNav"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav mr-auto"></ul>
      <ul class="navbar-nav">
        <li v-for="link in links" :key="link.to" class="nav-item">
          <router-link class="nav-link" :to="link.path">{{ link.name }} </router-link>
        </li>
      </ul>
      <ul class="navbar-nav">
        <li v-if="checklogin()" class="nav-item">
          <button class="nav-link logout-btn" @click="logout">LOG OUT</button>
        </li>
      </ul>
    </div>
  </nav>
</template>
<script setup>
import { computed, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import router from '../router/index'

const route = useRoute()
function checklogin() {
  return localStorage.getItem('loggedin') === 'true'
}

const logout = () => {
  confirm('Are you sure you want to logout?')
  localStorage.removeItem('token')
  localStorage.removeItem('role')
  localStorage.removeItem('loggedin')
  localStorage.removeItem('email')
  router.push('/')
}
const links = computed(() => {
  switch (route.name) {
    case 'welcome':
      return [
        { name: 'Home', path: '/' },
        { name: 'Admin Log In', path: '/admin_login' },
        { name: 'User Log In', path: '/user_login' }
      ]
    case 'user_login':
      return [
        { name: 'Home', path: '/' },
        { name: 'Register', path: '/register' },

      ]
    case 'register':
      return [
        { name: 'Home', path: '/' },
        { name: 'Login', path: '/user_login' }
      ]
    case 'admin_dash':
      return [
        { name: 'Home', path: '/' }
      ]
    
    case 'admin_login':
      return [
        { name: 'Home', path: '/' }
      ]
    

    case 'admin_dash':
      return [{ name: 'Home', path: '/' }]

    default:
      return []
  }
})
</script>
<style scoped>
.navbar {
  font-family: Georgia, 'Times New Roman', Times, serif;
}
.navbar a {
  color: green;
}

.logout-btn {
  background-color: rgb(240, 168, 132);
  color: black
}
/* on hover */
.logout-btn:hover {
  color: red;
  cursor: pointer;
}
</style>
