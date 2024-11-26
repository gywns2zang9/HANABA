<template>
  <!-- 지도 및 선택 옵션 표시 -->
  <div>
    <div class="options-container">
      <!-- 시/도 선택 드롭다운 -->
      <label for="city" class="option-label">시/도 선택 </label>
      <select id="city" v-model="selectedCity" @change="onCityChange" class="option-select">
        <option v-for="city in cities" :key="city.name" :value="city.name">{{ city.name }}</option>
      </select>

      <!-- 시/군/구 선택 드롭다운 -->
      <label for="district" class="option-label">시/군/구 선택</label>
      <select id="district" v-model="selectedDistrict" @change="updateMapCenterAndSearch" class="option-select">
        <option v-if="!selectedCity" disabled>시/도를 먼저 선택해주세요</option>
        <option v-for="district in filteredDistricts" :key="district" :value="district">{{ district }}</option>
      </select>
      
      <!-- 은행 선택 드롭다운 -->
      <label for="bank" class="option-label">은행 선택</label>
      <select id="bank" v-model="selectedBank" @change="onBankChange" class="option-select">
        <option value="" @click=""> 근처 은행 보기 </option>
        <option v-for="bank in banks" :key="bank" :value="bank">{{ bank }}</option>
      </select>
    </div>
    <KakaoMap :lat="mapCenter.lat" :lng="mapCenter.lng" @onLoadKakaoMap="onLoadKakaoMap" class="kakao-map" width="700px" height="500px" >
      <KakaoMapMarker
        v-for="(marker, index) in markers"
        :key="index"
        :lat="marker.lat"
        :lng="marker.lng"
        :infoWindow="marker.infoWindow"
        :clickable="true"
        @onClickKakaoMapMarker="onClickMapMarker(marker)"
      />
    </KakaoMap>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { KakaoMap, KakaoMapMarker } from 'vue3-kakao-maps';

