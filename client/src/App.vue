<template>
  <div id="app">
    <div class="navbar navbar-expand navbar-light fixed-top header p-1">
      <div class="container">
        <div class="navbar-brand pl-2">Tabla</div>
        <ul class="navbar-nav ml-auto">
          <li v-if="this.$store.state.token" class="nav-item">
            <router-link to="/tables" class="nav-link">Home</router-link>
          </li>
          <li v-if="this.$store.state.token" class="nav-item">
            <div class="nav-link" style="cursor: pointer" @click="logout">Logout</div>
          </li>
          <li v-if="!this.$store.state.token" class="nav-item">
            <router-link to="/" class="nav-link">Login</router-link>
          </li>
          <li v-if="!this.$store.state.token" class="nav-item">
            <router-link to="/register" class="nav-link">Register</router-link>
          </li>
        </ul>
      </div>
    </div>
    <br />
    <br />
    <br />
    <router-view />
  </div>
</template>

<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

.header {
  display: flex;
  flex-direction: row;
  border-bottom: 2px solid #28a745;
  background-color: white;
  color: white;
  user-select: none;
}

.dialog {
  height: 100%;
  display: flex;
  flex-direction: column;
}

.dialog-content {
  flex: 1 0 auto;
  width: 100%;
  padding: 15px;
  font-size: 14px;
}

.dialog-buttons {
  display: flex;
  flex: 0 1 auto;
  width: 100%;
  border-top: 1px solid #eee;
}

.dialog-title {
  font-weight: 600;
  padding-bottom: 15px;
}

.dialog-button {
  font-size: 12px !important;
  background: transparent;
  outline: none;
  padding: 0;
  margin: 0;
  border: 0;

  flex: 1 1 100%;
  box-sizing: border-box;
  line-height: 40px;
  height: 40px;

  &:hover {
    background: rgba(0, 0, 0, 0.01);
  }
  &:active {
    background: rgba(0, 0, 0, 0.025);
  }
  &:not(:first-of-type) {
    border-left: 1px solid #eee;
  }
}

.material-design-icon.icon-2x {
  height: 2em;
  width: 2em;
}

.material-design-icon.icon-2x > .material-design-icon__svg {
  height: 2em;
  width: 2em;
}

.material-design-icon__svg {
  bottom: 0 !important;
}
</style>

<script>
import { mapMutations } from 'vuex';

export default {
  methods: {
    ...mapMutations(['setToken', 'setCurrentTable']),
    logout() {
      this.setToken('');
      this.setCurrentTable({});
      this.$router.push({ path: '/' });
    },
  },
};
</script>
