<template>
  <div class="login-container">
    <h1>로그인</h1>
    <form @submit.prevent="logIn">
      <div class="form-group">
        <label for="username">아이디 : </label>
        <input type="text" v-model.trim="username" id="username" class="form-control">
      </div>
      <div class="form-group">
        <label for="password">비밀번호 : </label>
        <input type="password" v-model.trim="password" id="password" class="form-control">
      </div>
      <input type="submit" class="submit-btn">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const username = ref(null)
const password = ref(null)
const store = useCounterStore()

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}

</script>

<style>
.login-container {
  width: 300px;
  margin: 50px auto;
  padding: 30px;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h1 {
  color: #008485;
  text-align: center;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  color: #008485;
  display: block;
  margin-bottom: 5px;
}

.form-control {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.submit-btn {
  width: 100%;
  padding: 10px;
  background-color: #008485;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-btn:hover {
  background-color: #006666;
}
</style>