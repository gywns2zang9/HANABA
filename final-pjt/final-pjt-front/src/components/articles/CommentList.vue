<template>
  <div>
    <h5 class="comment-title">댓글 목록</h5>
    <hr class="comment-divider">
    <template v-if="store.comments.length > 0">
      <CommentListItem 
        v-for="comment in store.comments"
        :key="comment.id"
        :comment="comment"/>
    </template>
    <template v-else>
      <p class="no-comments">아직 댓글이 없습니다.</p>
    </template>
  </div>
</template>

<script setup>
import CommentListItem from '@/components/articles/CommentListItem.vue'
import { useCounterStore } from '@/stores/counter';
const store = useCounterStore()
</script>

<style scoped>
.comment-title {
  color: #008485; /* 메인 컬러로 설정 */
  margin: 10px; /* 아래쪽 마진 추가 */
}

.comment-divider {
  border-color: #008485; /* 메인 컬러로 설정 */
  margin: 10px; /* 수평선 아래쪽 마진 추가 */
}

.no-comments {
  color: #666; /* 회색으로 설정 */
  margin: 15px; /* 상하좌우 여백 추가 */
}
</style>
