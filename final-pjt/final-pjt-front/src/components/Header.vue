<template>
  <div class="main">
    <div class="logo">
      <RouterLink :to="{name: 'home'}">
        <img src="@/assets/logo.jpeg">
      </RouterLink>
    </div>
    <div class="nav-links">
    <template v-if="store.isLogin === false">
      <RouterLink :to="{name: 'signup'}" class="nav-link">회원가입</RouterLink>
      <RouterLink :to="{name: 'login'}" class="nav-link">로그인</RouterLink>
    </template>
    <template v-if="store.isLogin === true">
      <RouterLink :to="{name: 'logout'}" class="nav-link">로그아웃</RouterLink>
      <RouterLink :to="{name: 'userInfo'}" class="nav-link">마이페이지</RouterLink>
    </template>
    </div>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()
</script>

<style scoped>
.main {
  background-color: rgb(253, 253, 253);
  padding: 10px; /* 상하 여백을 추가하여 요소 간의 간격을 늘립니다 */
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
}

.logo {
  margin-right: auto; /* 로고와 다른 요소 사이의 간격을 늘립니다 */
}

.logo img {
  height: 50px; /* 로고 이미지의 높이를 줄입니다 */
}
.nav-links {
  color: #008485;
}

.nav-link {
  color: inherit;
  text-decoration: none;
}

.nav-link:hover {
  text-decoration: underline;
}
</style>