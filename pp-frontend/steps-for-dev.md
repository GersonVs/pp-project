# Criação de projeto FrontEnd com Vue.js usando Vite

## Passos

1. Criar uma pasta para o projeto e acessar a pasta e criar o projeto. `yarn create vite . --template vue`

2. Instalar as dependências iniciais com  `yarn`

3. Rodar `yarn dev` e acessar o localhost

4. Alterar o arquivo vite.conf.js para definir um alias para a pasta **src**.
```js 
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    }
  }
})
```
5. Alterar os imports dos arquivos em src de **./** para **@/**.

6. Instar a vue-router dependência `yarn add -D vue-router@<version>`

7. Criar o arquivo @/plugins/router.js e adicionar as configurações de rota seguindo padrão. 
```js
import { createRouter, createWebHashHistory, createWebHistory } from "vue-router";

const routes = [
    {path: '', name: 'home', component: () => import('@/views/Home.vue')},
]

const router = createRouter({
    routes,
    history: createWebHistory(),
})

export default router
```
8. Criar o arquivo @/views/Home.vue
```vue
<template>
    <h1>Home</h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias quis rerum animi doloribus neque quam facere voluptas mollitia ex voluptatem ipsum dolore distinctio dignissimos, sint itaque porro labore natus. Magnam!</p>
</template>
```
9. Adicionar a navegação do arquivo App.vue
```vue
<template>
  <ul>
    <li>
      <router-link :to="{name: 'home'}">Home</router-link>
    </li>
  </ul>
  <router-view />
</template>

<script setup>
  import { RouterView, RouterLink } from 'vue-router'
</script>
```
10. Alterar o arquivo main.js para usar o vue-router
```js
import { createApp } from 'vue'
import App from '@/App.vue'
import router from '@/plugins/router'
import '@/style.css'

createApp(App).use(router).mount('#app')
```

11. Adicionando autenticação e redirecionamento ao vue-router
  - Adicionar um objeto **meta** as configurações da rota: 
  ```js
    function loadPage(view) {
      return () =>
      import(
          `@/views/${view}.vue`
      );
    }

    const routes = [
      {
        path: ''      , 
        name: 'crud_list' ,
        component: loadPage("CrudItems"),
        meta: {
            requiresAuth: true,
            permission: 'accessVoteRoute'
        }
      }
    ]

    const router = createRouter({
        routes,
        history: createWebHistory(),
    })

    export default router
  ```
  - Adicionar o seguinte ouvinte de evento após a instancia de router:
  ```js
    router.beforeEach( async (to, from, next) => {
      const requiresAuth = to.matched.some
      (record => record.meta.requiresAuth)

      if(requiresAuth && !await isUserLoggedIn()) next('/login')
      else next()
    })
  ```  

  > Onde **isUserLoggedIn** é uma função que analisa se o usuário está logado. 

12. Configurando um arquivo **.env**
1 - Na raiz do projeto crie um arquivo .env:
  ```env
  VITE_BACKEND_HOST='http://localhost:8000'
  ```
2 - Em seu código acesse o valor da variável da seguinte maneira:
```js
  const env = import.meta.env.VITE_BACKEND_HOST
```
