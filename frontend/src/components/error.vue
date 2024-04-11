<template>
    <div v-if="check" class="alert alert-danger text-center">
      
      {{ error }}
      
    </div>
  </template>
  
  <script>
  export default {
    props: {
      error: String,
    },
    methods: {
      dismiss() {
        error.value=null;
      },
      check() {
        if (error.value!=null) {
          return true;
        } else {
          return false;
        }
      },
    },
  };
  </script>
  