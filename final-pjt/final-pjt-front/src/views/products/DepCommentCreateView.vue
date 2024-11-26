<template>
  <div>
    <h1>후기 작성</h1>
    <form @submit.prevent="createComment">
      <div>
        <label for="content">댓글 : </label>
        <textarea v-model.trim="content" id="content"></textarea>
      </div>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useProductStore } from '@/stores/product';

import { useRouter, useRoute } from 'vue-router'

const route = useRoute()
const content = ref(null)
const store = useCounterStore()
const productStore = useProductStore()
const router = useRouter()
const product_id = route.params.product_id


const createComment = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/deposit/${product_id}/comments/`,
    data: {
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((response) => {
      console.log(response)
      productStore.getDepositComments(product_id)
      router.push({ name: 'depositDetail' })
    })
    .catch((error) => {
      console.log(error)
    })
}

</script>

<style scoped>

</style>