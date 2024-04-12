<template>
    <router-view></router-view>
  
    <div id="m">
      <div class="container">
        <div class="jumbotron text-center">
          <h1>Get Ready for Shopping</h1>
          <h5>Enter your details</h5>
          <form @submit.prevent="login" novalidate>
            <EmailField v-model="user.email" />
  
            <br />
  
            <PasswordField v-model="user.password" />
            <br />
            <div class="form-group">
              <button
                class="btn btn-primary"
                :disabled="isSignupButtonDisabled"
                @click="loginButtonPressed"
              >
                LOG IN
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { reactive, onBeforeMount } from 'vue'
  import EmailField from '@/components/EmailField.vue'
  import PasswordField from '@/components/PasswordField.vue'
  import useFormValidation from '../modules/useFormValidation'
  import useSubmitButtonState from '../modules/useSubmitButtonState'
  
  import customfetch from '../modules/customfetch'
  import router from '../router/index'
  const loggedin = localStorage.getItem('loggedin')
  const role = localStorage.getItem('role')
  const user = reactive({
    email: '',
    password: ''
  })
  onBeforeMount(() => {
    if (loggedin == 'true' && role == 'user') {
      router.push('/dashboard')
    }
  })
  
  function login() {
    customfetch('http://127.0.0.1:5000/auth/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
  
      body: JSON.stringify({ email: user.email, password: user.password })
    })
      .then((data) => {
        console.log(data.token)
        localStorage.setItem('token', data.token)
        localStorage.setItem('role', 'user')
        localStorage.setItem('loggedin', 'true')
        localStorage.setItem('email', data.email)
        router.push('/dashboard')
      })
      .catch((err) => {
        console.log(err.message)
        alert(err.message)
      })
  }
  
  const { errors } = useFormValidation()
  const { isSignupButtonDisabled } = useSubmitButtonState(user, errors)
  
  const loginButtonPressed = () => {
    console.log(user)
  }
  </script>
  
  <style>
  .jumbotron {
    /* background-image: url("@/assets/BGimg3.jpg"); */
    font-family: cursive;
  }
  .container {
    display: flex;
    justify-content: center;
    padding-top: 100px;
  }
  
  #m {
    background-image: url('@/assets/BGimg3.jpg');
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-size: 100% 100%;
  }
  </style>
  