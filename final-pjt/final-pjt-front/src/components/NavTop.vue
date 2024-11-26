<template>
  <div class="nav-top">
    <b-nav>
      <b-nav-item><RouterLink :to="{name: 'home'}" class="nav-link">하나바 홈</RouterLink></b-nav-item>
      <b-nav-item><RouterLink :to="{name: 'product'}" class="nav-link">금융상품</RouterLink></b-nav-item>
      <b-nav-item><RouterLink :to="{name: 'exchange'}" class="nav-link">환율 계산기</RouterLink></b-nav-item>
      <b-nav-item><RouterLink :to="{name: 'map'}" class="nav-link">지도</RouterLink></b-nav-item>
      <b-nav-item><RouterLink :to="{name: 'article'}" class="nav-link">커뮤니티</RouterLink></b-nav-item>
    </b-nav>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
.nav-top {
  display: flex;
  justify-content: center;
  font-size: 20px;
}

.nav-link {
  color: #008485;
  text-decoration: none;
  padding: 5px 15px;
}

.nav-link:hover {
  background-color: #008485;
  color: #fff;
  border-radius: 5px;
}
</style>
