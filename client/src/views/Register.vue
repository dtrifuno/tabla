<template>
  <div>
    <h4>Create an account</h4>
    <br />
    <v-dialog />
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
      <button type="button" v-on:click="click_register" class="btn btn-primary form-group">Sign Up</button>
    </form>
    <br />
    <p>
      Already a user?
      <a href="/">Please login instead</a>.
    </p>
  </div>
</template>

<script>
import { registerUser } from '../api';

export default {
  name: 'home',
  components: {},
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    account_created_modal() {
      this.$modal.show('dialog', {
        title: 'Account Created',
        text: 'Account successfully created. Please login to continue.',
        buttons: [
          {
            title: 'OK',
            handler: () => {
              this.$router.push({ path: '/' });
            },
            default: true,
          },
        ],
      });
    },
    account_exists_modal() {
      this.$modal.show('dialog', {
        title: 'Account Exists',
        text:
          'There already is an account associated to that email. Did you mean to login instead?',
      });
    },
    async click_register() {
      await registerUser(this.email, this.password)
        .then(() => {
          this.account_created_modal();
        })
        .catch(() => {
          this.account_exists_modal();
        });
    },
  },
};
</script>
