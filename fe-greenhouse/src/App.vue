<template>
  <div id="app">
    <div class="header">
      <h1>GreenHouse</h1>
    </div>
    <div class="main-panel">
      <Login/>
      <EnvironmentalFact/>
      <BudgetVisualization/>
      <EcoGoalProgress v-bind:ecoScore="45"/>
      <Settings/>
      <ExpenseInput/>
      <BudgetInput/>
    </div>
    <div class="nav-bar">
      <FooterNav/>
    </div>
  </div>
</template>

<script>
import Login from "./components/Login.vue";
import EnvironmentalFact from "./components/EnvironmentalFact.vue";
import BudgetVisualization from "./components/BudgetVisualization.vue";
import EcoGoalProgress from "./components/EcoGoalProgress.vue";
import FooterNav from "./components/FooterNav.vue";
import Settings from "./components/Settings.vue";
import ExpenseInput from "./components/ExpenseInput.vue";
import BudgetInput from "./components/BudgetInput.vue";


export default {
  name: "App",
  components: {
    Login,
    EnvironmentalFact,
    BudgetVisualization,
    EcoGoalProgress,
    FooterNav,
    Settings,
    ExpenseInput,
    BudgetInput
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

.main-panel > * {
  border: 1pt solid red;
  margin-top: 5px;
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
  margin-bottom: 10vh;
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
</style>
