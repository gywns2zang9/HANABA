import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useExchangeStore = defineStore('exchange', () => {
  const exchangeRates = ref([])
  const API_URL = 'http://127.0.0.1:8000/api/v1'

  // 백엔드에서 환율 데이터를 가져오는 함수
  const getExchangeRates = async () => {
    try {
      const response = await axios.get(`${API_URL}/exchanges/save-exchange-rates/`)
      exchangeRates.value = response.data // 데이터를 가져와서 저장
    } catch (error) {
      console.error('Error fetching exchange rates:', error)
    }
  }
  return { exchangeRates, API_URL, getExchangeRates }
},{persist: true})
