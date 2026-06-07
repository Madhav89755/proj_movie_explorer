import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import MovieDetailsView from '@/views/MovieDetailsView.vue'
import StaffProfileView from '@/views/StaffProfileView.vue'
import CreateRecordsView from '@/views/CreateRecordsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/movies/:id',
      name: 'movie-details',
      component: MovieDetailsView,
    },
    {
      path: '/staff/:id',
      name: 'staff-profile',
      component: StaffProfileView,
    },
    {
      path: '/create',
      name: 'create-records',
      component: CreateRecordsView,
    },
  ],
})

export default router
