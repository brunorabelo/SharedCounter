import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/WaitingRoom.vue')
    },
    {
      path: '/enter-room/:roomName/',
      name: 'enter-room',
      component: () => import('../views/WaitingRoom.vue')
    },
    {
      path: '/room/:roomName/',
      name: 'room',
      component: () => import('../views/RoomView.vue')
    },
    {
      path: '/about/',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router
