<template>
  <div>
    <h4>Login</h4>
    <br />
    <form class="mx-auto col-10 col-lg-2">
      <div class="form-group">
        <label for="email">Email</label>
        <input
          type="email"
          v-model="email"
          class="form-control"
          id="email"
          placeholder="Enter email."
        />
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input
          type="password"
          v-model="password"
          class="form-control"
          id="password"
          placeholder="Password"
        />
      </div>
      <button type="button" @click="click_login" class="btn btn-success form-group">Login</button>
    </form>
    <br />
    <p>
      Don't have an account?
      <a href="/register" class="text-success">Register for one</a>.
    </p>
  </div>
</template>

<style scoped>
label,
h4 {
  user-select: none;
}
</style>


<script>
import { mapActions } from 'vuex';

import { login } from '../api';

export default {
  name: 'home',
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    ...mapActions(['setToken', 'fetchTables']),
    async click_login() {
      await login(this.email, this.password)
        .then((response) => {
          this.setToken(response.data.access_token);
          console.log('logged in');
          this.fetchTables();
        })
        .then(() => this.$router.push({ path: '/tables' }));
    },
  },
};
</script>
