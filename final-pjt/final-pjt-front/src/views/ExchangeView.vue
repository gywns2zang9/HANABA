<template>
  <div class="exchange-calculator">
    <!-- 페이지 제목 -->
    <h3>환율 계산기</h3>
    
    <!-- 기준 국가 선택 -->
    <div class="form-group">
      <label for="baseCountry">기준 국가 선택 </label>
      <select id="baseCountry" v-model="selectedBaseCountry" @change="calculateAmount">
        <option v-for="country in exchangeRates" :key="country.id" :value="country.cur_nm">
          {{ country.cur_nm.split(' ')[0] }} ({{ country.cur_unit }})
        </option>
      </select>
    </div>

    <!-- 금액 입력 -->
    <div class="form-group">
      <label for="inputAmount">변환 금액 입력 </label>
      <input id="inputAmount" type="number" v-model="inputAmount" @input="calculateAmount" placeholder="금액을 입력해주세요.">
    </div>
    
    <!-- 변환할 국가 선택 -->
    <div class="form-group">
      <label for="targetCountry">변환 국가 선택 </label>
      <select id="targetCountry" v-model="selectedTargetCountry" @change="calculateAmount">
        <option v-for="country in exchangeRates" :key="country.id" :value="country.cur_nm">
          {{ country.cur_nm.split(' ')[0] }} ({{ country.cur_unit }})
        </option>
      </select>
    </div>
    
    <!-- 변환된 금액 표시 -->
    <p v-if="convertedAmount !== null" class="converted-amount">
      {{ conversionText }}
    </p>
  </div>
<h3>주요 환율 정보</h3>

<!-- ExchangeBox 컴포넌트 렌더링 -->
<div class="exchange-box-container">
<ExchangeBox :mainExchangeRates="mainExchangeRates"  />
</div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue';
import { useExchangeStore } from '@/stores/exchange';
import ExchangeBox from '@/components/ExchangeBox.vue'

// 상태 관리 스토어 사용
const store = useExchangeStore();

// 환율 데이터, 선택된 기준 국가, 변환 국가, 입력 금액, 변환된 금액을 위한 ref 선언
const exchangeRates = ref([]);
const selectedBaseCountry = ref(null);
const selectedTargetCountry = ref(null);
const inputAmount = ref(null);
const convertedAmount = ref(null);

onMounted(() => {
  // 페이지 로드 시 환율 데이터를 가져옴
  store.getExchangeRates().then(() => {
    exchangeRates.value = store.exchangeRates;
  });
});
// mainExchangeRates computed 속성 정의
const mainExchangeRates = computed(() => {
  return exchangeRates.value.filter(rate => rate.cur_unit === 'USD' || rate.cur_unit === 'JPY(100)' || rate.cur_unit === 'EUR');
});

function calculateAmount() {
  // 기준 국가와 금액이 입력되었을 때 계산 실행
  if (selectedBaseCountry.value && inputAmount.value) {
    // 기준 국가의 환율 정보 찾기
    const baseCountryRate = exchangeRates.value.find(rate => rate.cur_nm === selectedBaseCountry.value);

    if (baseCountryRate) {
      // 기준 국가의 환율을 숫자로 변환 (쉼표 제거)
      const baseRate = parseFloat(baseCountryRate.kftc_bkpr.replace(',', ''));
      // 입력된 금액을 기준 국가 환율로 변환
      const converted = parseFloat(inputAmount.value) * baseRate;
      // 변환된 금액을 소수점 2자리로 반올림하여 저장
      convertedAmount.value = converted.toFixed(2);
    } else {
      // 기준 국가 환율 정보를 찾지 못했을 때 에러 로그 출력
      console.error('선택한 기준 국가의 환율 정보를 찾을 수 없습니다.');
      // 변환된 금액을 null로 설정
      convertedAmount.value = null;
    }
  }

  // 변환 국가가 선택되었고 변환된 금액이 null이 아닐 때 실행
  if (selectedTargetCountry.value && convertedAmount.value !== null) {
    // 변환 국가의 환율 정보 찾기
    const targetCountryRate = exchangeRates.value.find(rate => rate.cur_nm === selectedTargetCountry.value);
    
    if (targetCountryRate) {
      // 변환 국가의 환율을 숫자로 변환 (쉼표 제거)
      const targetRate = parseFloat(targetCountryRate.kftc_bkpr.replace(',', ''));
      // 변환된 금액을 변환 국가 환율로 다시 계산
      convertedAmount.value = (convertedAmount.value / targetRate).toFixed(2);
    } else {
      // 변환 국가 환율 정보를 찾지 못했을 때 에러 로그 출력
      console.error('선택한 변환 국가의 환율 정보를 찾을 수 없습니다.');
      // 변환된 금액을 null로 설정
      convertedAmount.value = null;
    }
  }
}

// 변환 결과를 텍스트로 반환하는 computed 속성
const conversionText = computed(() => {
  if (convertedAmount.value !== null) {
    if (selectedTargetCountry.value) {
      // 변환 국가가 선택되었을 때 변환 결과를 텍스트로 구성
      const targetCountry = exchangeRates.value.find(rate => rate.cur_nm === selectedTargetCountry.value);
      const baseCountry = exchangeRates.value.find(rate => rate.cur_nm === selectedBaseCountry.value);
      return `${inputAmount.value} ${baseCountry.cur_unit} = ${convertedAmount.value} ${targetCountry.cur_unit}`;
    } else {
      // 변환 국가가 선택되지 않았을 때 변환 결과를 텍스트로 구성
      const baseCountry = exchangeRates.value.find(rate => rate.cur_nm === selectedBaseCountry.value);
      return ` ${inputAmount.value} ${baseCountry.cur_unit} = ${convertedAmount.value} 원`;
    }
  } else {
    // 변환된 금액이 없을 때 빈 문자열 반환
    return '';
  }
});

</script>

<style>
.exchange-calculator {
  max-width: 400px;
  margin: 50px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h3 {
  font-size: 24px;
  margin-bottom: 20px;
  text-align: center;
  color: #333;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
}

input[type="number"],
select {
  padding: 8px;
  width: 100%;
  border: 1px solid #ccc;
  border-radius: 3px;
  box-sizing: border-box;
}

input[type="number"]:focus,
select:focus {
  outline: none;
  border-color: #6b9ce3;
}

.converted-amount {
  font-size: 24px;
  font-weight: bold;
  color: #4caf50;
  text-align: center;
  margin-top: 20px;
}

.exchange-box-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}
</style>