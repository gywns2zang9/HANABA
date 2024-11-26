<template>
  <div class="update-info-container">
    <h1>회원정보수정</h1>
    <form @submit.prevent="updateInfo">
      <div class="form-group">
        <label for="username">아이디 : </label>
        <input type="text" v-model.trim="username" id="username" class="form-control">
      </div>
      <div class="form-group">
        <label for="name">이름 : </label>
        <input type="text" v-model.trim="name" id="name" class="form-control">
      </div>
      <div class="form-group">
        <label for="age">나이 : </label>
        <input type="text" v-model.trim="age" id="age" class="form-control">
      </div>
      <div class="form-group">
        <label for="gender">성별 : </label>
        <input type="text" v-model.trim="gender" id="gender" class="form-control">
      </div>
      <div class="form-group">
        <label for="asset">자산 : </label>
        <input type="text" v-model.trim="asset" id="asset" class="form-control">
      </div>
      <div class="form-group">
        <label for="salary">연봉 : </label>
        <input type="text" v-model.trim="salary" id="salary" class="form-control">
      </div>
      <div class="form-group">
        <label for="target_period">목표 자산 : </label>
        <input type="text" v-model.trim="target_period" id="target_period" class="form-control">
      </div>
      <div class="form-group">
        <label for="future_value">목표 기간 : </label>
        <input type="text" v-model.trim="future_value" id="future_value" class="form-control">
      </div>
      <div class="form-group">
        <label for="purpose">목적 : </label>
        <input type="text" v-model.trim="purpose" id="purpose" class="form-control">
      </div>
      <input type="submit" class="submit-btn" value="수정">
    </form>
  </div>
</template>
  
  <script setup>
  import axios from 'axios';
  import { ref, onMounted } from 'vue'
  import { useRoute, useRouter } from 'vue-router';
  import { useCounterStore } from '@/stores/counter'

  const router = useRouter();

  const username = ref('') 
  const password1 = ref('')
  const password2 = ref('')
  const name = ref('')
  const age = ref('')
  const gender = ref('')
  const asset = ref('')
  const salary = ref('')
  const target_period = ref('')
  const future_value = ref('')
  const purpose = ref('')
  
  const info = ref(null)

  const store = useCounterStore()
  
  onMounted(() => {
    const token = localStorage.getItem('user-token')
    axios({
      method:'get',
      url:`${store.API_URL}/userinfo/`,
      headers: {
        Authorization: `Token ${token}`
      }
    })
      .then((response)=> {
        console.log(response)
        info.value = response.data
        username.value = info.value.username
        name.value = info.value.name
        age.value = info.value.age
        gender.value = info.value.gender
        asset.value = info.value.asset
        salary.value = info.value.salary
        target_period.value = info.value.target_period
        future_value.value = info.value.future_value
        purpose.value = info.value.purpose
        // console.log(info.value)
      })
      .catch((error)=> console.log(error))
  })
  
  const updateInfo = function () {
    axios({
        method: 'put',
        url:`${store.API_URL}/userinfo/`,
        data: {
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
        },
        headers: {
        Authorization: `Token ${store.token}`
        }
    })
        .then((response) => {
        router.push({ name: 'userInfo' })
        })
        .catch((error) => {
        console.log(error)
        })
    }
  </script>
  
  <style scoped>
  .update-info-container {
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