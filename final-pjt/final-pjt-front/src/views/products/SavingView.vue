<template>
  <div>
    <!-- 검색 입력 필드 -->
    <input class="input" type="text" :value="searchQuery" @input="updateSearchQuery($event.target.value)" placeholder="은행명 혹은 금융 상품명을 입력하세요" id="productName">
    <!-- 검색 버튼 -->
    <button class="search-button" @click="filterProducts">검색</button>
    <!-- 정렬 버튼 -->
    <button class="sort-button" @click="sortByProductJoins">가입자 순 정렬</button>
    <!-- 검색 결과 메시지 -->
    <div class="search-result-message">
      <p v-show="searchResultMessage !== ''">{{ searchResultMessage }}</p>
    </div>
    <!-- 적금 리스트 -->
    <div class="saving-list-item">
      <SavingList
      v-for="product in filteredSavingProducts"
      :key="product.fin_prdt_cd"
      :product="product"
      />
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, computed, watch } from 'vue';
import { useProductStore } from '@/stores/product';
import SavingList from '@/components/products/SavingList.vue';

import { useCounterStore } from '@/stores/counter';
const counterStore = useCounterStore()

const store = useProductStore();
const searchQuery = ref(''); // 사용자의 검색어를 저장하는 상태
const searchResultMessage = ref(''); // 검색 결과 메시지 상태
const savingProducts = store.savingProducts; // 전체 적금 리스트

onMounted(() => {
  store.getSaving(); // 페이지 로딩 시 적금 데이터 가져오기
  counterStore.getInfo()
});

// 검색된 적금 리스트를 계산된 속성으로 정의
const filteredSavingProducts = computed(() => {
  if (!searchQuery.value) {
    // 검색어가 없는 경우 전체 리스트 반환
    return savingProducts;
  } else {
    // 검색어가 있는 경우 검색 결과에 따라 리스트 반환
    const searchResult = savingProducts.filter(product => {
      return product.kor_co_nm.includes(searchQuery.value) || product.fin_prdt_nm.includes(searchQuery.value);
    });
    return searchResult;
  }
});

// 검색어 업데이트 메소드
const updateSearchQuery = (value) => {
  searchQuery.value = value;
};

// 검색 버튼 클릭 시 동작하는 메소드
const filterProducts = () => {
  // 검색어가 없으면 메시지를 비움
  if (!searchQuery.value) {
    searchResultMessage.value = '';
  }
};

// 필터링된 결과가 변경될 때마다 검색 결과 메시지를 업데이트
watch(filteredSavingProducts, (newValue) => {
  const searchCount = newValue.length;
  searchResultMessage.value = `${searchCount} 개의 검색 결과입니다.`;
});

// 정렬 방향을 추적하는 상태 추가
const sortDirection = ref('desc'); // 초기값: 내림

// 정렬 버튼 클릭 시 동작하는 메소드
const sortByProductJoins = () => {
  // 정렬 방향에 따라 다르게 정렬
  if (sortDirection.value === 'asc') {
    // 오름차순 정렬
    filteredSavingProducts.value.sort((a, b) => {
      return a.productJoins - b.productJoins;
    });
    // 정렬 방향 변경
    sortDirection.value = 'desc';
  } else {
    // 내림차순 정렬
    filteredSavingProducts.value.sort((a, b) => {
      return b.productJoins - a.productJoins;
    });
    // 정렬 방향 변경
    sortDirection.value = 'asc';
  }
};
</script>

<style scoped>
.input {
  width: 250px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-right: 10px;
}

.search-button,
.sort-button {
  padding: 10px 20px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-right: 10px;
}

.search-button:hover,
.sort-button:hover {
  background-color: #45a049;
}
.saving-list-item {
  margin-top: 30px;
}
.search-result-message {
  margin-top: 10px;
}
</style>
