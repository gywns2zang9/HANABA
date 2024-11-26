<template>
  <div class="container">
    <nav class="nav-links">
      <RouterLink :to="{name:'deposit'}" class="nav-link" :class="{ 'active-link': $route.name === 'deposit' }">예금 상품 목록 보기</RouterLink>
      <RouterLink :to="{name:'saving'}" class="nav-link" :class="{ 'active-link': $route.name === 'saving' }">적금 상품 목록 보기</RouterLink>
    </nav>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router';
</script>

<style scoped>
.container {
  padding: 20px;
}

.nav-links {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.nav-link {
  padding: 10px 20px;
  border-radius: 5px;
  background-color: #008485;
  color: #fff;
  text-decoration: none;
  font-weight: bold;
  margin: 0 10px;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.nav-link:hover {
  background-color: #005454;
}

.active-link {
  background-color: #005454;
  color: #fff;
  font-weight: bold;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.3); /* 활성화된 링크에 그림자 효과 추가 */
}
</style>
