<template>
  
  <div>
    <p class="budget-progress">80%</p>

    <h2> Potential savings: {{income-expenses}} </h2>
    <h3> Income: {{income}} </h3>
    <h3> Expenses: {{expenses}}</h3>

  </div>

</template>

<script>
export default {
  name: "BudgetVisualization",
  data: () => {
    return ({
    income: 3,
    expenses: 1,
  });
  },
  methods: {
  },
  mounted() {
  }
  
};

</script>

<style>

</style>