<template>
  <div class="login-container">
    <h2>账户注册</h2>
    <div class="login-form">
      <table class="login-table" border="0" cellpadding="10">
        <tr>
          <td align="center">用户名</td>
          <td><input id='username' type="text" v-model="username" placeholder="请输入学号"/></td>
        </tr>
        <tr>
          <td align="center">密&nbsp;&nbsp;&nbsp;&nbsp;码</td>
          <td><input id='password' type="password" v-model="password" placeholder="请输入密码"/></td>
        </tr>
        <tr align="center">
          <td colspan="2">
            <button @click="handleLogin">注册</button>
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

const router = useRouter();
const username = ref('');
const password = ref('');

async function handleLogin() {
  try {
    const response = await axios.post('/api/student/register', {
      id: username.value,
      password: password.value
    }, {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    console.log(response.status);
    if (response.data.code === -1) {
      alert('用户已注册');
    }else if (response.data.code === 200) {
      alert('注册成功！');
      router.push({ path: '/face-register', query: { id: username.value } }); // 跳转到人脸录入页面
    } 
  } catch (error) {
    console.error("Error during login:", error.message); // 添加错误处理，打印错误信息
  }
}
</script>

<style lang="less" scoped>
.login-container {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: url('../assets/background.png') no-repeat center center;
  background-size: cover;
  text-align: center;
}

h2 {
  margin-bottom: 30px;
  color: #fff;
  font-size: 35px;
}

.login-form {
  width: 100%;
  max-width: 400px;
  padding: 20px;
  background-color: rgba(249, 249, 249, 0.9);
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.login-table {
  width: 100%;
  border-collapse: collapse;
  border-spacing: 0;
}

.login-table td {
  padding: 16px 8px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

.login-table input[type="text"],
.login-table input[type="password"] {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  outline: none;
  box-sizing: border-box;
}

.login-table button {
  display: block;
  width: 100%;
  padding: 12px;
  background-color: #007bff;
  color: white;
  font-size: 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s ease;

  &:hover,
  &:focus {
    background-color: #0056b3;
  }
}

.register-link {
  margin-top: 20px;
  font-size: 14px;
}

.register-link a {
  color: #007bff;
  text-decoration: none;
  transition: color 0.3s ease;

  &:hover {
    color: #0056b3;
  }
}
</style>
