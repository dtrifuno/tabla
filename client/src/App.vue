<template>
  <div id="app">
    <img src="./assets/logo.png">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: "App"
};
</script>

<style>
:root {
  --red: #e6261f;
  --orange: #eb7532;
  --yellow: #f7d038;
  --limegreen: #a3e048;
  --shamrock: #49da9a;
  --azure: #34bbe6;
  --royalblue: #4355db;
  --violet: #d23be7;
}

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.item-dropzone-area {
  background-color: green;
  width: 100%;
  height: 1rem;
}
</style>
