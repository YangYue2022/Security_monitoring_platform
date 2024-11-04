// src/store/index.js
import { createStore } from 'vuex';

const store = createStore({
  state: {
    username: localStorage.getItem('username') || ''
  },
  mutations: {
    setUsername(state, username) {
      state.username = username;
      localStorage.setItem('username', username);
    },
    clearUsername(state) {
      state.username = '';
      localStorage.removeItem('username');
    }
  },
  actions: {
    login({ commit }, username) {
      commit('setUsername', username);
      localStorage.setItem('isAuthenticated', 'true');
    },
    logout({ commit }) {
      commit('clearUsername');
      localStorage.removeItem('isAuthenticated');
    }
  }
});

export default store;
