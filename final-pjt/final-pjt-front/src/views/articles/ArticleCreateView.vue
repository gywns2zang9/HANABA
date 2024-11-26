<template>
  <div>
    <h1 class="page-title">게시글 작성</h1>
    <form @submit.prevent="createArticle" class="article-form">
      <div class="form-group">
        <label for="title" class="label">제목 : </label>
        <input type="text" v-model.trim="title" id="title" class="input-field">
      </div>
      <div class="form-group">
        <label for="content" class="label">내용 : </label>
        <textarea v-model.trim="content" id="content" class="input-field"></textarea>
      </div>
      <button type="submit" class="submit-button">작성 완료</button>
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const title = ref(null)
const content = ref(null)

const store = useCounterStore()
const router = useRouter()

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((response) => {
      console.log('게시글 작성 완료!')
      router.push({ name: 'article' })
    })
    .catch((error) => {
      console.log(error)
    })
}

</script>

<style scoped>
.page-title {
  color: #008485;
}

.article-form {
  margin-top: 20px;
}

.form-group {
  margin-bottom: 15px;
}

.label {
  font-weight: bold;
  color: #008485;
}

.input-field {
  padding: 5px;
  width: 100%;
  border: 1px solid #008485;
  border-radius: 5px;
}

.submit-button {
  padding: 8px 16px;
  background-color: #008485;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #005e5e;
}
</style>