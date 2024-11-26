<template>
    <div>
      <h1>게시글 작성</h1>
      <form @submit.prevent="updateArticle">
        <div>
          <label for="title">제목 : </label>
          <input type="text" v-model.trim="title" id="title">
        </div>
        <div>
          <label for="content">내용 : </label>
          <textarea v-model.trim="content" id="content"></textarea>
        </div>
        <input type="submit">
      </form>
    </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useCounterStore } from '@/stores/counter'


const store = useCounterStore()
const route = useRoute();
const router = useRouter();

const title = ref('');
const content = ref('');


const article = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`
  })
  .then((response) => {
    article.value = response.data
    title.value = article.value.title
    content.value = article.value.content
  })
  .catch((error) => {
    console.log(error)
  })
})


const updateArticle = function () {
  axios({
    method: 'put',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((response) => {
      router.push({ name: 'article' })
    })
    .catch((error) => {
      console.log(error)
    })
}

</script>
