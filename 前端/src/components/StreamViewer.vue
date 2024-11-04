<template>
  <div class="video-stream-viewer">
    <select v-model="selectedStream">
      <option value="1">Stream 1</option>
      <option value="2">Stream 2</option>
      <option value="3">Stream 3</option>
    </select>
    <img :src="videoFeedUrl" alt="Video Stream" @error="handleImageError"/>
  </div>
</template>

<script>
export default {
  name: 'VideoStreamViewer',
  data() {
    return {
      selectedStream: '1',
      videoFeedBaseUrl: 'http://127.0.0.1:5000/video_feed/'
    };
  },
  computed: {
    videoFeedUrl() {
      return `${this.videoFeedBaseUrl}${this.selectedStream}`;
    }
  },
  methods: {
    handleImageError() {
      console.error('Failed to load the video stream image.');
    }
  }
};
</script>

<style scoped>
.video-stream-viewer {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.video-stream-viewer img {
  max-width: 100%;
  max-height: 100%;
  display: block;
  margin: 0 auto;
}

</style>
