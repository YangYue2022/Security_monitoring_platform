<!-- <template>
  <div id="app">
    <StreamViewer/>
  </div>
</template>

<script>
import StreamViewer from './components/StreamViewer.vue';

export default {
  name: 'App',
  components: {
    StreamViewer
  }
};
</script> -->

<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
</script>

<style lang="less">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
