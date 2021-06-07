<template>
  <div class="login-container">
    <h2>Let's go <span class="green-emphasis">green</span>!</h2>
    <input
      type="text"
      v-model="userName"
      id="username-input"
      name="username-input"
      placeholder="Enter your username"
    />
    <br />
    <input
      type="password"
      v-model="password"
      id="password-input"
      name="password-input"
      placeholder="Enter your password"
    />
    <br />
    <button @click="validateUserInput">Login</button>
  </div>
</template>

<script>
export default {
  name: "Login",
  props: {
    msg: String,
  },
  data: () => ({
    userName: "",
    password: "",
  }),
  methods: {
    validateUserInput() {
      this.$store.dispatch("verifyLogin", {
        username: this.userName,
        password: this.password,
      });
      // this.$store.commit("setUserName", { userName: this.userName });
      // this.$emit("login-success");
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
input {
  margin-top: 5px;
  margin-bottom: 5px;
}

.green-emphasis {
  color: lightgreen;
}
</style>
