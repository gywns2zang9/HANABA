<template>
  <div>
    <hr>
    <p>공시 제출월 : {{ option.dcls_month }}</p>
    <p>금융회사 코드 : {{ option.fin_co_no }}</p>
    <p>금융 상품 코드 : {{ option.fin_prdt_cd }}</p>
    <p>저축 금리 유형 : {{ option.intr_rate_type }}</p>
    <p>저축 금리 유형명 : {{ option.intr_rate_type_nm }}</p>
    <p>저축 기간 : {{ option.save_trm }}개월</p>
    <p>저축 금리 : {{ option.intr_rate }}%</p>
    <p>최고 우대금리 : {{ option.intr_rate2 }}%</p>
  </div>
</template>

<script setup>
defineProps({
  option: Object
})
</script>

<style scoped>

</style>