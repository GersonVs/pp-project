import { createRouter, createWebHistory } from "vue-router";
import { isUserLoggedIn } from '@/auth/jwtUtils' 

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
    },
    {
        path: '/vote' ,
        name: 'vote_items',
        component: loadPage("VoteItemsPage")
    },
    {
        path: '/home' ,
        name: 'home'      ,
        component: loadPage("Home")
    },
    {
        path: '/about',
        name: 'about'     ,
        component: loadPage("About")
    },
    {
        path: '/login',
        name: 'login'     , component: () => import('@/views/authentication/Login.vue')
    },
]

const router = createRouter({
    routes,
    history: createWebHistory(),
})

router.beforeEach( async (to, from, next) => {
    const requiresAuth = to.matched.some
    (record => record.meta.requiresAuth)

    if(requiresAuth && !await isUserLoggedIn()) next('/login')
    else next()
})

export default router






