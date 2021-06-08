<template>
  <div class="login-container">
    <h2>Let's go <span class="green-emphasis">green</span>!</h2>
    <input
      type="text"
      v-model="userName"
      id="username-input"
      name="username-input"
      placeholder="username..."
    />
    <input
      type="password"
      v-model="password"
      id="password-input"
      name="password-input"
      placeholder="password..."
    />
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
.login-container {
  border-radius: 50%;
  border: none;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 40px;
  width: 280px;
  height: 280px;
  margin-top: auto;
}

input {
  margin-bottom: 1.5em;
  height: 1.2em;
}

.green-emphasis {
  color: rgb(40, 87, 76);
}

button {
  height: 2em;
  font-size: large;
}
</style>
