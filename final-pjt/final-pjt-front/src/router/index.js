import { createRouter, createWebHistory } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

import HomeView from '@/views/HomeView.vue'
import SignUpView from '@/views/accounts/SignUpView.vue'
import LogInView from '@/views/accounts/LogInView.vue'
import LogOutView from '@/views/accounts/LogOutView.vue'
import UserInfoView from '@/views/accounts/UserInfoView.vue'
import UserInfoUpdateView from '@/views/accounts/UserInfoUpdateView.vue'
import ArticleView from '@/views/articles/ArticleView.vue'
import ArticleDetailView from '@/views/articles/ArticleDetailView.vue'
import ArticleCreateView from '@/views/articles/ArticleCreateView.vue'
import CommentCreateView from '@/views/articles/CommentCreateView.vue'
import ArticleUpdateView from '@/views/articles/ArticleUpdateView.vue'
import ProductView from '@/views/ProductView.vue'
import DepositView from '@/views/products/DepositView.vue'
import SavingView from '@/views/products/SavingView.vue'
import DepositDetailView from '@/views/products/DepositDetailView.vue'
import DepCommentCreateView from '@/views/products/DepCommentCreateView.vue'
import SavCommentCreateView from '@/views/products/SavCommentCreateView.vue'
import SavingDetailView from '@/views/products/SavingDetailView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import MapView from '@/views/MapView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/article',
      name: 'article',
      component: ArticleView
    },
    {
      path: '/article/:id',
      name: 'articleDetail',
      component: ArticleDetailView,
      children: [
        {
        path: 'comment',
        name: 'comment',
        component: CommentCreateView
      },
    ]
    },
    {
      path: '/update/:id',
      name: 'articleUpdate',
      component: ArticleUpdateView
    },
    {
      path: '/create',
      name: 'articleCreate',
      component: ArticleCreateView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'login',
      component: LogInView
    },
    {
      path: '/logout',
      name: 'logout',
      component: LogOutView,
      beforeEnter: (to, from) => {
        const store = useCounterStore()
        store.logOut()
      }
    },
    {
      path: '/userinfo',
      name: 'userInfo',
      component: UserInfoView
    },
    {
      path: '/userinfo/update',
      name: 'userInfoUpdate',
      component: UserInfoUpdateView
    },
    {
      path: '/product',
      name: 'product',
      component: ProductView,
      children: [{
        path: 'deposit',
        name: 'deposit',
        component: DepositView,
      },
      {
        path: 'saving',
        name: 'saving',
        component: SavingView,
      },
      {
        path: 'deposit/:fin_prdt_cd', // 상세 페이지 라우트
        name: 'depositDetail',
        component: DepositDetailView,
        children: [{
          path: 'comment/:product_id',
          name: 'dep_comment',
          component: DepCommentCreateView
        }]
      },
      {
        path: '/saving/:fin_prdt_cd', // 상세 페이지 라우트
        name: 'savingDetail',
        component: SavingDetailView,
        children: [{
          path: 'comment/:product_id',
          name: 'sav_comment',
          component: SavCommentCreateView
        }]
      }
    ]
    },
    {
      path: '/exchange',
      name: 'exchange',
      component: ExchangeView
    },
    {
      path: '/map',
      name: 'map',
      component: MapView
    },
  ]
})

router.beforeEach((to, from) => {
  const store = useCounterStore()
  if (to.name === 'article' && store.isLogin === false) {
    window.alert('로그인이 필요해요!!')
    return { name: 'login' }
  }
  if ((to.name === 'signup' || to.name === 'login') && (store.isLogin === true)) {
    window.alert('이미 로그인 했습니다.')
    return { name: 'article' }
  }
})

export default router
