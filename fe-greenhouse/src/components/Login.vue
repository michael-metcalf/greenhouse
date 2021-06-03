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
      type="text"
      v-model="password"
      id="password-input"
      name="password-input"
      placeholder="Enter your password"
    />
    <br />
    <button id="login_button" @click="validateUserInput">Login</button>
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
      this.$store.commit("setUserName", { userName: this.userName });
      this.$emit("login-success");
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
input {
  margin-top: 5px;
  margin-bottom: 5px;
  border-radius: 5px;
  height: 60px;
  width: 250px;
  background-color: rgb(216, 232, 245);
}
h2 {
  font-size: 37px;
  margin-top: 40px;
  margin-bottom: 40px;
}
#username-input {
  margin-bottom: 20px;
}

.green-emphasis {
  color: lightgreen;
  text-shadow: 1px 1px 1px black;
}
#login_button {
  width: 200px;
  height: 60px;
  border-radius: 5px;
  margin-top: 40px;
  background: #2b37e0;
  color: white;
  font-size: 30px;
  border: 3px solid rgb(0, 0, 0);
}
</style>
