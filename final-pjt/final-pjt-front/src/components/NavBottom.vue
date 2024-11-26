<template>
  <div class="navbar-section">
    <nav>
      <RouterLink :to="{name: 'product'}" class="nav-link">금융상품</RouterLink> 
      <RouterLink :to="{name: 'exchange'}" class="nav-link">환율 계산기</RouterLink> 
      <RouterLink :to="{name: 'map'}" class="nav-link">지도</RouterLink> 
      <RouterLink :to="{name: 'article'}" class="nav-link">커뮤니티</RouterLink>
    </nav>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
.navbar-section {
  background-color: #d9dfdf; 
  padding: 35px 50px 20px; 
  height: 120px;
  margin: 50px;
}

nav {
  display: flex; 
  align-items: center; 
  justify-content: space-between; 
  font-size: 20px; 
}

.nav-link {
  color: white; 
  text-decoration: none; 
  padding: 10px 20px; 
  border-radius: 8px; 
  background-color: #d9dfdf; 
}

.nav-link:hover {
  text-decoration: underline;
}
</style>
