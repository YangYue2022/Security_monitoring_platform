// 引入Vue3以及新的vue-router
import { createRouter, createWebHistory } from 'vue-router';
import Login from '@/components/LoginView.vue';
import Index from "@/components/IndexView.vue";
import Register from "@/components/RegisterView.vue"
import FaceDetection from '@/components/StreamViewer.vue';
import Feature2 from '@/components/StreamViewer.vue';
import Feature3 from '@/components/StreamViewer.vue';
import Layout from '@/components/Layout.vue';
import FaceRegistration from '@/components/FaceRegistration.vue';


// 定义路由
const routes = [
  {
    path: '/login',
    name: 'LoginView',
    component: Login
  },
  { path: '/face-register', component: FaceRegistration},
  {
    path: '/register',
    name: 'RegisterView',
    component: Register
  },
  {
    path: '/',
    redirect: '/login'  // 将根路径重定向到登录界面
  },
  {
    path: '/',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'IndexView',
        component: Index,
        meta: { requiresAuth: true }
      },
      {
        path: 'face-detection',
        name: 'FaceDetection',
        component: FaceDetection,
        meta: { requiresAuth: true }
      },
      {
        path: 'feature2',
        name: 'Feature2',
        component: Feature2,
        meta: { requiresAuth: true }
      },
      {
        path: 'feature3',
        name: 'Feature3',
        component: Feature3,
        meta: { requiresAuth: true }
      }
    ]
  }
];

// 创建路由器实例
const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('isAuthenticated');
  if (to.matched.some(record => record.meta.requiresAuth) && !isAuthenticated) {
    next({ name: 'LoginView' });
  } else {
    next();
  }
});

// 导出全局注册
export default router;
