<template>
  <div>
    <h2 class="product-title">{{ product.fin_prdt_nm }} 상세정보</h2>
    <div class="product-details">
      <p>공시 제출월 : {{ product.dcls_month }} </p>
      <p>금융회사 코드 : {{ product.fin_co_no }} </p>
      <p>금융회사 명 : {{ product.kor_co_nm}} </p>
      <p>금융 상품 코드 : {{ product.fin_prdt_cd }} </p>
      <p>금융 상품명 : {{ product.fin_prdt_nm }} </p>
      <p>가입 방법 : {{ product.join_way }} </p>
      <p>만기 후 이자율 : {{ product.mtrt_int }} </p>
      <p>우대조건 : {{ product.spcl_cnd }} </p>
      <p>가입 제한 : {{ product.join_deny }} </p>
      <p>가입대상 : {{ product.join_member }} </p>
      <p>기타 유의사항 : {{ product.etc_note }} </p>
      <p>최대 한도 : {{ product.max_limit }} </p>
      <p>공시 시작일 : {{ product.dcls_strt_day }} </p>
      <p>공시 종료일 : {{ product.dcls_end_day }} </p>
      <p>금융회사 제출일 : {{ product.fin_co_subm_day }} </p>
      <button @click="joinDeposit(product.fin_prdt_cd)" class="join-button">{{ buttonText }}</button>
      <hr class="divider">
      <h3>Options</h3>
      <div class="card-container">
  <DepositOptions v-for="option in options" :key="option.id" :option="option" />
</div>
      <hr class="divider">
      <DepositCommentList />
      <RouterLink :to="{name: 'dep_comment', params: {product_id: product.id}}" class="comment-link">[CREATE]</RouterLink>
      <RouterView />
    </div>
  </div>
</template>

<script setup>
import { useRoute, RouterLink, RouterView } from 'vue-router';
import { useProductStore } from '@/stores/product';
import { useCounterStore } from '@/stores/counter';
import { ref, computed, onMounted } from 'vue';

import axios from 'axios';
import DepositOptions from '@/components/products/DepositOptions.vue';
import DepositCommentList from '@/components/products/DepositCommentList.vue'

const route = useRoute()
const fin_prdt_cd = route.params.fin_prdt_cd

const store = useProductStore()
const counterStore = useCounterStore()

const myDeposits = computed(() => {
  return counterStore.info.deposit_products
})

const product = ref({})
const getDepositProduct = function (fin_prdt_cd) {
  product.value = store.depositProducts.find((depositProduct) => {
    return depositProduct.fin_prdt_cd === fin_prdt_cd
  })
}
getDepositProduct(fin_prdt_cd)

const options = ref([])
axios.get(`http://127.0.0.1:8000/api/v1/products/get-deposit-options/${fin_prdt_cd}/`)
  .then(response => {
    options.value = response.data
  })
  .catch(error => {
    console.error('Error fetching deposit options:', error);
  });

const isJoined = ref(false);

onMounted(() => {
  counterStore.getInfo()
  const productId = product.value.id
  const depositProducts = counterStore.info.deposit_products;
  store.getDepositComments(productId)

  if (depositProducts.some(depositProduct => depositProduct === productId)) {
    isJoined.value = true;
  }
})

const joinDeposit = function (fin_prdt_cd) {
  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/userinfo/join-deposit/${fin_prdt_cd}/`,
    headers: {
      Authorization: `Token ${counterStore.token}`
    }
  })
    .then(response => {
      console.log(response)
      isJoined.value = !isJoined.value;
    })
    .catch(error => {
      console.error('Error fetching deposit options:', error);
    });
}

const buttonText = computed(() => {
  return isJoined.value ? '해지하기' : '가입하기';
});
</script>

<style scoped>
.product-title {
  color: #008485; /* 메인 컬러로 변경 */
  margin-bottom: 20px;
}

.product-details p {
  margin-bottom: 10px;
}

.join-button {
  background-color: #008485; /* 메인 컬러로 변경 */
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
}

.join-button:hover {
  background-color: #006666; /* 메인 컬러의 조금 진한 버전으로 변경 */
}

.comment-link {
  color: #008485; /* 메인 컬러로 변경 */
  text-decoration: none;
  margin-left: 10px;
}

.comment-link:hover {
  text-decoration: underline;
}

.divider {
  border: none;
  border-top: 2px solid #008485; /* 메인 컬러로 변경 */
  margin: 20px 0;
}
.card-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between; /* 원하는 정렬 방식에 따라 변경할 수 있습니다. */
}

.DepositOptions {
  /* 원하는 스타일을 여기에 추가하세요. */
  /* 각 카드 요소에 대한 스타일을 지정할 수 있습니다. */
}

</style>
