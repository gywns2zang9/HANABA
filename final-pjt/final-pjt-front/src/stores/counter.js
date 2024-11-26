import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const articles = ref([])
  const comments = ref([])
  const info = ref([])
  const token = ref(null)

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const isToken = computed(()=> {
    if(token.value) {
      return token.value
    } else {
      return null
    }
  })
  const router = useRouter()

  const getArticles = function() {
    const token = localStorage.getItem('user-token')
    if (articles) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
        headers: {
          Authorization: `Token ${token}`
        }
      })
        .then((response)=> {
          articles.value = response.data 
        })
        .catch((error)=> console.log(error))
    }}

  const getComments = function (article_id) {
    axios({
      method:'get',
      url:`${API_URL}/api/v1/articles/${article_id}/comments/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((response)=> {
        comments.value = response.data 
      })
      .catch((error)=> console.log(error))
  }
  
  const getInfo = function () {
    const token = localStorage.getItem('user-token')
    axios({
      method:'get',
      url:`${API_URL}/userinfo/`,
      headers: {
        Authorization: `Token ${token}`
      }
    })
      .then((response)=> {
        info.value = response.data
      })
      .catch((error)=> console.log(error))
  }

  const signUp = function (payload) {
    const { username, password1, password2, name, age, gender, asset, salary, target_period, future_value, purpose } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
         username, password1, password2, name, age, gender, asset, salary, target_period, future_value, purpose
      }
    })
     .then((response) => {
       console.log('회원가입 성공!')
       const password = password1
       logIn({ username, password })
     })
     .catch((error) => {
       console.log(error)
     })
  }
  
  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((response) => {
        token.value = response.data.key
        localStorage.setItem('user-token', token.value);
        // console.log(localStorage)
        getInfo()
        router.push({ name : 'home' })
      })
      .catch((error) => {
        console.log(error)
      })
  }


  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
      
    })
      .then((response) => {
        console.log(response)
        token.value = null
        info.value = []
        localStorage.removeItem('user-token');
        router.push({ name : 'logout' })
      })
      .catch((error) => {
        console.log(error)
      })
  }
  return { API_URL, articles, getArticles, signUp, logIn, token, isLogin, isToken, logOut, getComments, comments, getInfo, info }
},{persist: true})
