<template>
  <div id="homePanel">
    <h1>Welcome, {{ this.$store.state.userName }} </h1>
      <EcoGoalProgress :ecoScore="Math.max(0, 10 - this.missedEcoActions)" />
      
    <div class="budget-viz-container">
      <h1>This month's savings</h1>
      <div class="chart-align-container">
        <div class="budget-progress">
          <p>{{ Math.floor(targetPercent * 100) + "%" }}</p>
        </div>
        <progress-chart
          :savingsScore="Math.min(targetPercent, 1)"
          :css-classes="'chartContainer'"
        />
      </div>
      <h2>
        Potential savings:
        {{ !isNaN(income - expenses) ? income - expenses : 0 }}
      </h2>
      <ul class="no-bullets">
        <li>Income: {{ income }}</li>
        <li>Expenses: {{ expenses }}</li>
      </ul>
    </div>
      <EnvironmentalFact />
  </div>
</template>

<script>
import ProgressChart from "./progressChart.vue";
import EnvironmentalFact from "./EnvironmentalFact.vue";
import EcoGoalProgress from "./EcoGoalProgress";


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
      this.expenses = !isNaN(
        this.$store.state.expensesList
          .map((x) => x.amount)
          .reduce((currentSum, currentValue) => currentSum + currentValue, 0)
      )
        ? this.$store.state.expensesList
            .map((x) => x.amount)
            .reduce((currentSum, currentValue) => currentSum + currentValue, 0)
        : 0;
    },
    getMonthlyBudget() {
      this.income = this.$store.state.monthlyBudget.monthly_income;
    },
    getNumberOfMissedEcoActions() {
      // TO DO -> remove the hard coded value
      this.missedEcoActions = this.$store.state.ecoActionsList.filter(
        (action) => action.eco_goal_id === 4
      ).length;
    },
  },
  beforeMount() {
    this.getMonthlyBudget();
    this.getSumOfExpenses();
    console.log(
      `This is before month expense ${this.expenses} and income ${this.income}`
    );
    this.getNumberOfMissedEcoActions();
    this.targetPercent =
      !isNaN(Math.floor((this.expenses / this.income) * 100) / 100) &&
      ((this.expenses / this.income) * 100) / 100 !== Infinity
        ? Math.floor((this.expenses / this.income) * 100) / 100
        : 0;
  },

  mounted() {},
};
</script>

<style>
#homePanel {
  display: flex;
  flex-direction: column;
  background-color: rgba(255, 255, 255, 0.5);
  align-content: center;
}

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
