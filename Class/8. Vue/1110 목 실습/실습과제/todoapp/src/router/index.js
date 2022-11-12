import Vue from 'vue'
import VueRouter from 'vue-router'
import AllTodoPageView from '../views/AllTodoPageView.vue'
import ImportTodoPageView from '@/views/ImportTodoPageView'
import TodayTodoPageView from '@/views/TodayTodoPageView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'all',
    component: AllTodoPageView
  },
  {
    path: '/important',
    name: 'important',
    component: ImportTodoPageView
  },
  {
    path: '/today',
    name: 'today',
    component: TodayTodoPageView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
