<template>
  <div id="app">
    <div class="header">
      <h1>MoneySprouts</h1>
    </div>
    <div class="main-panel">
      <!-- we display the LOGIN component if no user is currently active -->
      <user-message-display />
      <Login v-if="this.$store.state.userName === ''" />
      <loading-message
        v-if="this.$store.state.userName !== '' && this.$store.state.isLoading"
      />
      <component
        v-if="this.$store.state.userName !== '' && !this.$store.state.isLoading"
        :is="component"
      ></component>
    </div>
    <div class="nav-bar">
      <div
        v-if="this.$store.state.userName !== ''"
        id="footer-button-container"
      >
        <button
          v-on:click="component = 'BudgetVisualization'"
          class="footer-button"
          name="profile"
          value="profile"
        >
          <i id="home-icon" class="fas fa-home"></i>
        </button>
        <button
          v-on:click="component = 'ExpenseInput'"
          class="footer-button"
          name="expense-input"
          value="expense-input"
        >
          <i id="dollar-icon" class="fas fa-dollar-sign"></i>
        </button>
        <button
          v-on:click="component = 'BudgetInput'"
          class="footer-button"
          name="monthly-budget"
          value="monthly-budget"
        >
          <i id="calendar-icon" class="far fa-calendar-alt"></i>
        </button>
        <button
          v-on:click="component = 'BarChart'"
          class="footer-button"
          name="eco-action-chart"
          value="eco-action-chart"
        >
          <i id="chart-icon" class="fas fa-chart-bar"></i>
        </button>
        <button
          v-on:click="$store.commit('clearUserName')"
          class="footer-button"
          name="logout"
          value="logout"
        >
          <i id="signout-icon" class="fas fa-sign-out-alt"></i>
        </button>
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
import LoadingMessage from "./components/LoadingMessage.vue";
import UserMessageDisplay from "./components/UserMessageDisplay";
import BarChart from "./components/BarChart";

export default {
  name: "App",
  components: {
    Login,
    BudgetVisualization,
    EcoGoalProgress,
    ExpenseInput,
    BudgetInput,
    LoadingMessage,
    UserMessageDisplay,
    BarChart,
  },
  data() {
    return {
      component: "BudgetVisualization",
    };
  },
  methods: {
    // async receiveLoginSignal() {
    //   // Need to download the data related to the current user
    //   console.log(`Received login signal...${this.$store.state.userName}`);
    //   this.$store.commit("setLoadingStatus", true);
    //   try {
    //     const api_address = "http://localhost:5000/api/";
    //     const budget_response = await axios.get(`${api_address}user/${this.$store.state.userName}/user_budget`);
    //     console.log(`Monthly budget : ${JSON.stringify(budget_response.data)}`);
    //     this.$store.commit("setMonthlyBudget", { monthlyBudget: budget_response.data });
    //     const expenses_response = await axios.get(`${api_address}user/${this.$store.state.userName}/expenses`);
    //     console.log(`Expenses list: ${JSON.stringify(expenses_response.data)}`);
    //     this.$store.commit("setExpensesList", { expensesList: expenses_response.data.expenses  });
    //     const eco_goals_response = await axios.get(`${api_address}user/${this.$store.state.userName}/eco_goals`);
    //     console.log(`Eco Goals list: ${JSON.stringify(eco_goals_response.data)}`);
    //     if (eco_goals_response.data.eco_goals) {
    //       this.$store.commit("setEcoGoalsList", { ecoGoalsList: eco_goals_response.data.eco_goals });
    //     }
    //     const eco_actions_response = await axios.get(`${api_address}user/${this.$store.state.userName}/eco_actions`);
    //     if (eco_actions_response.data.eco_actions) {
    //       this.$store.commit("setEcoActionsList", { ecoActionsList: eco_actions_response.data.eco_actions} );
    //     }
    //     this.$store.commit("setLoadingStatus", false);
    //   } catch(err) {
    //     console.error(`ERROR in the back-end API download! ${err}`);
    //   }
  },
  mounted() {
    const externalScript = document.createElement("script");
    externalScript.setAttribute(
      "src",
      "https://kit.fontawesome.com/e3cbc00358.js"
    );
    externalScript.setAttribute("crossorigin", "anonymous");
    document.head.appendChild(externalScript);
  },
};
</script>

<style>
#app {
  --app-max-width: 500px;

  /* Variable calculation for positioning */
  --header-footer-height: max(10vh, 60px);

  max-width: var(--app-max-width);
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  min-height: 100vh;

  /* Background features */
  /* 
  background: url("assets/blurred-bg-green.jpg") top repeat-y;
  background: url("assets/green-palmtree.jpg") top repeat-y;
  background: url("assets/green-surfer.jpg") top no-repeat;
  background: url("assets/grass-background.jpg") top repeat-y; */
  background: url("assets/green-palmtree.jpg") top repeat-y;
  background-size: auto 100%;
}

.main-panel {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  /* Height of the panel is the whole size - footer height */
  height: calc(100vh - 2 * var(--header-footer-height));
  /* The main panel has to be displayed from the bottom of the header, i.e
     header-content-height + 2* padding */
  margin-top: var(--header-footer-height);
}

.main-panel > * {
  padding: 5px;
  background-color: rgba(255, 255, 255, 0.8);
}

.header {
  /* Header position: ABSOLUTE (to always stay on top) */
  position: fixed;
  top: 0;
  width: 100%;
  max-width: var(--app-max-width);
  box-sizing: border-box;
  height: var(--header-footer-height);
  background-color: rgba(197, 231, 226, 1);
  display: flex; /* header has a flex display in order to center the title vertically */
  flex-direction: column;
}

.nav-bar {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 10px;
  box-sizing: border-box;
  position: fixed;
  bottom: 0;
  width: 100%;
  max-width: var(--app-max-width);
  height: var(--header-footer-height);
  background: rgba(255, 255, 255, 1);
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

#home-icon,
#dollar-icon,
#calendar-icon,
#signout-icon,
#chart-icon {
  color: teal;
}
</style>
