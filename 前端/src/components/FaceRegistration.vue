<template>
    <div class="registration-container">
      <h2>人脸录入</h2>
      <div class="video-container">
        <video ref="video" width="640" height="480" autoplay></video>
        <button @click="captureAndRegister">录入人脸</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import axios from 'axios';
  
  const route = useRoute();
  const router = useRouter();
  const video = ref(null);
  const studentId = route.query.id;
  
  onMounted(async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ video: true });
      if (video.value) {
        video.value.srcObject = stream;
      }
    } catch (error) {
      console.error('Error accessing the camera:', error);
    }
  });
  
  async function captureAndRegister() {
    if (!video.value) return;
  
    const canvas = document.createElement('canvas');
    canvas.width = video.value.videoWidth;
    canvas.height = video.value.videoHeight;
    const context = canvas.getContext('2d');
    context.drawImage(video.value, 0, 0, canvas.width, canvas.height);
    const imageBase64 = canvas.toDataURL('image/jpeg').split(',')[1];
  
    try {
      const response = await axios.post('/python/face-register', {
        student_id: studentId,
        image: imageBase64
      }, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
  
      if (response.status === 200) {
        alert('人脸录入成功！');
        router.replace('/index');
      } else {
        alert('人脸录入失败，请重试！');
      }
    } catch (error) {
      console.error('Error during face registration:', error.message);
      alert('人脸录入失败，请重试！');
    }
  }
  </script>
  
  <style scoped>
  .registration-container {
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
  
  .video-container {
    width: 100%;
    max-width: 640px;
    padding: 20px;
    background-color: rgba(249, 249, 249, 0.9);
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }
  
  video {
    display: block;
    width: 100%;
    border-radius: 8px;
    margin-bottom: 20px;
  }
  
  button {
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
  </style>
  