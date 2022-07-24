import Vue from 'vue';
import App from './App.vue';

import router from './router';
import vuetify from './plugins/vuetify' // add vuetify 했더니 자동생성

Vue.config.productionTip = false;

new Vue({
  router,
  vuetify,
  render: (h) => h(App)
}).$mount('#app');
