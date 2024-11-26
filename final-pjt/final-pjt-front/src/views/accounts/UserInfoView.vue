<template>
  <div class="info-container">
    <h1>회원정보 페이지</h1>
    <div class="info-group">
      <p>이름 : {{ store.info.name }}</p>
      <p>나이 : {{ store.info.age }}살</p>
      <p>성별 : {{ store.info.gender }}</p>
      <p>자산 : {{ store.info.asset }}만 원</p>
      <p>연봉 : {{ store.info.salary }}만 원</p>
      <p>목표 자산 : {{ store.info.target_period }}만 원</p>
      <p>목표 기간 : {{ store.info.future_value }}개월</p>
      <p>목적 : {{ store.info.purpose }}</p>
      <p v-if="store.info.deposit_product_names && store.info.deposit_product_names.length > 0">예금가입상품 : {{ store.info.deposit_product_names.join(', ') }}</p>
      <p v-if="store.info.saving_product_names && store.info.saving_product_names.length > 0">적금가입상품 : {{ store.info.saving_product_names.join(', ') }}</p>
      <RouterLink :to="{name: 'userInfoUpdate'}" class="edit-link">수정하기</RouterLink>
      <hr>
      <br><strong>회원님과 비슷한 연령대가 가입한 예금 상품들</strong>
      <div>
        <br>
        <div v-for="(product, index) in recommendDeposit" :key="index">
        <p>{{ index + 1 }} 위</p>
        <p>상품명: {{ product.fin_prdt_nm }}</p>
        <p>가입 횟수: {{ product.count }}</p>
      </div>
      <br><strong>회원님과 비슷한 연령대가 가입한 적금 상품들</strong>
      <div>
        <br>
        <div v-for="(product, index) in recommendSaving" :key="index">
        <p>{{ index + 1 }} 위</p>
        <p>상품명: {{ product.fin_prdt_nm }}</p>
        <p>가입 횟수: {{ product.count }}</p>
      </div>
    </div>
    </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { RouterLink } from 'vue-router'
import axios from 'axios';


const store = useCounterStore()


onMounted(() => {
  store.getInfo();
  getTopDepositProducts()
  getTopSavingProducts()
});

const recommendDeposit = ref([])
const recommendSaving = ref([])

const getTopDepositProducts = function () {
    const token = localStorage.getItem('user-token')
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/products/top-deposit-products/`,
        headers: {
            Authorization: `Token ${token}`
        }
    })
    .then((response)=> {
        // 상품 정보를 받아온 후 처리
        console.log(response.data);
        recommendDeposit.value = response.data
        // 받아온 데이터를 변수에 저장하고 표시하는 등의 작업 수행
    })
    .catch((error)=> console.log(error))
}

const getTopSavingProducts = function () {
    const token = localStorage.getItem('user-token')
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/products/top-saving-products/`,
        headers: {
            Authorization: `Token ${token}`
        }
    })
    .then((response)=> {
        // 상품 정보를 받아온 후 처리
        console.log(response.data);
        recommendSaving.value = response.data
        // 받아온 데이터를 변수에 저장하고 표시하는 등의 작업 수행
    })
    .catch((error)=> console.log(error))
}

</script>

<style scoped>
.info-container {
  width: 500px;
  margin: 50px auto;
  padding: 30px;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  background-color: #f9f9f9;
}

h1 {
  color: #008485;
  text-align: center;
  margin-bottom: 20px;
}

.info-group {
  margin-bottom: 20px;
}

p {
  color: #333;
  font-size: 16px;
  line-height: 1.5;
}

.edit-link {
  display: block;
  text-align: center;
  color: #008485;
  font-weight: bold;
  text-decoration: none;
  margin-top: 20px;
}

.edit-link:hover {
  color: #006666;
}
</style>