<template>
  <div class="login-container">
  <h2>Let's go <span class="green-emphasis">green</span>!</h2>
    <input type="text" v-model="userName" id="username-input" name="username-input" placeholder="Enter your username">
    <br>
    <input type="password" v-model="password" id="password-input" name="password-input" placeholder="Enter your password">
    <br>
    <button id="login-button" @click="validateUserInput">Login</button>
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
      this.$store.dispatch("verifyLogin", {"username": this.userName, "password": this.password})
      // this.$store.commit("setUserName", { userName: this.userName });
      // this.$emit("login-success");
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h2 {
    font-size: 60px;
    font-family: 'Lato', sans-serif;
  }

  input {
    margin-top: 5px;
    margin-bottom: 5px;
  }

  .green-emphasis {
    color: rgb(26, 146, 26);
    font-size: 70px;
  }

  #username-input, #password-input {
    width: 230px;
    height: 50px;
    font-size: 20px;
    border-radius: 5px;
    font-weight: 200;
  }
  #username-input:hover, #password-input:hover {
    border: 2px solid black;
  }

  #login-button {
    background-color:rgb(26, 146, 26);
    color: white;
    width: 200px;
    height: 50px;
    margin-top: 40px;
    border-radius: 5px;
    font-weight: 200;
    font-size: 30px;
    font-family: 'Lato', sans-serif;
  }
  #login-button:hover {
    background-color:rgb(15, 87, 15);
  }
</style>