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
    <div class="signup-container">
    <input
      type="text"
      v-model="newUserName"
      id="new-username-input"
      name="username-input"
      placeholder="New username..."
    />
    <input
      type="password"
      v-model="newUserPassword"
      id="new-password-input"
      name="password-input"
      placeholder="New password..."
    />
    <input
      type="email"
      v-model="newUserEmail"
      id="new-email-input"
      name="email-input"
      placeholder="Enter Email..."
    />
    <button id="sign-up" @click="createUser">Sign Me Up!</button>
    </div>
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
    },
    createUser() {
      this.$store.dispatch("createUser", {
        username: this.userName,
      });
      this.$store.dispatch("createUserPassword", {
        password: this.password,
      });
    },
  }
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
}

.signup-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

#new-username-input, #new-password-input, #new-email-input {
  margin-top: 5px;
  width: 100px;
  display: flex;
  flex-direction: column;
  justify-content: center;
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

#sign-up {
  font-size: smaller;
  background-color: lightcyan;
}
</style>
