import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'
import Dashboard from '../views/Dashboard.vue'
import Profile from '../views/Profile.vue'
import Request from '../views/SignRequest.vue'
import Documents from '../views/Documents.vue'
import Document from '../views/Document.vue'
import Register from '../views/Register.vue'
import Login from '../views/Login.vue'
import DocumentValidation from '../views/DocValidation.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/register',
    name: 'register',
    
    component: Register
  },
  {
    path: '/',
    name: 'login',
    component: Login
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: Dashboard,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
    meta: {
      requireLogin: true
    }
    // // route level code-splitting
    // // this generates a separate chunk (about.[hash].js) for this route
    // // which is lazy-loaded when the route is visited.
    // component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/request',
    name: 'request',
    component: Request,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/documents',
    name: 'documents',
    component: Documents,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/document/:id',
    name: 'document',
    component: Document,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/documentvalidation',
    name: 'documentvalidation',
    component: DocumentValidation,
   
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !localStorage.getItem('token')) {
    next('/')
  } else {
    next()
  }
})



export default router
