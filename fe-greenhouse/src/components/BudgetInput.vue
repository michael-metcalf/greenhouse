<template>
  <div id="budget-input-container">
    <p>Monthly Budget: {{ monthlyBudget }}</p>
    <table id="budget-input-table">
      <thead>
        <th></th>
        <th>Running Total</th>
        <th>Amount Allocated</th>
      </thead>
      <tbody>
        <tr>Groceries
          <td>{{runningGroceries}}</td>
          <td>{{allocatedGroceries}}</td>
        </tr>
        <tr>Bills
          <td>{{runningBills}}</td>
          <td>{{allocatedBills}}</td>
        </tr>
        <tr>Transport
          <td>{{runningTransport}}</td>
          <td>{{allocatedTransport}}</td>
        </tr>
        <tr>Misc
          <td>{{runningMisc}}</td>
          <td>{{allocatedMisc}}</td>
        </tr>
        <tr>Savings Target
          <td>{{savingsTarget}}</td>
        </tr>
      </tbody>
    </table>
    <p>Savings Leeway: {{savingsLeeway}}</p>
    <div id="button-container">
      <button class="budget-button" name="back" value="back">Back</button>
      <button class="budget-button" name="edit" value="edit">Edit</button>
      <button class="budget-button" name="ok" value="ok">OK</button>
    </div>
  </div>
</template>

<script>

export default {
  name: "BudgetInput",
  props: {
  },
  methods: {
  },
  data() {
    return {
      monthlyBudget: '',
      runningGroceries: '',
      allocatedGroceries: '',
      runningBills: '',
      allocatedBills: '',
      runningTransport: '',
      allocatedTransport: '',
      runningMisc: '',
      allocatedMisc: '',
      savingsTarget: '',
      savingsLeeway: '',
    }
  },
  mounted() {
    this.monthlyBudget = 200000;
    this.runningGroceries = 20000;
    this.allocatedGroceries = 0;
    this.runningBills = 20000;
    this.allocatedBills = 0;
    this.runningTransport = 20000;
    this.allocatedTransport = 0;
    this.runningMisc = 20000;
    this.allocatedMisc = 0;
    this.savingsTarget = 10000;
    this.savingsLeeway = 110000;
  }
}
</script>

<style scoped>

</style>