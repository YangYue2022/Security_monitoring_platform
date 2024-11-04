<template>
  <div class="index-container">
    <h1>项目简介</h1>
    <p>这是一个面向视频流处理和人脸识别的项目，用户可以通过以下地址进行视频推流。</p>
    <div>
      <label for="stream-id">输入您的 Stream ID：</label>
      <input type="text" v-model="streamId" id="stream-id">
    </div>
    <p>您的推流地址是：</p>
    <p><code>rtmp://101.42.183.175:9090/live/{{ streamId }}</code></p>
  </div>
</template>

<script>
export default {
  name: "IndexView",
  data() {
    return {
      streamId: ''  // 初始化 streamId，用户可以在页面上输入
    };
  }
}
</script>

<style scoped>
.index-container {
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.index-container h1 {
  color: #333;
}

.index-container p {
  font-size: 16px;
  color: #666;
}

.index-container input[type="text"] {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 100%;
  box-sizing: border-box;
}

.index-container code {
  background-color: #eee;
  padding: 2px 6px;
  border-radius: 4px;
  color: #d23669;
}
</style>

