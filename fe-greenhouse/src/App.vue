<template>
  <div id="app">
    <div class="header">
      <h1>GreenHouse</h1>
    </div>
    <div class="main-panel">
      <component :is="component"></component>
      <!-- <Login/>
      <EnvironmentalFact/>
      <BudgetVisualization/>
      <EcoGoalProgress v-bind:ecoScore="45"/>
      <BudgetInput/> -->
    </div>
    <div class="nav-bar">
    <div id="footer-button-container">
    <button v-on:click="component = 'BudgetVisualization'" class="footer-button" name="profile" value="profile">🏠</button>
    <button v-on:click="component = 'ExpenseInput'" class="footer-button" name="expense-input" value="expense-input">💲</button>
    <button v-on:click="component = 'BudgetInput'" class="footer-button" name="monthly-budget" value="monthly-budget">📆</button>
    <!-- <button v-on:click="component = 'EcoGoalProgress'" class="footer-button" name="eco-goals" value="eco-goals">🌍</button> -->
    <!-- <button v-on:click="component = 'Login'" class="footer-button" name="logout" value="logout">👋</button> -->
  </div> 
    </div>
  </div>
</template>

<script>
import Login from "./components/Login.vue";
import BudgetVisualization from "./components/BudgetVisualization.vue";
import EcoGoalProgress from "./components/EcoGoalProgress.vue";
import ExpenseInput from "./components/ExpenseInput.vue";
import BudgetInput from "./components/BudgetInput.vue";


export default {
  name: "App",
  components: {
    Login,
    BudgetVisualization,
    EcoGoalProgress,
    ExpenseInput,
    BudgetInput
  },
  data () {
    return {
      component:
        "Login",
    }
  }
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

.main-panel > * {
  border: 1pt solid red;
  margin-top: 8vh;
  margin-bottom: 5px;
  padding: 5px;
}

.header {
  position: fixed;
  top: 0;
  width: 100%;
  min-height: 10vh;
  background: #ade3f6;
  border: 2px solid red;
}

.main-panel {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-bottom: 11.5vh;
}

.nav-bar {
  display: flex;
  flex-direction: column;
  justify-content: center;
  position: fixed;
  bottom: 0;
  width: 100%;
  min-height: 10vh;
  background: #ade3f6;
  border: 2px solid red;
}

#footer-button-container {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  padding: 10px;
}

.footer-button {
  font-size: 2em;
  min-width: 60px;
  min-height: 60px;
  padding: 5px;
  text-align: center;
  border-radius: 12%;
  border: 2px solid red;
}
</style>
