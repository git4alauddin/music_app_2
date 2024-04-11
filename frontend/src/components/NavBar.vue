<template>
    <nav class="navbar">
      <div class="container">
        <a class="navbar-brand" href="/">My Music App</a>
        <div class="navbar-search">
          <input type="text" class="search-input" placeholder="Search...">
          <button class="search-button">Search</button>
        </div>
        <ul class="navbar-nav">
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/dashboard">Dashboard</router-link></li>
          <li><router-link to="/about">About</router-link></li>
          <!-- Add more links as needed -->
        </ul>
      </div>
    </nav>
  </template>

  <script setup>
  import { computed, ref } from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  import router from '../router/index'
  
  const route = useRoute()
  
  </script>

<style scoped>
  .navbar {
    background-color: #007bff;
    color: #fff;
    padding: 10px 0;
  }
  
  .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .navbar-brand {
    font-size: 1.5rem;
    text-decoration: none;
    color: #fff;
  }
  
  .navbar-search {
    display: flex;
    align-items: center;
  }
  
  .search-input {
    padding: 8px;
    border-radius: 5px;
    border: 1px solid #ccc;
    margin-right: 10px;
    width: 200px;
  }
  
  .search-button {
    padding: 8px 16px;
    background-color: #fff;
    border: none;
    border-radius: 5px;
    color: #007bff;
    cursor: pointer;
  }
  
  .navbar-nav {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .navbar-nav li {
    display: inline;
    margin-left: 20px;
  }
  
  .navbar-nav li a {
    text-decoration: none;
    color: #fff;
  }
  
  .navbar-nav li a:hover {
    text-decoration: underline;
  }
  </style>
  