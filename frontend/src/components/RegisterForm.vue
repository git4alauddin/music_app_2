<template>
  <div class="register-form">
    <h2>Register</h2>
    <form @submit.prevent="register">
      <div class="form-group">
        <label>Username:</label>
        <input type="text" v-model="username" required>
      </div>
      <div class="form-group">
        <label>Email:</label>
        <input type="email" v-model="email" required>
      </div>
      <div class="form-group">
        <label>Password:</label>
        <input type="password" v-model="password" required>
      </div>
      <button type="submit">Register</button>
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
      username: '',
      email: '',
      password: '',
      errorMessage: '',
      successMessage: ''
    };
  },
  methods: {
    async register() {
      try {
        const response = await axios.post('http://localhost:5000/auth/register', {
          username: this.username,
          email: this.email,
          password: this.password
        });
        console.log('Registration successful:', response.data);
        this.successMessage = 'Registration successful';
        this.errorMessage = '';
        // Clear form fields
        this.username = '';
        this.email = '';
        this.password = '';

        
      } catch (error) {
        console.error('Registration failed:', error.response.data.message);
        this.errorMessage = error.response.data.message || 'Registration failed';
        this.successMessage = '';
      }
    }
  }
}
</script>

<style scoped>
.register-form {
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
.form-group input[type="text"],
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
