<template>
  <div class="container">
    <Main />
    <NavBottom />
    <Footer />
  </div>
</template>

<script setup>
import Main from '@/components/Main.vue';
import NavBottom from '@/components/NavBottom.vue';
import Footer from '@/components/Footer.vue';

</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}
</style>