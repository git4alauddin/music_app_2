<template>
    <div class="container">
      <div class="jumbotron text-center">
        <h1><b>Welcome to the world of music!</b></h1>
  
        <h4>Your favourite music hub</h4>
        <br />
        <h4>Already a user?</h4>
  
        <router-link class="btn btn-primary btn-lg" to="/user_login">Log In</router-link>
        <br />
        <br />
  
        <h4>Don't have an account?</h4>
  
        <router-link class="btn btn-primary btn-lg" to="/register">Register</router-link>
      </div>
    </div>
  </template>

  <script setup>
  import { onBeforeMount } from 'vue'
  import router from '../router/index'
//   const loggedin = localStorage.getItem('loggedin')
  
  </script>

<style>
.jumbotron {
  font-family: cursive;

  /* background-image: url('@/assets/BGimg3.jpg'); */
  background-size: 100% 100%;
  background-attachment: fixed;
  background-repeat: no-repeat;
}
.container {
  display: flex;
  justify-content: center;
  padding-top: 100px;
}
</style>
  