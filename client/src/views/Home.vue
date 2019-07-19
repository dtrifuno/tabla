<template>
  <div>
    <v-dialog />
    <h4>Login</h4>
    <br />
    <form class="mx-auto col-10 col-lg-2" v-on:submit.prevent>
      <div class="form-group">
        <label for="email">Email</label>
        <input
          type="email"
          v-model="email"
          class="form-control"
          id="email"
          placeholder="Email"
          @keyup.enter="triggerLogin"
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
          @keyup.enter="triggerLogin"
        />
      </div>
      <button
        type="button"
        @click="clickLogin"
        class="btn btn-success form-group"
        ref="loginButton"
      >Login</button>
    </form>
    <br />
    <p>
      Don't have an account?
      <router-link to="/register" class="text-success">Register for one</router-link>.
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
    triggerLogin() {
      this.$refs.loginButton.click();
    },
    invalidCredentialsModal() {
      this.$modal.show('dialog', {
        title: 'Invalid credentials',
        text:
          'Invalid login credentials. Please re-enter your email and password.',
      });
    },
    async clickLogin() {
      await login(this.email, this.password)
        .then((response) => {
          this.setToken(response.data.access_token);
          this.fetchTables();
        })
        .then(() => this.$router.push({ path: '/tables' }))
        .catch(() => {
          this.email = '';
          this.password = '';
          this.invalidCredentialsModal();
        });
    },
  },
};
</script>
