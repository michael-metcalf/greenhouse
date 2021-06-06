<template>
  <div>
    <span class="env-fact-container">
    <EnvironmentalFact />
    </span>
    <div class="budget-viz-container">
      <div class="chart-align-container">
        <div class="budget-progress"><p>{{ Math.floor(targetPercent*100) + "%" }}</p></div>
        <progress-chart :savingsScore="targetPercent" :css-classes="'chartContainer'" />
      </div>
      <h2>Potential savings: {{ income - expenses }}</h2>
      <ul class="no-bullets">
        <li>Income: {{ income }}</li>
        <li>Expenses: {{ expenses }}</li>
      </ul>
    </div>
    <span>
      <EcoGoalProgress :ecoScore="Math.max(0,10-this.missedEcoActions)" />
    </span>
  </div>
</template>

<script>
import ProgressChart from "./progressChart.vue";
import EnvironmentalFact from './EnvironmentalFact.vue';
import EcoGoalProgress from './EcoGoalProgress';

export default {
  name: "BudgetVisualization",
  components: {
    ProgressChart,
    EnvironmentalFact,
    EcoGoalProgress,
  },
  data: () => {
    return {
      income: 3,
      expenses: 1,
      targetPercent: 0.8,
      missedEcoActions: 0,
    };
  },
  methods: {
    getSumOfExpenses() {
      this.expenses = this.$store.state.expensesList
        .map((x) => x.amount)
        .reduce((currentSum, currentValue) => currentSum + currentValue,0);
    },
    getMonthlyBudget() {
      console.log("I AM SETTING THE MONTHLY BUDGET NOW")
      this.income = this.$store.state.monthlyBudget.monthly_income;
      console.log("THIS IS INCOME", this.income)
    },
    getNumberOfMissedEcoActions() {
      // TO DO -> remove the hard coded value
      this.missedEcoActions = this.$store.state.ecoActionsList.filter(action => action.eco_goal_id === 4).length;
    }
  },
  beforeMount() {
    console.log("THIS IS BEFORE MOUNTED")
    this.getMonthlyBudget();
    this.getSumOfExpenses();
    this.getNumberOfMissedEcoActions();
    this.targetPercent = Math.floor(this.expenses/this.income*100)/100
  },

  mounted() {
    console.log("I AM MOUNTED")
  }
};
</script>

<style>
.budget-viz-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  /* position: relative; */
}

.chart-align-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  width: 100%;
}

.budget-progress {
  position: absolute;
  top: 50%;
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
  left: 0;
  width: 100%;
}

.budget-progress p {
  font-size: larger;
  font-weight: bold;
}

ul.no-bullets {
  list-style-type: none;
  padding: 0;
  margin: 0;
}
</style>
