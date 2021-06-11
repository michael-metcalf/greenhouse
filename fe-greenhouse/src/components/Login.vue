<template>
  <div class="login-container">
    <h2>Let's go <span class="green-emphasis">green</span>!</h2>
    <input
      type="text"
      v-model="currentUser.userName"
      id="username-input"
      name="username-input"
      placeholder="username..."
    />
    <input v-on:keyup.enter="validateUserInput"
      type="password"
      v-model="currentUser.password"
      id="password-input"
      name="password-input"
      placeholder="password..."
    />
    <div class="button-row">
      <button @click="validateUserInput">Login</button>
      <button id="create-account" v-on:click="showSignUp">Sign Up</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "Login",
  props: {
    msg: String,
  },
  data() {
    return {
      currentUser: {
        userName: "",
        password: "",
      },
    };
  },
  methods: {
    validateUserInput() {
      this.$store.dispatch("verifyLogin", {
        username: this.currentUser.userName,
        password: this.currentUser.password,
      });
    },
    showSignUp() {
      this.$store.commit("setShowsToFalse");
      this.$store.commit("showSignUp");
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
  align-items: center;
  justify-content: center;
  padding: 40px;
  width: 400px;
  height: 400px;
}

input {
  margin-bottom: 1.5em;
  height: 2em;
  font-size: large;
  filter: none;
}

.green-emphasis {
  color: rgb(40, 87, 76);
}

button {
  height: 2em;
  font-size: large;
  border-radius: 5px;
  background-color: #403d58;
  color: white;
  width: 75%;
  margin-left: 5px;
  margin-right: 5px;
}

h2 {
  margin-top: 0;
}

#sign-up {
  font-size: smaller;
  background-color: lightcyan;
}

.button-row {
  display: flex;
  justify-content: space-between;
  width: 90%;
}

/* #create-account {
  width: 150px;
  font-size: smaller;
} */
</style>
