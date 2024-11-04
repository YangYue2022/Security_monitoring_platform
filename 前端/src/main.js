// 导入Vue3的核心API，用于创建Vue应用实例
import {createApp} from 'vue';
import store from './store';

// 导入根组件App.vue，它是整个应用程序的主视图模板
import App from './App.vue';

// 导入已配置好的路由模块（index.js或router.ts等），它管理着应用内的页面跳转逻辑
import router from "@/router";

// 使用createApp方法创建一个Vue应用实例，并注册全局路由配置
const app = createApp(App).use(router);
app.use(store);

// 将Vue应用挂载到HTML文档中id为'app'的元素上
// 这将把整个应用程序渲染到这个DOM元素内部
app.mount('#app');