const cities = ref([
  { name: '서울특별시', districts: ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구'] },
  { name: '부산광역시', districts: ['강서구', '금정구', '기장군', '남구', '동구', '동래구', '부산진구', '북구', '사상구', '사하구', '서구', '수영구', '연제구', '영도구', '중구', '해운대구'] },
  { name: '대구광역시', districts: ['남구', '달서구', '달성군', '동구', '북구', '서구', '수성구', '중구'] },
  { name: '인천광역시', districts: ['강화군', '계양구', '미추홀구', '남동구', '동구', '부평구', '서구', '연수구', '옹진군', '중구'] },
  { name: '광주광역시', districts: ['광산구', '남구', '동구', '북구', '서구'] },
  { name: '대전광역시', districts: ['대덕구', '동구', '서구', '유성구', '중구'] },
  { name: '울산광역시', districts: ['남구', '동구', '북구', '울주군', '중구'] },
  { name: '세종특별자치시', districts: ['조치원읍', '연기면', '연동면', '부강면', '금남면', '장군면', '연서면', '전의면', '전동면', '소정면'] },
  { name: '경기도', districts: ['수원시', '성남시', '의정부시', '안양시', '부천시', '광명시', '평택시', '동두천시', '안산시', '고양시', '과천시', '구리시', '남양주시', '오산시', '시흥시', '군포시', '의왕시', '하남시', '용인시', '파주시', '이천시', '안성시', '김포시', '화성시', '광주시', '양주시', '포천시', '여주시'] },
  { name: '강원도', districts: ['춘천시', '원주시', '강릉시', '동해시', '태백시', '속초시', '삼척시', '홍천군', '횡성군', '영월군', '평창군', '정선군', '철원군', '화천군', '양구군', '인제군', '고성군', '양양군'] },
  { name: '충청북도', districts: ['청주시', '충주시', '제천시', '보은군', '옥천군', '영동군', '증평군', '진천군', '괴산군', '음성군', '단양군'] },
  { name: '충청남도', districts: ['천안시', '공주시', '보령시', '아산시', '서산시', '논산시', '계룡시', '당진시', '금산군', '부여군', '서천군', '청양군', '홍성군', '예산군', '태안군'] },
  { name: '전라북도', districts: ['전주시', '군산시', '익산시', '정읍시', '남원시', '김제시', '완주군', '진안군', '무주군', '장수군', '임실군', '순창군', '고창군', '부안군'] },
  { name: '전라남도', districts: ['목포시', '여수시', '순천시', '나주시', '광양시', '담양군', '곡성군', '구례군', '고흥군', '보성군', '화순군', '장흥군', '강진군', '해남군', '영암군', '무안군', '함평군', '영광군', '장성군', '완도군', '진도군', '신안군'] },
  { name: '경상북도', districts: ['포항시', '경주시', '김천시', '안동시', '구미시', '영주시', '영천시', '상주시', '문경시', '경산시', '군위군', '의성군', '청송군', '영양군', '영덕군', '청도군', '고령군', '성주군', '칠곡군', '예천군', '봉화군', '울진군', '울릉군'] },
  { name: '경상남도', districts: ['창원시', '진주시', '통영시', '사천시', '김해시', '밀양시', '거제시', '양산시', '의령군', '함안군', '창녕군', '고성군', '남해군', '하동군', '산청군', '함양군', '거창군', '합천군'] },
  { name: '제주특별자치도', districts: ['제주시', '서귀포시'] }
]);

const selectedCity = ref(cities.value[0].name);
const selectedDistrict = ref('');
const selectedBank = ref('');
const map = ref(null);
const infoWindow = ref(null);
const markers = ref([]);
const banks = ref([
  '국민은행', '신한은행', '우리은행', 'KEB하나은행', 'SC제일은행', '외환은행', '한국시티은행',
  '경남은행', '광주은행', '대구은행', '부산은행', '전북은행', '제주은행',
  '기업은행', '농협', '수협', '한국산업은행', '한국수출입은행'
]);

// 선택된 시/도에 따라 시/군/구를 필터링하는 계산된 속성
const filteredDistricts = computed(() => {
  const city = cities.value.find(city => city.name === selectedCity.value);
  return city ? city.districts : [];
});

// 시/도와 시/군/구의 좌표 정보
const coordinates = {
  '서울특별시': {
    '강남구': { lat: 37.5172, lng: 127.0473 },
    '강동구': { lat: 37.5301, lng: 127.1238 },
    '강북구': { lat: 37.6396, lng: 127.0255 },
    '강서구': { lat: 37.5509, lng: 126.8495 },
    '관악구': { lat: 37.4784, lng: 126.9516 },
    '광진구': { lat: 37.5384, lng: 127.0823 },
    '구로구': { lat: 37.4955, lng: 126.8875 },
    '금천구': { lat: 37.4569, lng: 126.8957 },
    '노원구': { lat: 37.6544, lng: 127.0561 },
    '도봉구': { lat: 37.6688, lng: 127.0479 },
    '동대문구': { lat: 37.5743, lng: 127.0397 },
    '동작구': { lat: 37.5124, lng: 126.9395 },
    '마포구': { lat: 37.5663, lng: 126.9011 },
    '서대문구': { lat: 37.5791, lng: 126.9368 },
    '서초구': { lat: 37.4836, lng: 127.0327 },
    '성동구': { lat: 37.5633, lng: 127.0364 },
    '성북구': { lat: 37.5894, lng: 127.0164 },
    '송파구': { lat: 37.5145, lng: 127.1065 },
    '양천구': { lat: 37.5169, lng: 126.8665 },
    '영등포구': { lat: 37.5262, lng: 126.8963 },
    '용산구': { lat: 37.5326, lng: 126.9905 },
    '은평구': { lat: 37.6176, lng: 126.9227 },
    '종로구': { lat: 37.5735, lng: 126.9790 },
    '중구': { lat: 37.5636, lng: 126.9976 },
    '중랑구': { lat: 37.6063, lng: 127.0920 },
  },
  '부산광역시': {
      '강서구': { lat: 35.2123, lng: 128.9806 },
      '금정구': { lat: 35.2427, lng: 129.0922 },
      '기장군': { lat: 35.2444, lng: 129.2220 },
      '남구': { lat: 35.1365, lng: 129.0849 },
      '동구': { lat: 35.1293, lng: 129.0450 },
      '동래구': { lat: 35.2042, lng: 129.0837 },
      '부산진구': { lat: 35.1624, lng: 129.0530 },
      '북구': { lat: 35.1973, lng: 128.9905 },
      '사상구': { lat: 35.1470, lng: 128.9902 },
      '사하구': { lat: 35.1046, lng: 128.9661 },
      '서구': { lat: 35.0965, lng: 129.0241 },
      '수영구': { lat: 35.1427, lng: 129.1131 },
      '연제구': { lat: 35.1859, lng: 129.0794 },
      '영도구': { lat: 35.0910, lng: 129.0687 },
      '중구': { lat: 35.1066, lng: 129.0332 },
      '해운대구': { lat: 35.1587, lng: 129.1604 },
    },
    '대구광역시': {
      '남구': { lat: 35.8453, lng: 128.6014 },
      '달서구': { lat: 35.8297, lng: 128.5329 },
      '달성군': { lat: 35.7746, lng: 128.4310 },
      '동구': { lat: 35.8831, lng: 128.6286 },
      '북구': { lat: 35.8854, lng: 128.5824 },
      '서구': { lat: 35.8717, lng: 128.5594 },
      '수성구': { lat: 35.8585, lng: 128.6300 },
      '중구': { lat: 35.8693, lng: 128.5940 },
    },
    '인천광역시': {
      '강화군': { lat: 37.7464, lng: 126.4876 },
      '계양구': { lat: 37.5384, lng: 126.7367 },
      '미추홀구': { lat: 37.4636, lng: 126.6505 },
      '남동구': { lat: 37.4473, lng: 126.7316 },
      '동구': { lat: 37.4736, lng: 126.6424 },
      '부평구': { lat: 37.5067, lng: 126.7218 },
      '서구': { lat: 37.5454, lng: 126.6752 },
      '연수구': { lat: 37.4103, lng: 126.6788 },
      '옹진군': { lat: 37.4480, lng: 126.6145 },
      '중구': { lat: 37.4736, lng: 126.6212 },
    },
    '광주광역시': {
      '광산구': { lat: 35.1396, lng: 126.7914 },
      '남구': { lat: 35.0039, lng: 126.8395 },
      '동구': { lat: 35.1449, lng: 126.9236 },
      '북구': { lat: 35.1741, lng: 126.9157 },
      '서구': { lat: 35.1515, lng: 126.8904 },
    },
    '대전광역시': {
      '대덕구': { lat: 36.3733, lng: 127.4311 },
      '동구': { lat: 36.3252, lng: 127.4545 },
      '서구': { lat: 36.3529, lng: 127.3849 },
      '유성구': { lat: 36.3626, lng: 127.3568 },
      '중구': { lat: 36.3255, lng: 127.4180 },
    },
    '울산광역시': {
      '남구': { lat: 35.5419, lng: 129.3309 },
      '동구': { lat: 35.5057, lng: 129.4164 },
      '북구': { lat: 35.5821, lng: 129.3615 },
      '울주군': { lat: 35.5664, lng: 129.2426 },
      '중구': { lat: 35.5680, lng: 129.3328 },
    },
    '세종특별자치시': {
      '조치원읍': { lat: 36.6046, lng: 127.2961 },
      '연기면': { lat: 36.5826, lng: 127.2908 },
      '연동면': { lat: 36.6896, lng: 127.2905 },
      '부강면': { lat: 36.5631, lng: 127.3808 },
      '금남면': { lat: 36.4707, lng: 127.2615 },
      '장군면': { lat: 36.5157, lng: 127.2102 },
      '연서면': { lat: 36.6081, lng: 127.2021 },
      '전의면': { lat: 36.6707, lng: 127.1856 },
      '전동면': { lat: 36.5985, lng: 127.1528 },
      '소정면': { lat: 36.7184, lng: 127.1128 },
    },
    '경기도': {
      '수원시': { lat: 37.2636, lng: 127.0286 },
      '성남시': { lat: 37.4200, lng: 127.1265 },
      '의정부시': { lat: 37.7381, lng: 127.0338 },
      '안양시': { lat: 37.3943, lng: 126.9568 },
      '부천시': { lat: 37.5036, lng: 126.7660 },
      '광명시': { lat: 37.4780, lng: 126.8643 },
      '평택시': { lat: 36.9921, lng: 127.1129 },
      '동두천시': { lat: 37.9034, lng: 127.0603 },
      '안산시': { lat: 37.3218, lng: 126.8309 },
      '고양시': { lat: 37.6584, lng: 126.8324 },
      '과천시': { lat: 37.4331, lng: 126.9960 },
      '구리시': { lat: 37.5929, lng: 127.1296 },
      '남양주시': { lat: 37.6355, lng: 127.2166 },
      '오산시': { lat: 37.1499, lng: 127.0775 },
      '시흥시': { lat: 37.3808, lng: 126.8000 },
      '군포시': { lat: 37.3604, lng: 126.9330 },
      '의왕시': { lat: 37.3445, lng: 126.9707 },
      '하남시': { lat: 37.5404, lng: 127.2166 },
      '용인시': { lat: 37.2411, lng: 127.1775 },
      '파주시': { lat: 37.7599, lng: 126.7969 },
      '이천시': { lat: 37.2722, lng: 127.4350 },
      '안성시': { lat: 37.0107, lng: 127.2797 },
      '김포시': { lat: 37.6153, lng: 126.7156 },
      '화성시': { lat: 37.1995, lng: 126.8312 },
      '광주시': { lat: 37.4365, lng: 127.2576 },
      '양주시': { lat: 37.7741, lng: 127.0452 },
      '포천시': { lat: 37.8941, lng: 127.2004 },
      '여주시': { lat: 37.2959, lng: 127.6303 },
    },
    '강원도': {
      '춘천시': { lat: 37.8858, lng: 127.7341 },
      '원주시': { lat: 37.3442, lng: 127.9499 },
      '강릉시': { lat: 37.7519, lng: 128.8763 },
      '동해시': { lat: 37.5209, lng: 129.1163 },
      '태백시': { lat: 37.1631, lng: 128.9906 },
      '속초시': { lat: 38.2044, lng: 128.5911 },
      '삼척시': { lat: 37.4440, lng: 129.1688 },
      '홍천군': { lat: 37.6985, lng: 127.8896 },
      '횡성군': { lat: 37.4812, lng: 127.9856 },
      '영월군': { lat: 37.1840, lng: 128.4676 },
      '평창군': { lat: 37.3705, lng: 128.3907 },
      '정선군': { lat: 37.3726, lng: 128.6609 },
      '철원군': { lat: 38.1468, lng: 127.3042 },
      '화천군': { lat: 38.1069, lng: 127.7047 },
      '양구군': { lat: 38.1050, lng: 127.9907 },
      '인제군': { lat: 38.0700, lng: 128.1706 },
      '고성군': { lat: 38.3805, lng: 128.4675 },
      '양양군': { lat: 38.0745, lng: 128.6286 },
    },
    '충청북도': {
      '청주시': { lat: 36.6361, lng: 127.4892 },
      '충주시': { lat: 36.9755, lng: 127.9283 },
      '제천시': { lat: 37.1320, lng: 128.2093 },
      '보은군': { lat: 36.4879, lng: 127.7762 },
      '옥천군': { lat: 36.3081, lng: 127.5705 },
      '영동군': { lat: 36.1768, lng: 127.7815 },
      '증평군': { lat: 36.7881, lng: 127.5849 },
      '진천군': { lat: 36.8552, lng: 127.4342 },
      '괴산군': { lat: 36.8161, lng: 127.7957 },
      '음성군': { lat: 36.9412, lng: 127.6898 },
      '단양군': { lat: 36.9948, lng: 128.3780 },
    },
    '충청남도': {
      '천안시': { lat: 36.8151, lng: 127.1135 },
      '공주시': { lat: 36.4548, lng: 127.1218 },
      '보령시': { lat: 36.3496, lng: 126.5923 },
      '아산시': { lat: 36.7920, lng: 127.0045 },
      '서산시': { lat: 36.7847, lng: 126.4521 },
      '논산시': { lat: 36.2014, lng: 127.1098 },
      '계룡시': { lat: 36.2759, lng: 127.2390 },
      '당진시': { lat: 37.0524, lng: 126.7952 },
      '금산군': { lat: 36.1068, lng: 127.4873 },
      '부여군': { lat: 36.2720, lng: 126.9082 },
      '서천군': { lat: 36.0809, lng: 126.6845 },
      '청양군': { lat: 36.4439, lng: 126.7934 },
      '홍성군': { lat: 36.5982, lng: 126.6704 },
      '예산군': { lat: 36.6807, lng: 126.8390 },
      '태안군': { lat: 36.7468, lng: 126.2934 },
    },
    '전라북도': {
      '전주시': { lat: 35.8242, lng: 127.1479 },
      '군산시': { lat: 35.9657, lng: 126.7111 },
      '익산시': { lat: 35.9402, lng: 126.9545 },
      '정읍시': { lat: 35.5693, lng: 126.8501 },
      '남원시': { lat: 35.4109, lng: 127.3902 },
      '김제시': { lat: 35.8123, lng: 126.8885 },
      '완주군': { lat: 35.8159, lng: 127.1315 },
      '진안군': { lat: 35.7978, lng: 127.4228 },
      '무주군': { lat: 36.0010, lng: 127.6620 },
      '장수군': { lat: 35.6717, lng: 127.5204 },
      '임실군': { lat: 35.6055, lng: 127.2872 },
      '순창군': { lat: 35.3766, lng: 127.1378 },
      '고창군': { lat: 35.4357, lng: 126.7033 },
      '부안군': { lat: 35.7295, lng: 126.7352 },
    },
    '전라남도': {
      '목포시': { lat: 34.8128, lng: 126.3922 },
      '여수시': { lat: 34.7445, lng: 127.7266 },
      '순천시': { lat: 34.9511, lng: 127.4888 },
      '나주시': { lat: 35.0107, lng: 126.7195 },
      '광양시': { lat: 34.9434, lng: 127.6961 },
      '담양군': { lat: 35.3197, lng: 126.9855 },
      '곡성군': { lat: 35.2783, lng: 127.2951 },
      '구례군': { lat: 35.2081, lng: 127.4698 },
      '고흥군': { lat: 34.5991, lng: 127.2901 },
      '보성군': { lat: 34.7782, lng: 127.1332 },
      '화순군': { lat: 35.0632, lng: 127.0055 },
      '장흥군': { lat: 34.6813, lng: 126.9163 },
      '강진군': { lat: 34.6335, lng: 126.7685 },
      '해남군': { lat: 34.5703, lng: 126.5985 },
      '영암군': { lat: 34.7967, lng: 126.6850 },
      '무안군': { lat: 34.9909, lng: 126.4654 },
      '함평군': { lat: 35.0735, lng: 126.5169 },
      '영광군': { lat: 35.2784, lng: 126.5051 },
      '장성군': { lat: 35.3066, lng: 126.7804 },
      '완도군': { lat: 34.3114, lng: 126.7325 },
      '진도군': { lat: 34.4804, lng: 126.2891 },
      '신안군': { lat: 34.8262, lng: 126.3696 },
    },
    '경상북도': {
      '포항시': { lat: 36.0188, lng: 129.3410 },
      '경주시': { lat: 35.8566, lng: 129.2242 },
      '김천시': { lat: 36.1397, lng: 128.1141 },
      '안동시': { lat: 36.5685, lng: 128.7295 },
      '구미시': { lat: 36.1196, lng: 128.3446 },
      '영주시': { lat: 36.8277, lng: 128.6260 },
      '영천시': { lat: 35.9772, lng: 128.9517 },
      '상주시': { lat: 36.4153, lng: 128.1563 },
      '문경시': { lat: 36.5889, lng: 128.1977 },
      '경산시': { lat: 35.8231, lng: 128.7371 },
      '군위군': { lat: 36.2386, lng: 128.5627 },
      '의성군': { lat: 36.3556, lng: 128.6851 },
      '청송군': { lat: 36.3487, lng: 129.0554 },
      '영양군': { lat: 36.6547, lng: 129.1225 },
      '영덕군': { lat: 36.4160, lng: 129.3882 },
      '청도군': { lat: 35.6428, lng: 128.7198 },
      '고령군': { lat: 35.7233, lng: 128.2538 },
      '성주군': { lat: 35.9193, lng: 128.2908 },
      '칠곡군': { lat: 35.9708, lng: 128.4514 },
      '예천군': { lat: 36.6481, lng: 128.4570 },
      '봉화군': { lat: 36.8955, lng: 128.7368 },
      '울진군': { lat: 36.9941, lng: 129.3994 },
      '울릉군': { lat: 37.4805, lng: 130.8906 },
    },
    '경상남도': {
      '창원시': { lat: 35.2276, lng: 128.6811 },
      '진주시': { lat: 35.1798, lng: 128.1076 },
      '통영시': { lat: 34.8554, lng: 128.4262 },
      '사천시': { lat: 35.0728, lng: 128.0865 },
      '김해시': { lat: 35.2341, lng: 128.8811 },
      '밀양시': { lat: 35.4914, lng: 128.7518 },
      '거제시': { lat: 34.8882, lng: 128.6213 },
      '양산시': { lat: 35.3382, lng: 129.0263 },
      '의령군': { lat: 35.3201, lng: 128.2921 },
      '함안군': { lat: 35.2798, lng: 128.4092 },
      '창녕군': { lat: 35.5419, lng: 128.4992 },
      '고성군': { lat: 34.9760, lng: 128.3233 },
      '남해군': { lat: 34.8396, lng: 127.9245 },
      '하동군': { lat: 35.1143, lng: 127.7510 },
      '산청군': { lat: 35.4150, lng: 127.8805 },
      '함양군': { lat: 35.5219, lng: 127.7360 },
      '거창군': { lat: 35.6869, lng: 127.9094 },
      '합천군': { lat: 35.5665, lng: 128.1690 },
    },
    '제주특별자치도': {
      '제주시': { lat: 33.4996, lng: 126.5312 },
      '서귀포시': { lat: 33.2507, lng: 126.5635 },
    },
};

// 맵 중심 좌표
const mapCenter = ref({ lat: 37.566826, lng: 126.9786567 });

// 시/도 변경 시 호출되는 함수
const onCityChange = () => {
  // 시/도 변경 시 시/군/구 드롭다운을 초기화합니다.
  selectedDistrict.value = '';
  // 시/도에 따른 중심 좌표 변경
  updateMapCenterAndSearch();
};

// 시/군/구 선택 시 호출되는 함수
const updateMapCenterAndSearch = () => {
  const selectedCityCoordinates = coordinates[selectedCity.value];
  if (selectedCityCoordinates && selectedDistrict.value) {
    mapCenter.value = selectedCityCoordinates[selectedDistrict.value];
    // 시/군/구가 선택되면 은행 키워드로 검색
    searchAllBanks();
  }
  // 시/군/구 변경 시 은행 선택 초기화
  selectedBank.value = '';
};

// 은행 선택 시 호출되는 함수
const onBankChange = () => {
  if (selectedBank.value) {
    // 은행 선택에 따라 은행 키워드로 검색
    searchNearbyBanks(selectedBank.value);
  }
};

// 은행 전체 검색 함수
const searchAllBanks = () => {
  if (selectedDistrict.value && selectedCity.value) {
    // 시/도, 시/군/구에 따라 은행 주변 검색 수행
    const ps = new kakao.maps.services.Places();
    ps.keywordSearch( selectedCity.value + ' ' + selectedDistrict.value + '은행 ', placesSearchCB);
  }
};
// 은행 주변 검색 함수
const searchNearbyBanks = (keyword) => {
  if (selectedDistrict.value && selectedCity.value) {
    // 시/도, 시/군/구에 따라 은행 주변 검색 수행
    const ps = new kakao.maps.services.Places();
    ps.keywordSearch(keyword + ' ' + selectedCity.value + ' ' + selectedDistrict.value, placesSearchCB);
  }
};

// 키워드 검색 완료 시 호출되는 콜백함수 입니다
const placesSearchCB = (data, status) => {
  if (status === kakao.maps.services.Status.OK) {
    // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
    // LatLngBounds 객체에 좌표를 추가합니다
    const bounds = new kakao.maps.LatLngBounds();

    markers.value = [];

    for (let marker of data) {
      const markerItem = {
        lat: marker.y,
        lng: marker.x,
        infoWindow: {
          content: marker.place_name,
          visible: false
        }
      };
      markers.value.push(markerItem);
      bounds.extend(new kakao.maps.LatLng(Number(marker.y), Number(marker.x)));
    }

    // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
    map.value?.setBounds(bounds);
  }
};

//마커 클릭 시 인포윈도우의 visible 값을 반전시킵니다
const onClickMapMarker = (markerItem) => {
  if (markerItem.infoWindow?.visible !== null && markerItem.infoWindow?.visible !== undefined) {
    markerItem.infoWindow.visible = !markerItem.infoWindow.visible;
  } else {
    markerItem.infoWindow.visible = true;
  }
};

// 카카오 맵 로드시 호출되는 함수
const onLoadKakaoMap = (mapRef) => {
  map.value = mapRef;
  // 초기 로딩 시 은행 주변 검색
  searchNearbyBanks();
};
</script>

<style scoped>
.options-container {
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-wrap: wrap;
  border: 2px solid #008485; /* 테두리 추가 */
  border-radius: 10px; /* 테두리를 둥글게 만듭니다. */
  padding: 10px; /* 내부 여백 추가 */
  margin: 10px;
}

.option-label {
  font-weight: bold;
  margin-bottom: 5px; /* 라벨 아래 여백을 줄입니다. */
  margin-right: 10px; /* 라벨 오른쪽 여백을 추가합니다. */
  color: #008485; /* 메인 컬러로 변경 */
}

.option-select {
  padding: 5px;
  border: 1px solid #008485; /* 메인 컬러로 변경 */
  border-radius: 5px;
  background-color: #f8f8f8;
  color: #333;
  width: 150px; /* 드롭다운 너비를 줄입니다. */
  margin: 5px;
}

.option-select:hover {
  background-color: #e0e0e0;
  cursor: pointer;
}

.kakao-map {
  margin: 50px auto; /* 가운데 정렬을 위해 margin 속성 추가 */
  border-radius: 1%;
}
</style>