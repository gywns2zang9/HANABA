<template>
  <div class="carousel-container">
    <Carousel :autoplay="2000" :wrap-around="true">
      <Slide v-for="(slide, index) in slides" :key="index">
        <div class="carousel__item">
          <router-link :to="{name: slide.routeName}">
            <img :src="slide.image" :alt="'Slide ' + (index + 1)" class="carousel-image"/>
          </router-link>
          <div class="carousel-caption">{{ slide.caption }}</div>
        </div>
      </Slide>

      <template #addons>
        <Pagination class="custom-pagination" />
      </template>
    </Carousel>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
import { Carousel, Pagination, Slide } from 'vue3-carousel'

import 'vue3-carousel/dist/carousel.css'

import image1 from '@/assets/main/main_slide_1.png'
import image2 from '@/assets/main/main_slide_2.jpg'
import image3 from '@/assets/main/main_slide_3.png'


export default defineComponent({
  name: 'Autoplay',
  components: {
    Carousel,
    Slide,
    Pagination,
  },
  data() {
    return {
      slides: [
        { image: image1, caption: '예적금!', routeName: 'product' },
        { image: image2, caption: '환율 궁금해?', routeName: 'exchange' },
        { image: image3, caption: '커뮤니티!', routeName: 'article' }
      ]
    }
  }
})
</script>


<style scoped>

.carousel-container {
  width: 80%;
  margin: 0 auto;
}

.carousel__item {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 300px;
  background-color: #f9fcfa; /* 배경색 설정 */
}

.carousel-image {
  max-width: 760px;
  max-height: 440px;
}

.carousel-caption {
  position: absolute;
  bottom: 120px; /* 조정 가능 */
  left: 30%;
  width: 200px;
  transform: translateX(-50%);
  background-color: #f9fcfa; /* 새로운 배경색 */
  color: #008485; /* 새로운 텍스트 색상 */
  padding: 10px 20px;
  border-radius: 8px;
  font-size: 24px; /* 텍스트 크기 증가 */
  font-weight: bold; /* 텍스트 굵게 설정 */
  font-family: 'Arial', sans-serif; /* 원하는 폰트 설정 */
  text-align: center;
  text-transform: uppercase; /* 텍스트 대문자로 변환 */
}

.carousel-container .carousel {
  background-color: #008485; /* 캐러셀 전체 배경색 설정 */
}

/* Pagination 커스터마이징 */
.custom-pagination {
  margin-top: 0 !important;
  background-color: white;
  padding: 10px; /* 필요한 경우 padding을 추가 */
  text-align: center; /* 페이지네이션 가운데 정렬 */
}

.custom-pagination .carousel__pagination-button {
  background-color: #ccc; /* 페이지네이션 버튼 배경색 */
  border-radius: 50%; /* 버튼 모양 둥글게 */
}

.custom-pagination .carousel__pagination-button--active {
  background-color: #008485; /* 활성화된 버튼 배경색 */
}
</style>