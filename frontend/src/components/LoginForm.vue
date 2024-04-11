<template>
  <div class="login-form">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <div class="form-group">
        <label>Email:</label>
        <input type="email" v-model="email" required>
      </div>
      <div class="form-group">
        <label>Password:</label>
        <input type="password" v-model="password" required>
      </div>
      <button type="submit">Login</button>
    </form>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    <p v-if="successMessage" class="success">{{ successMessage }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: '',
      errorMessage: '',
      successMessage: ''
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://localhost:5000/auth/login', {
          email: this.email,
          password: this.password
        });

        // Store token and user ID in session storage
        sessionStorage.setItem('token', response.data.token);
        sessionStorage.setItem('id', response.data.id);

        console.log('Login successful:', response.data);
        this.successMessage = 'Login successful';
        this.errorMessage = '';

        // You can redirect the user to another page upon successful login if needed

        // Clear form fields
        this.email = '';
        this.password = '';
      } catch (error) {
        console.error('Login failed:', error.response.data.message);
        this.errorMessage = error.response.data.message || 'Login failed';
        this.successMessage = '';
      }
    }
  }
}
</script>

<style scoped>
.login-form {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}

h2 {
  margin-bottom: 20px;
  text-align: center;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  font-weight: bold;
}

/* Target only input elements inside .form-group */
.form-group input[type="email"],
.form-group input[type="password"] {
  width: calc(100% - 22px); /* Adjust the width based on the padding */
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-right: 10px; /* Add margin to the right side */
}

button[type="submit"] {
  display: block;
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button[type="submit"]:hover {
  background-color: #0056b3;
}

.error,
.success {
  margin-top: 10px;
  text-align: center;
}
.error {
  color: red;
}
.success {
  color: green;
}
</style>

