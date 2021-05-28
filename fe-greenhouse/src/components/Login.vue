<template>
  <div class="login-container">
  <h2>Let's go green!</h2>
    <input type="text" id="username-input" name="username-input" placeholder="Enter your username">
    <br>
    <input type="text" id="password-input" name="password-input" placeholder="Enter your password">
    <br>
    <button>Login</button>
  </div>
</template>

<script>
export default {
  name: "Login",
  props: {
    msg: String,
  },
  methods: {
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>