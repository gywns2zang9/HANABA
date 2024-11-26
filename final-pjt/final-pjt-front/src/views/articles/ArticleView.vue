<template>
  <div>
    <div class="navbar">
      <div class="nav-links">
        <RouterLink to="" class="nav-link">전체 게시판</RouterLink>
        <RouterLink to="" class="nav-link">질문 게시판</RouterLink>
        <RouterLink to="" class="nav-link">비밀 게시판</RouterLink>
        <RouterLink to="" class="nav-link">거지방</RouterLink>
        <RouterLink to="" class="nav-link">플랙스방</RouterLink>
      </div>
      <div class="nav-buttons">
        <button class="search-button" @click="toggleSearch">검색</button>
        <button class="create-button" @click="goToCreatePage">글쓰기</button>
      </div>
    </div>
    <hr>
    <div class="container">
      <ArticleList />
    </div>
    <div class="search-container" v-show="isSearchVisible">
      <!-- 여기에 검색 입력 필드와 검색 버튼을 넣어주세요 -->
      <input type="text" placeholder="검색어를 입력하세요" v-model="searchQuery">
      <button @click="search">검색</button>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { RouterLink } from 'vue-router';
import ArticleList from '@/components/articles/ArticleList.vue';
import { useRouter } from 'vue-router'

const store = useCounterStore();
const isSearchVisible = ref(false);
const searchQuery = ref('');

onMounted(()=>{
  store.getArticles();
})


const router = useRouter()
const goToCreatePage = () => {
  router.push({ name: 'articleCreate' });
}

const toggleSearch = () => {
  isSearchVisible.value = !isSearchVisible.value;
}

const search = () => {
  // 검색 기능을 구현하세요.
}
</script>

<style scoped>
/* 네비게이션 바 스타일 */
.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px;
  background-color: #008485;
}

/* 네비게이션 링크 스타일 */
.nav-links {
  display: flex;
}

.nav-link {
  margin-right: 20px;
  color: #fff;
  text-decoration: none;
}

.nav-link:hover {
  text-decoration: underline;
}

/* 네비게이션 버튼 스타일 */
.nav-buttons {
  display: flex;
  gap: 10px; /* 버튼 간격 설정 */
}

.create-button, .search-button {
  color: #fff;
  text-decoration: none;
  font-weight: bold;
  padding: 8px 16px;
  border-radius: 5px;
  background-color: #005454;
  transition: background-color 0.3s ease;
  border: none;
  cursor: pointer;
}

.create-button:hover, .search-button:hover {
  background-color: #008485;
}

/* 검색 컨테이너 스타일 */
.search-container {
  margin-top: 10px;
  display: flex;
  align-items: center;
}

.search-container input {
  padding: 8px;
  border-radius: 5px;
  border: 1px solid #ccc;
  margin-right: 8px;
}

.search-container button {
  padding: 8px 16px;
  border-radius: 5px;
  background-color: #005454;
  color: #fff;
  border: none;
  cursor: pointer;
}

.search-container button:hover {
  background-color: #008485;
}

/* 컨테이너 스타일 */
.container {
  margin-top: 20px;
}
</style>
