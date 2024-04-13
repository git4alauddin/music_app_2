import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'welcome',
      component: () => import('../views/welcome.vue')
    },
    {
      path: '/user_login',
      name: 'user_login',
      component: () => import('../views/user_login.vue')
    },
    {
      path: '/admin_login',
      name: 'admin_login',
      component: () => import('../views/admin_login.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/register.vue')
    },
    {
      path: '/user_dash',
      name: 'user_dash',
      component: () => import('../views/user_dash.vue')
    },
    {
      path: '/upload_song',
      name: 'upload_song',
      component: () => import('../views/upload_song.vue')
    },
    {
      path: '/admin_dash',
      name: 'admin_dash',
      component: () => import('../views/admin_dash.vue')
    },
    {
      path: '/creator_dash',
      name: 'creator_dash',
      component: () => import('../views/creator_dash.vue')
    },
    {
      path: '/playlist/:id/:title',
      name: 'playlist',
      component: () => import('../views/playlist.vue')
    },
    {
      path: '/album/:id/:title',
      name: 'album',
      component: () => import('../views/album.vue')
    }
  ]
})

export default router