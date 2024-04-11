<template>
  <div id="app">
    <NavBar />
    <router-view />
    <HelloWorld />
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';
import NavBar from './components/NavBar.vue';

export default {
  name: 'App',
  components: {
    HelloWorld, 
    NavBar
  }
}
</script>

<style>
/* Add your global styles here */
</style>
