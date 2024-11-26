<template>
  <div class="comment-item">
    <div class="comment-user">{{ comment.user.name }}</div>
    <div class="comment-content">{{ comment.content }}</div>
  </div>
</template>

<script setup>
defineProps({
  comment: Object
})
</script>

<style scoped>
.comment-item {
  display: flex;
  flex-direction: column;
  margin-bottom: 15px;
  margin-left: 15px; /* 왼쪽에 마진 추가 */
}

.comment-user {
  font-weight: bold;
  color: #008485;
}

.comment-content {
  margin-top: 5px;
  margin-left: 10px;
}
</style>
