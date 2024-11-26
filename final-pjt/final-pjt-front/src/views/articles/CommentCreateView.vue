<template>
  <div>
    <form @submit.prevent="createComment" class="comment-form">
      <div class="input-wrapper">
        <textarea v-model.trim="content" id="content" class="comment-input"></textarea>
        <input type="submit" value="작성" class="submit-button">
      </div>
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter, useRoute } from 'vue-router'

const route = useRoute()
const content = ref(null)
const store = useCounterStore()
const router = useRouter()
const article_id = route.params.id
const createComment = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/comments/`,
    data: {
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((response) => {
      console.log(response)
      store.getComments(article_id)
      router.push({ name: 'articleDetail' })
    })
    .catch((error) => {
      console.log(error)
    })
}

</script>

<style scoped>
.comment-form {
  display: flex;
}

.input-wrapper {
  display: flex;
}

.comment-input {
  width: 600px;
  height: 40px;
  padding: 10px;
  border: 2px solid #008485;
  border-radius: 5px;
  resize: none;
  margin-right: 10px; /* 입력창과 버튼 사이의 간격 조절 */
}

.submit-button {
  height: 40px; /* 입력창과 높이를 동일하게 설정 */
  background-color: #008485;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #005454;
}
</style>