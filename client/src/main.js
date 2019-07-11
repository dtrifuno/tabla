import Vue from 'vue';
import BootstrapVue from 'bootstrap-vue';
import VModal from 'vue-js-modal';
import App from './App.vue';

import router from './router';
import store from './store';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import 'vue-js-modal/dist/styles.css';
import 'vue-material-design-icons/styles.css';

Vue.config.productionTip = false;
Vue.use(BootstrapVue);
Vue.use(VModal, { dialog: true });

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
