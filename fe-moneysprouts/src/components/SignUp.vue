<template>
  <div class="signup-container">
    <h2>Let's go <span class="green-emphasis">green</span>!</h2>
    <input
      type="text"
      v-model="newUser.userName"
      id="new-username-input"
      name="username-input"
      placeholder="New username..."
    />
    <input
      type="password"
      v-model="newUser.password"
      id="new-password-input"
      name="password-input"
      placeholder="New password..."
    />
    <input
      type="email"
      v-model="newUser.email"
      id="new-email-input"
      name="email-input"
      placeholder="Email..."
    />
    <button id="sign-up" @click="createUser">Sign Me Up!</button>
    <p id="created"></p>
    <button id="login" v-on:click="showLogin">Return To Login</button>
  </div>
</template>

<script>
export default {
  name: "SignUp",
  props: {
    msg: String,
  },
  data() {
    return {
      warningNotice: null,
      newUser: {
        userName: null,
        password: null,
        email: null,
      },
    };
  },
  methods: {
    dataValidator() {
      // check if the input fields are blank
      const signUpWarnings = {
        userName: "username",
        password: "password",
        email: "email",
      };

      for (let signup in signUpWarnings) {
        if (!this.newUser[signup]) {
          this.warningNotice = `Please enter a valid ${signUpWarnings[signup]}`;
          return false;
        }
      }
      return true;
    },
    createUser() {
      if (this.dataValidator()) {
        const newUser = {
          username: this.newUser.userName,
          password: this.newUser.password,
          email: this.newUser.email,
        };
        this.$store.dispatch("createUser", newUser);
      } else {
        alert(this.warningNotice);
      }
    },
    showLogin() {
      this.$store.commit("setShowsToFalse");
      this.$store.commit("showLogin");
    },
  },
};
</script>

<style scoped>
  input {
    margin-bottom: 1em;
    height: 2em;
    font-size: large;
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

.signup-container {
  border-radius: 50%;
  border: none;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 40px;
  width: 400px;
  height: 400px;
}

.green-emphasis {
  color: rgb(40, 87, 76);
}

#created {
  background-color: white;
  color: green;
}
</style>
