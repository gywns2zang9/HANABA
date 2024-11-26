<template>
  <div class="exchange-box">
    <div v-for="country in mainExchangeRates" :key="country.id" class="country-rate">
      <!-- 국가명과 매매기준율 표시 -->
      <h3>{{ country.cur_nm.split(' ')[0] }}</h3>
      <h4>{{ country.kftc_deal_bas_r }}</h4>
      <!-- 송금환율 정보 박스 -->
      <div class="transfer-box-container">
        <!-- 첫 번째 송금환율 정보 박스 -->
        <div class="transfer-box">
          <h5>송금받으실 때</h5>
          <p>{{ country.ttb }}</p>
        </div>
        <!-- 두 번째 송금환율 정보 박스 -->
        <div class="transfer-box">
          <h5>송금보내실 때</h5>
          <p>{{ country.tts }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';

defineProps({
  mainExchangeRates: Object
});
</script>

<style scoped>
.exchange-box {
  width: 1400px;
  display: flex;
  justify-content: space-around;
}

.country-rate {
  background-color: #008485;
  color: white;
  padding: 20px;
  border-radius: 10px;
  margin: 10px;
  width: calc(33.33% - 20px); /* 3개의 박스로 나누기 위한 너비 조정 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 그림자 효과 추가 */
}

.transfer-box-container {
  display: flex;
}

.transfer-box {
  width: 130px;
  flex: 1; /* 가로 공간 동일하게 할당 */
  text-align: center;
  border-radius: 10px;
  background-color: rgba(0, 0, 0, 0.1); 
  padding: 10px; /* 내부 여백 추가 */
  margin-right: 10px; /* 오른쪽 마진 추가 */
}

h3 {
  margin-top: 0;
  font-size: 1.2rem; /* 좀 더 큰 글자 크기 */
}

h4 {
  text-align: center;
  margin-bottom: 10px; /* h4 요소 아래 여백 추가 */
}

h5 {
  margin-top: 0;
  font-size: 1rem;
}

p {
  margin: 5px 0;
}
</style>
