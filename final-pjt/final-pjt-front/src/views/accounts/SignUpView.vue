<!-- 호성이형이 알려준거 
  <div v-for="i in 10">
  <label for="">asdasdas</label>
  <input type="radio" name="" id="">
</div> -->
<template>
  <div class="signup-container">
    <h1>회원가입</h1>
    <form @submit.prevent="signUp">
      <div class="form-group">
        <label for="username">아이디</label>
        <input type="text" v-model.trim="username" id="username" class="form-control">
      </div>
      <div class="form-group">
        <label for="password1">비밀번호</label>
        <input type="password" v-model.trim="password1" id="password1" class="form-control">
      </div>
      <div class="form-group">
        <label for="password2">비밀번호 확인</label>
        <input type="password" v-model.trim="password2" id="password2" class="form-control">
      </div>
      <div class="form-group">
        <label for="name">이름</label>
        <input type="text" v-model.trim="name" id="name" class="form-control">
      </div>
      <div class="form-group">
        <label for="age">나이</label>
        <input type="text" v-model.trim="age" id="age" class="form-control">
      </div>
      <div class="form-group">
        <label for="gender">성별 (남자, 여자, 둘 다, 없음 중 택1)</label>
        <input type="text" v-model.trim="gender" id="gender" class="form-control">
      </div>
      <div class="form-group">
        <label for="asset">자산 (만 원 단위로 입력)</label>
        <input type="text" v-model.trim="asset" id="asset" class="form-control">
      </div>
      <div class="form-group">
        <label for="salary">연봉 (만 원 단위로 입력) </label>
        <input type="text" v-model.trim="salary" id="salary" class="form-control">
      </div>
      <div class="form-group">
        <label for="target_period">목표 자산 (만 원 단위로 입력) </label>
        <input type="text" v-model.trim="target_period" id="target_period" class="form-control">
      </div>
      <div class="form-group">
        <label for="future_value">목표 기간 (개월 단위로 입력) </label>
        <input type="text" v-model.trim="future_value" id="future_value" class="form-control">
      </div>
      <div class="form-group">
        <label for="purpose">목적</label>
        <input type="text" v-model.trim="purpose" id="purpose" class="form-control">
      </div>
      <input type="submit" class="submit-btn" value="가입하기">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const username = ref(null) 
const password1 = ref(null)
const password2 = ref(null)
const name = ref(null)
const age = ref(null)
const gender = ref(null)
const asset = ref(null)
const salary = ref(null)
const target_period = ref(null)
const future_value = ref(null)
const purpose = ref(null)

const store = useCounterStore()

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    name: name.value,
    age: age.value,
    gender: gender.value,
    asset: asset.value,
    salary: salary.value,
    target_period: target_period.value,
    future_value: future_value.value,
    purpose: purpose.value,
  }
  store.signUp(payload)
}

</script>

<style>
.signup-container {
  width: 600px;
  margin: 30px auto;
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