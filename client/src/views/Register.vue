<template>
  <div>
    <h4>Create an account</h4>
    <br />
    <v-dialog />
    <form class="mx-auto col-10 col-lg-2" v-on:submit.prevent>
      <div class="form-group">
        <label for="email">Email</label>
        <input
          type="email"
          v-model="email"
          class="form-control"
          id="email"
          placeholder="Email"
          @keyup.enter="triggerSignup"
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
          @keyup.enter="triggerSignup"
        />
      </div>
      <div class="form-group">
        <label for="confirmPassword">Confirm Password</label>
        <input
          type="password"
          v-model="confirmPassword"
          class="form-control"
          id="confirmPassword"
          placeholder="Confirm Password"
          @keyup.enter="triggerSignup"
        />
      </div>
      <button
        type="button"
        v-on:click="clickRegister"
        class="btn btn-success form-group"
        ref="signUpButton"
      >Sign Up</button>
    </form>
    <br />
    <p>
      Already a user?
      <router-link to="/" class="text-success">Please login instead</router-link>.
    </p>
  </div>
</template>

<style scoped>
h4,
label {
  user-select: none;
}
</style>

<script>
import validator from 'validator';
import { registerUser } from '../api';

export default {
  name: 'home',
  components: {},
  data() {
    return {
      email: '',
      password: '',
      confirmPassword: '',
    };
  },
  methods: {
    triggerSignup(event) {
      event.stopPropagation();
      this.$refs.signUpButton.click();
    },
    accountCreatedModal() {
      this.$modal.show('dialog', {
        title: 'Account created',
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
    accountExistsModal() {
      this.$modal.show('dialog', {
        title: 'Account already exists',
        text:
          'There already is an account associated to that email. Did you mean to login instead?',
      });
    },
    invalidEmailModal() {
      this.$modal.show('dialog', {
        title: 'Invalid email',
        text: 'You have entered an invalid email. Please check the email field for mistakes.',
      });
    },
    invalidPasswordModal() {
      this.$modal.show('dialog', {
        title: 'Invalid password',
        text:
          'The password you entered is too short. Please choose a password that is at least six characters.',
      });
    },
    differentPasswordsModal() {
      this.$modal.show('dialog', {
        title: 'Invalid password',
        text: 'The password fields do not match. Please re-enter your password.',
      });
    },
    async clickRegister() {
      if (!validator.isEmail(this.email)) {
        this.invalidEmailModal();
      } else if (this.password.length < 6) {
        this.invalidPasswordModal();
        this.password = '';
        this.confirmPassword = '';
      } else if (this.password !== this.confirmPassword) {
        this.differentPasswordsModal();
        this.password = '';
        this.confirmPassword = '';
      } else {
        await registerUser(this.email, this.password)
          .then(() => {
            this.accountCreatedModal();
          })
          .catch(() => {
            this.accountExistsModal();
          });
      }
    },
  },
};
</script>
