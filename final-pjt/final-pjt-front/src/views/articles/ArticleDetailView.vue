<template>
  <div>
    <div v-if="article" class="article-container">
      <p>글 번호 : {{ article.id }}</p>
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
      <p>작성 시간 : {{ formatDate(article.created_at) }}</p>
      <p>수정 시간 : {{ formatDate(article.updated_at) }}</p>
      <button @click="deleteArticle(article.id)" class="delete-button">DELETE</button>
      <RouterLink :to="{name: 'articleUpdate', params: {id: article.id }}" class="update-link">수정하기</RouterLink>
    </div>
    <CommentList />
    <hr class="comment-divider">
    <RouterLink :to="{name: 'comment'}" class="create-link">댓글 작성</RouterLink>
    <RouterView />
  </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRoute, useRouter, RouterLink, RouterView } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
import CommentList from '@/components/articles/CommentList.vue';

const store = useCounterStore()
const route = useRoute()
const article = ref(null)
onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`
  })
  .then((response) => {
    article.value = response.data
    store.getComments(article.value.id)
  })
  .catch((error) => {
    console.log(error)
  })
})

const router = useRouter()
const deleteArticle = function(id) {
  axios({
    method: 'delete',
    url: `${store.API_URL}/api/v1/articles/${id}/`
  })
  .then((response) => {
    console.log('게시글 삭제 성공')
    store.getArticles()
    router.push({name: 'article'})
  })
  .catch((response) => {
    console.log(error)
  })
}

const formatDate = (dateString) => {
  const date = new Date(dateString);
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0'); // 월은 0부터 시작하므로 +1 해주고, 두 자리로 표시
  const day = String(date.getDate()).padStart(2, '0'); // 일자를 두 자리로 표시
  const hours = String(date.getHours()).padStart(2, '0'); // 시간을 두 자리로 표시
  const minutes = String(date.getMinutes()).padStart(2, '0'); // 분을 두 자리로 표시
  return `${year}년 ${month}월 ${day}일 ${hours}시 ${minutes}분`;
};
</script>

<style scoped>
.article-container {
  padding: 20px;
  border: 2px solid #008485; /* 하나은행 메인 컬러 */
  border-radius: 5px;
  margin-bottom: 20px;
}

.delete-button {
  background-color: #008485; /* 하나은행 메인 컬러 */
  color: #fff; /* 글자색을 흰색으로 설정 */
  border: none;
  padding: 5px 10px;
  border-radius: 3px;
  cursor: pointer;
}

.delete-button:hover {
  background-color: #005454; /* 버튼에 호버 시 어둡게 변경 */
}

.update-link {
  color: #008485; /* 하나은행 메인 컬러 */
  text-decoration: none;
  margin-left: 10px;
}

.create-link {
  color: #008485; /* 하나은행 메인 컬러 */
  text-decoration: none;
  margin-left: 10px;
}
.comment-divider {
  border-color: #008485; /* 메인 컬러로 설정 */
  margin: 10px; /* 수평선 아래쪽 마진 추가 */
}
</style>
