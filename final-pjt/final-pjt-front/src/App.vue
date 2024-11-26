<template>
    <Header />
    <NavTop />
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/counter';
import Header from '@/components/Header.vue';
import NavTop from '@/components/NavTop.vue';

const store = useCounterStore()
</script>

<style scoped>
</style>
