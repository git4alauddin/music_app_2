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
  
  <style scoped>
  #m {
    background-image: url('your-background-image-url.jpg');
    background-size: cover;
    background-position: center;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .container {
    background-color: rgba(255, 255, 255, 0.8);
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(5px);
  }

  .jumbotron {
    width: 400px;
  }

  .jumbotron h1 {
    font-size: 32px;
    margin-bottom: 20px;
    color: #333;
  }

  .jumbotron h5 {
    font-size: 18px;
    margin-bottom: 20px;
    color: #666;
  }

  .form-group {
    margin-bottom: 20px;
  }

  .form-group input[type="text"],
  .form-group input[type="email"],
  .form-group input[type="password"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-sizing: border-box;
    font-size: 16px;
  }

  .form-group button[type="submit"] {
    width: 100%;
    padding: 10px;
    border: none;
    border-radius: 5px;
    background-color: #007bff;
    color: #fff;
    font-size: 18px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .form-group button[type="submit"]:hover {
    background-color: #0056b3;
  }
</style>

  