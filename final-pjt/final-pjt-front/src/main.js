import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import { useKakao } from 'vue3-kakao-maps/@utils';
import BootstrapVue3 from 'bootstrap-vue-3'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'

const app = createApp(App)
const pinia = createPinia()

useKakao('e2704ad7daa6b163ad6381012a5fddfe', ['clusterer', 'services', 'drawing']);

pinia.use(piniaPluginPersistedstate)
app.use(pinia)
app.use(router)
app.use(BootstrapVue3)

app.mount('#app')
