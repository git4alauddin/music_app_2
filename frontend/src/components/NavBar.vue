<template>
  <nav class="navbar">
    <router-link class="navbar-brand" to="/">
      <!-- Add your brand logo or text here -->
      MusicHub
    </router-link>



    <button class="navbar-toggler" @click="toggleNav">
      <span class="navbar-toggler-icon"></span>
    </button>
    <ul class="navbar-nav" :class="{ 'show': isNavOpen }">
      <li v-for="link in links" :key="link.to" class="nav-item">
        <router-link class="nav-link" :to="link.path">
          <i :class="link.icon"></i> {{ link.name }}
        </router-link>
      </li>
      <li v-if="checklogin()" class="nav-item">
        <button class="nav-link logout-btn" @click="logout">
          <i class="logout-icon"></i> Logout
        </button>
      </li>
    </ul>
  </nav>
</template>
<script setup>
import axios from 'axios'
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
        { name: 'User Log In', path: '/user_login' },
        { name: 'Dashboard', path: '/dashboard' }
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
    
    case 'user_dash':
      return [
        { name: 'Home', path: '/' },
        {name: 'Dashboard', path: '/dashboard'}
      ]
    

    case 'upload_song':
      return [{ name: 'Dashboard', path: '/dashboard' }]

    default:
      return []
  }
})
</script>



<style scoped>
.navbar {
  background-color: #f8f9fa;
  padding: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.navbar-toggler {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
}

.navbar-toggler-icon {
  width: 20px;
  height: 2px;
  background-color: #333;
  display: block;
}

.navbar-nav {
  list-style-type: none;
  margin: 0;
  padding: 0;
  display: flex;
}

.nav-item {
  margin-left: 20px;
}

.nav-link {
  color: #333;
  text-decoration: none;
  display: flex;
  align-items: center;
}

.logout-btn {
  background-color: transparent;
  border: none;
  cursor: pointer;
  color: #333;
}

.logout-icon {
  /* Add your logout icon styles here */
}

.show {
  display: flex;
}
</style>


