import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/register',
      name: 'register',
      component: () => import(/* webpackChunkName: "about" */ './views/Register.vue'),
    },
    {
      path: '/tables',
      name: 'tables',
      component: () => import(/* webpackChunkName: "tables" */ './views/Tables.vue'),
    },
    {
      path: '/table',
      name: 'table',
      component: () => import(/* webpackChunkName: "table" */ './views/Table.vue'),
    },
  ],
});
