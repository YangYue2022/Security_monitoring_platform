<template>
  <div class="layout">
    <header class="header">
      <div class="logo">
        报警系统
      </div>
      <div class="user-info">
        <span>欢迎, {{ username }}</span>
        <button @click="logout">退出</button>
      </div>
    </header>
    <div class="content">
      <aside class="sidebar">
        <nav>
          <ul>
            <li :class="{ active: isActive('/face-detection') }"><router-link to="/face-detection">人脸检测</router-link></li>
            <li :class="{ active: isActive('/feature2') }"><router-link to="/feature2">功能2</router-link></li>
            <li :class="{ active: isActive('/feature3') }"><router-link to="/feature3">功能3</router-link></li>
          </ul>
        </nav>
      </aside>
      <main class="main-content">
        <router-view></router-view>
      </main>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
export default {
  name: 'Layout',
  computed: {
    ...mapState(['username'])
  },
  methods: {
    ...mapActions(['logout']),
    isActive(path) {
      return this.$route.path === path;
    },
    logout() {
      // 执行登出操作，比如清除用户数据和跳转到登录页面
      this.$router.push('/login');
    }
  }
};
</script>

<style scoped>
.layout {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color:  #333;
  color: white;
  padding: 0 20px;
  height: 60px; /* 增加 header 的高度 */
}

.logo {
  font-size: 20px;
  font-weight: bold;
}

.user-info {
  display: flex;
  align-items: center;
  height: 5vh;
}

.user-info span {
  margin-right: 20px;
}

.user-info button {
  background-color: transparent;
  border: none;
  color: white;
  cursor: pointer;
  font-size: 16px;
}

.content {
  display: flex;
  flex: 1;
}

.sidebar {
  width: 200px;
  background-color: #333;
  padding: 20px;
  box-sizing: border-box;
}

.sidebar nav ul {
  list-style: none;
  padding: 0;
}

.sidebar nav ul li {
  margin: 10px 0;
}

.sidebar nav ul li a {
  color: white;
  text-decoration: none;
  font-size: 16px;
  display: block;
  padding: 10px;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.sidebar nav ul li.active a {
  background-color: #007bff;
}

.sidebar nav ul li a:hover {
  background-color: #555;
}

.main-content {
  flex: 1;
  padding: 20px;
  background-color: #f5f5f5;
  box-sizing: border-box;
}
</style>
