<template>
  <hr class="divider">
  <div>
    <h4 class="product-info">
      <span class="product-name">{{ product.kor_co_nm }}의</span>
      <span class="product-name">{{ product.fin_prdt_nm }}</span>
      <span class="product-joins">가입자 수 : {{ productJoins }}</span>
      <RouterLink :to="{ name: 'savingDetail', params: { fin_prdt_cd: product.fin_prdt_cd } }" class="detail-link">상세 보기</RouterLink>
    </h4>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import { ref } from 'vue'
const props = defineProps({
  product: Object
})
const productId = props.product.id

const productJoins = ref()
import axios from 'axios';

  // Vue.js 컴포넌트 내에서 요청 보내기
axios.get(`http://127.0.0.1:8000/api/v1/products/saving-joins/${productId}/`)
  .then(response => {
    productJoins.value = response.data.num_users
  })
  .catch(error => {
    console.error('Error fetching saving joins:', error);
  });

</script>

<style scoped>
.product-info {
  font-size: 16px;
  color: #333; 
}

.product-name {
  margin-right: 5px;
}

.product-joins {
  margin-left: 10px;
}

.detail-link {
  color: #0066cc; /* 하나은행 브랜드 컬러 */
  text-decoration: none;
  margin-left: 10px;
}

.detail-link:hover {
  text-decoration: underline;
}

.divider {
  border: none;
  border-top: 2px solid #0066cc; /* 하나은행 브랜드 컬러 */
  margin: 20px 0;
}
</style>