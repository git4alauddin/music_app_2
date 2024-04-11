<template>
    <div id="m">
      <div class="container">
        <div class="jumbotron text-center">
          <h1>Create Account</h1>
          <h5>Enter your Details</h5>
          <br />
          <form @submit.prevent="signup" novalidate>
            <div class="form-group">
              <NameField v-model="user.name" />
            </div>
            <br />
            <div class="form-group">
              <EmailField v-model="user.email" />
            </div>
            <br />
            <div class="form-group">
              <PasswordField v-model="user.password" />
            </div>
            <br />
            <div class="form-group">
              <button
                class="btn btn-primary"
                @click="signUpButtonPressed"
                :disabled="isSignupButtonDisabled"
              >
                SIGN UP
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { reactive, onBeforeMount } from 'vue'
  
  import NameField from '@/components/NameField.vue'
  import EmailField from '@/components/EmailField.vue'
  import PasswordField from '@/components/PasswordField.vue'
  import customfetch from '../modules/customfetch'
  import useFormValidation from '@/modules/useFormValidation'
  import useSubmitButtonState from '@/modules/useSubmitButtonState'
  import router from '../router'
  const loggedin = localStorage.getItem('loggedin')
  onBeforeMount(() => {
    if (loggedin == 'true') {
      router.push('/')
    }
  })
  const user = reactive({
    name: '',
    email: '',
    password: ''
  })
  function signup() {
    customfetch('http://127.0.0.1:5000/auth/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
  
      body: JSON.stringify({ username: user.name, email: user.email, password: user.password })
    })
      .then((data) => {
        console.log(data)
        alert('Successfully Signed Up, Redirecting to Login Page')
        router.push('/user_login')
      })
      .catch((err) => {
        console.log(err.message)
        alert(err.message)
      })
  }
  
  const { errors } = useFormValidation()
  const { isSignupButtonDisabled } = useSubmitButtonState(user, errors)
  
  const signUpButtonPressed = () => {
    console.log(user)
  }
  </script>
  
  <style>
  .jumbotron {
    /* background-color:rgb(255, 255, 100); */
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
  