<template>
  <div class="hello">
    <h1>{{ greeting }}</h1>

    <div class="auth-buttons">
      <button class="auth-button" @click="toggleLoginForm">Login</button>
      <button class="auth-button" @click="toggleRegisterForm">Register</button>
    </div>

    <Login v-if="showLoginForm" />
    <Register v-if="showRegisterForm" />
  </div>
</template>

<script>
import Login from './LoginForm.vue';
import Register from './RegisterForm.vue';

export default {
  name: 'HelloWorld',
  components: {
    Login,
    Register
  },
  data() {
    return {
      greeting: 'Welcome to My Music App!',
      showLoginForm: false,
      showRegisterForm: false
    };
  },
  methods: {
    toggleLoginForm() {
      this.showLoginForm = !this.showLoginForm;
      this.showRegisterForm = false; // Close register form when opening login form
    },
    toggleRegisterForm() {
      this.showRegisterForm = !this.showRegisterForm;
      this.showLoginForm = false; // Close login form when opening register form
    }
  }
}
</script>

<style scoped>
.hello {
  text-align: center;
}

.auth-buttons {
  margin-bottom: 20px;
}

.auth-button {
  margin: 0 10px;
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  font-size: 16px; /* Increase font size */
}

.auth-button:hover {
  background-color: #0056b3;
}
</style>
