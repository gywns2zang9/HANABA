<template>
  <div class="container">
    <RouterLink :to="{name: 'articleDetail', params: {id: article.id }}" class="title">
      <p class="title-text">제목: {{ article.title }}</p>
    </RouterLink>
    <p class="author">작성자 : {{ article.user.name }}</p>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
defineProps({
  article: Object
})
</script>

<style scoped>
.container {
  padding: 20px;
  border: 2px solid #008485; /* 하나은행 메인 컬러 */
  border-radius: 5px;
  margin-bottom: 20px;
}

.title {
  text-decoration: none;
  color: #333; /* 제목의 글자색 */
}

.title:hover {
  text-decoration: underline;
}

.title-text {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 10px;
}

.author {
  font-size: 14px;
  color: #666; /* 작성자 정보의 글자색 */
}
</style>
