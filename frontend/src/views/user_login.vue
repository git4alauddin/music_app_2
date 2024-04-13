<template>
    <router-view></router-view>
  
    <div id="m">
      <div class="container">
        <div class="jumbotron text-center">
          <h1>Ready to explore the music world?</h1>
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
  
  async function login() {
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
        localStorage.setItem('email', data.email),
        localStorage.setItem('id', data.id)
        router.push('/user_dash')
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
  
  <style scoped>
  /* Container */
  .container {
    display: flex;
    justify-content: center; /* Center horizontally */
    align-items: center; /* Center vertically */
    height: 100vh; /* Make the container full height of the viewport */
    background-image: url('your-background-image-url.jpg'); /* Set background image */
    background-size:90%; /* Cover the entire container with the background image */
    backdrop-filter: blur(10px); /* Apply blur effect to the container */
  }

  /* Jumbotron */
  .jumbotron {
    text-align: center; /* Center the text */
    max-width: 600px; /* Limit the width of the jumbotron */
    padding: 30px; /* Add padding to the jumbotron */
    background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent white background */
    border-radius: 10px; /* Add border radius to the jumbotron */
    box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.3); /* Add box shadow */
  }

  .jumbotron h1 {
    color: #333; /* Heading color */
    margin-bottom: 20px; /* Add some space below the heading */
  }

  .jumbotron h5 {
    color: #666; /* Text color */
    margin-bottom: 20px; /* Add some space below the subtitle */
  }

  /* Form styles */
  form {
    margin-top: 20px; /* Add space above the form */
  }

  .form-group {
    margin-bottom: 20px; /* Add space below form elements */
  }

  /* Button styles */
  .btn-primary {
    background-color: #007bff; /* Button background color */
    color: #fff; /* Button text color */
    border: none; /* Remove button border */
    padding: 10px 20px; /* Add padding to the button */
    border-radius: 4px; /* Add border radius to the buttons */
    cursor: pointer; /* Change cursor to pointer on hover */
    transition: background-color 0.3s ease; /* Smooth background color transition */
  }

  /* Hover effect for the buttons */
  .btn-primary:hover {
    background-color: #0056b3; /* Darker background color on hover */
  }
</style>


  