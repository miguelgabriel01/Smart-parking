import { createRouter, createWebHistory } from "vue-router";

import ErrorPage from '../views/ErrorPage.vue'
import HomeDashboard from '../views/HomeDashboard.vue'
import HomePage from '../components/HomePage.vue'
import HomeParking from '../views/HomeParking.vue'


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
  {
    path: '/errorpage',
    name: 'ErrorPage',
    component: ErrorPage,
    props: true
  },
  {
    path: '/homeParking',
    name: 'HomeParking',
    component: HomeParking,
    props: true
  }

]

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;