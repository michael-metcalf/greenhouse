<template>
  <div>
    <span class="env-fact-container">
    <EnvironmentalFact />
    </span>
    <div class="budget-viz-container">
      <div class="chart-align-container">
        <div class="budget-progress"><p>80%</p></div>
        <progress-chart :savingsScore="0.8" :css-classes="'chartContainer'" />
      </div>
      <h2>Potential savings: {{ income - expenses }}</h2>
      <ul class="no-bullets">
        <li>Income: {{ income }}</li>
        <li>Expenses: {{ expenses }}</li>
      </ul>
    </div>
    <span>
      <EcoGoalProgress :ecoScore="70" />
    </span>
    <span class="settings-container">
    <Settings />
    </span>
  </div>
</template>

<script>
import ProgressChart from "./progressChart.vue";
import EnvironmentalFact from './EnvironmentalFact.vue';
import Settings from './Settings.vue';
import EcoGoalProgress from './EcoGoalProgress';

export default {
  name: "BudgetVisualization",
  components: {
    ProgressChart,
    EnvironmentalFact,
    Settings,
    EcoGoalProgress,
  },
  data: () => {
    return {
      income: 3,
      expenses: 1,
    };
  },
  methods: {
    getSumOfExpenses() {
      this.expenses = this.$store.state.expensesList
        .map((x) => x.amount)
        .reduce((currentSum, currentValue) => currentSum + currentValue);
    },
    getMonthlyBudget() {
      this.income = this.$store.state.monthlyBudget.monthly_income;
    }
  },
  beforeMount() {
    this.getSumOfExpenses();
    this.getMonthlyBudget();
  },
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
