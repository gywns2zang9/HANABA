<template>
  <div>
    <h3>Review</h3>
    <hr>
    <CommentListItem 
      v-for="comment in store.depositComments"
      :key="comment.id"
      :comment="comment"/>
  </div>
</template>

<script setup>
import CommentListItem from '@/components/articles/CommentListItem.vue'
import { useProductStore } from '@/stores/product';

const store = useProductStore()


</script>

<style scoped>

</style>