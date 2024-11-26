import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useProductStore = defineStore('product', () => {
  const depositProducts = ref([]) // 비어 있는 배열로 초기화
  const savingProducts = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const depositComments = ref([])
  const savingComments = ref([])

  const getDeposit = async function() {
    try {
      const response = await axios.get(`${API_URL}/api/v1/products/save-deposit-products/`);
      const responseData = response.data;

      // 응답 데이터가 유효한지 확인
    if (Array.isArray(responseData)) { // 응답 데이터가 배열인지 확인
      // 데이터를 저장
      depositProducts.value = responseData.map(product => ({
        ...product,
        productJoins: null // 초기 값은 null로 설정
      }));
      // 각 제품에 대한 추가 정보 가져오기
      await Promise.all(depositProducts.value.map(async product => {
        try {
          const joinResponse = await axios.get(`http://127.0.0.1:8000/api/v1/products/deposit-joins/${product.id}/`);
          product.productJoins = joinResponse.data.num_users;
        } catch (error) {
          console.error(`Error fetching deposit joins for product ${product.id}:`, error);
        }
      }));

    } else {
      console.error('Invalid response data:', responseData);
    }
  } catch (error) {
    console.error('Error fetching deposit products:', error);
  }
}
  
const getSaving = async function() {
  try {
    // 저축 상품에 대한 HTTP GET 요청
    const response = await axios.get(`${API_URL}/api/v1/products/save-saving-products/`);
    const responseData = response.data;

    // 응답 데이터가 유효한지 확인
    if (Array.isArray(responseData)) { // 응답 데이터가 배열인지 확인
      // 데이터를 저장
      savingProducts.value = responseData;

      // 각 제품에 대한 추가 정보 가져오기
      await Promise.all(savingProducts.value.map(async product => {
        try {
          // 각 제품에 대한 추가 정보를 얻기 위해 HTTP GET 요청
          const joinResponse = await axios.get(`http://127.0.0.1:8000/api/v1/products/saving-joins/${product.id}/`);
          // 제품에 대한 추가 정보 저장
          product.productJoins = joinResponse.data.num_users;
        } catch (error) {
          // 오류 처리
          console.error(`Error fetching saving joins for product ${product.id}:`, error);
        }
      }));

    } else {
      // 응답 데이터가 배열이 아닌 경우 오류 처리
      console.error('Invalid response data:', responseData);
    }
  } catch (error) {
    // 요청 오류 처리
    console.error('Error fetching saving products:', error);
  }
}

  const getDepositComments = function (product_id) {
    const token = localStorage.getItem('user-token')
    axios({
      method:'get',
      url:`${API_URL}/api/v1/deposit/${product_id}/comments/`,
      headers: {
        Authorization: `Token ${token}`
      }
    })
      .then((response)=> {
        depositComments.value = response.data 
      })
      .catch((error)=> console.log(error))
  }

  const getSavingComments = function (product_id) {
    const token = localStorage.getItem('user-token')
    axios({
      method:'get',
      url:`${API_URL}/api/v1/saving/${product_id}/comments/`,
      headers: {
        Authorization: `Token ${token}`
      }
    })
      .then((response)=> {
        savingComments.value = response.data 
      })
      .catch((error)=> console.log(error))
  }

  return { depositProducts, API_URL, getDeposit, savingProducts, getSaving, getDepositComments, depositComments, getSavingComments, savingComments }
},{persist: true})
