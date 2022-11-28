import { createRouter, createWebHistory } from "vue-router";

import HomeDashboard from '../components/HomeDashboard.vue'
import HomePage from '../components/HomePage.vue'



const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage,
  },
  {
    path: '/dashboard',
    name: 'HomeDashboard',
    component: HomeDashboard,
    props: true
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;