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

<style scoped>
  /* Container */
  .container {
    display: flex;
    justify-content: center; /* Center horizontally */
    align-items: center; /* Center vertically */
    height: 70vh; /* Make the container full height of the viewport */
  }

  /* Jumbotron */
  .jumbotron {
    text-align: center; /* Center the text */
    max-width: 600px; /* Limit the width of the jumbotron */
  }

  .jumbotron h1 {
    color: #333; /* Heading color */
    margin-bottom: 20px; /* Add some space below the heading */
  }

  .jumbotron h4 {
    color: #666; /* Text color */
  }

  /* Login and Registration Buttons */
  .btn-primary {
    background-color: #007bff; /* Button background color */
    color: #fff; /* Button text color */
    border: none; /* Remove button border */
    padding: 10px 20px; /* Add padding to the button */
    margin-top: 20px; /* Add some space above the buttons */
    border-radius: 4px; /* Add border radius to the buttons */
    cursor: pointer; /* Change cursor to pointer on hover */
    transition: background-color 0.3s ease; /* Smooth background color transition */
  }

  /* Hover effect for the buttons */
  .btn-primary:hover {
    background-color: #0056b3; /* Darker background color on hover */
  }
</style>


  