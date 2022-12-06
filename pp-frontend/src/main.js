import { createApp } from 'vue'
import OneSignalVuePlugin from '@onesignal/onesignal-vue3'
import App from '@/App.vue'
import router from '@/plugins/router'
import '@/style.scss'

const env = import.meta.env

const app = createApp(App)
app.use(router)
app.use(OneSignalVuePlugin, {
    appId: env.VITE_OS_APP_ID,
    subdomainName: env.VITE_BACKEND_HOST
})

app.mount('#app')

// import * as bootstrap from 'bootstrap'
// import { Tooltip, Toast, Popover } from 'bootstrap';
