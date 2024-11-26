<template>
  <div class="container">
    <ArticleListItem 
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
      class="item"/>
  </div>
</template>

<script setup>
import ArticleListItem from '@/components/articles/ArticleListItem.vue';
import { useCounterStore } from '@/stores/counter';
const store = useCounterStore()
</script>

<style scoped>
.container {
  max-width: 1000px; /* 최대 너비 설정 */
  margin: 0 auto; /* 가운데 정렬 */
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); /* 자동으로 컬럼을 채우고 최소 250px 너비로 설정 */
  gap: 20px; /* 그리드 아이템 간격 */
}

.item {
  border: 1px solid #008485; /* 하나은행 메인 컬러로 테두리 설정 */
  padding: 20px; /* 내부 여백 설정 */
}
</style>
