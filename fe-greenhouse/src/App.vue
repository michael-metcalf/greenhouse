<template>
  <div id="app">
    <div class="header">
      <h1>GreenHouse</h1>
    </div>
    <div class="main-panel">
      <Login/>
    </div>
    <div class="nav-bar"></div>
  </div>
</template>

<script>
import Login from "./components/Login.vue";

export default {
  name: "App",
  components: {
    Login,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  min-height: 100vh;
  background: #2980B9;  /* fallback for old browsers */
  background: -webkit-linear-gradient(to bottom, #FFFFFF, #ade3f6, #6DD5FA);  /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to bottom, #FFFFFF, #ade3f6, #6DD5FA); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}
</style>
