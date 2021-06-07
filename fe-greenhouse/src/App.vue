<template>
  <div id="app">
    <div class="header">
      <h1 id="moneySproutsLogo">MoneySprouts</h1>
    </div>
    <div class="main-panel">
      <!-- <p>{{ greeting }}</p> for testing Vue-flask connection -->
      <!-- <p>{{ flaskGreeting }}</p> for testing Vue-flask connection -->
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
      <!-- <Login/>
      <EnvironmentalFact/>
      <BudgetVisualization/>
      <EcoGoalProgress v-bind:ecoScore="45"/>
      <BudgetInput/> -->
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
          🏠
        </button>
        <button
          v-on:click="component = 'ExpenseInput'"
          class="footer-button"
          name="expense-input"
          value="expense-input"
        >
          💲
        </button>
        <button
          v-on:click="component = 'BudgetInput'"
          class="footer-button"
          name="monthly-budget"
          value="monthly-budget"
        >
          📆
        </button>
        <button
          v-on:click="$store.commit('clearUserName')"
          class="footer-button"
          name="logout"
          value="logout"
        >
          👋
        </button>
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
import LoadingMessage from "./components/LoadingMessage.vue";
import UserMessageDisplay from "./components/UserMessageDisplay";

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
};
</script>

<style>
#app {
  --app-max-width: 500px;
  max-width: var(--app-max-width);
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  min-height: 100vh;
  background-color: #B5B7BB;
}

.main-panel > * {
  margin-top: 8vh;
  margin-bottom: 5px;
  padding: 5px;
}

.header {
  position: fixed;
  top: 0;
  width: 100%;
  max-width: var(--app-max-width);
  min-height: 10vh;
  background-image: url("../public/img/background/grass-header.jpg");

  border: 2px solid black;
}

#moneySproutsLogo {
  float: left;
  margin-left: 10px;
  font-weight: bolder;
  color: white;
  text-shadow: 2px 2px black;

}
.main-panel {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-bottom: 5.5vh;
  background-color: rgb(228, 225, 225);
  width: 450px;
  height: 800px;
  border: 1pt solid black;
  margin-left: 23px;
  border-radius: 5px;
}

.nav-bar {
  display: flex;
  flex-direction: column;
  justify-content: center;
  position: fixed;
  bottom: 0;
  width: 100%;
  max-width: var(--app-max-width);
  min-height: 10vh;
  background-color: black;
  background-image: url("../public/img/background/grass-header.jpg");
  border: 2px solid black;
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
  border: 2px solid black;
}
</style>
