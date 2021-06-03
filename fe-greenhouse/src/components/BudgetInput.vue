<template>
  <div id="budget-input-container">
    <form id="budget-input-form" action="" @submit.prevent="getUserBudgetInput">
      <p>Monthly Income: 
        <span class="field-value" v-show="!showField('monthlyIncome')" @click="focusField('monthlyIncome')">{{form.monthlyIncome}}</span>
        <input v-model="form.monthlyIncome" v-show="showField('monthlyIncome')" id="monthly-income" type="text" class="field-value form-control" @focus="focusField('monthlyIncome')" @blur="blurField">
      </p>
      <table id="budget-input-table">
        <thead>
          <th></th>
          <th>Running Total</th>
          <th>Amount Allocated</th>
        </thead>
        <tbody>
          <tr>Groceries
            <td>{{runningGroceries}}</td>
            <td>
              <span class="field-value" v-show="!showField('allocatedGroceries')" @click="focusField('allocatedGroceries')">{{form.allocatedGroceries}}</span>
              <input v-model="form.allocatedGroceries" v-show="showField('allocatedGroceries')" id="allocated-groceries" type="text" class="field-value form-control" @focus="focusField('allocatedGroceries')" @blur="blurField">
            </td>
          </tr>
          <tr>Bills
            <td>{{runningBills}}</td>
            <td>
              <span class="field-value" v-show="!showField('allocatedBills')" @click="focusField('allocatedBills')">{{form.allocatedBills}}</span>
              <input v-model="form.allocatedBills" v-show="showField('allocatedBills')" id="allocated-bills" type="text" class="field-value form-control" @focus="focusField('allocatedBills')" @blur="blurField">
            </td>
          </tr>
          <tr>Transport
            <td>{{runningTransport}}</td>
            <td>
              <span class="field-value" v-show="!showField('allocatedTransport')" @click="focusField('allocatedTransport')">{{form.allocatedTransport}}</span>
              <input v-model="form.allocatedTransport" v-show="showField('allocatedTransport')" id="allocated-transport" type="text" class="field-value form-control" @focus="focusField('allocatedTransport')" @blur="blurField">
            </td>
          </tr>
          <tr>Misc
            <td>{{runningMisc}}</td>
            <td>
              <span class="field-value" v-show="!showField('allocatedMisc')" @click="focusField('allocatedMisc')">{{form.allocatedMisc}}</span>
              <input v-model="form.allocatedMisc" v-show="showField('allocatedMisc')" id="allocated-misc" type="text" class="field-value form-control" @focus="focusField('allocatedMisc')" @blur="blurField">
            </td>
          </tr>
          <tr>Savings Target
            <td>
              <span class="field-value" v-show="!showField('savingsTarget')" @click="focusField('savingsTarget')">{{form.savingsTarget}}</span>
              <input v-model="form.savingsTarget" v-show="showField('savingsTarget')" id="savings-target" type="text" class="field-value form-control" @focus="focusField('savingsTarget')" @blur="blurField">
            </td>
          </tr>
        </tbody>
      </table>
      <p>Savings Leeway: {{savingsLeeway}}</p>
      <div id="button-container">
        <!-- <button class="budget-button" name="back" value="back">Back</button> -->
        <!-- <button class="budget-button" name="edit" value="edit">Edit</button> -->
        <button class="budget-submit-button" form="budget-input-form" type="submit" name="submit" value="submit">Submit</button>
      </div>
    </form>
  </div>
</template>

<script>

export default {
  name: "BudgetInput",
  props: {
  },
  data() {
    return {
      userBudget : {},
      runningGroceries: '',
      runningBills: '',
      runningTransport: '',
      runningMisc: '',
      savingsLeeway: '',
      editField: '',
      form: {
        groceries_alloc: '',
        bills_alloc: '',
        transport_alloc: '',
        misc_alloc: '',
        savings_target: '',
        monthly_income: ''
      }
    }
  },
  mounted() {
    const groceries_id = 1;
    const transport_id = 2;
    const misc_id = 3;
    const bills_id = 4;
    this.monthlyIncome = 200000;
    this.runningGroceries = this.$store.state.expensesList.filter(element => element.category_id = groceries_id)
                                                          .reduce((accumulator, currentElement) => accumulator + currentElement.amount, 0);
    this.allocatedGroceries = 0;
    this.runningBills = this.$store.state.expensesList.filter(element => element.category_id = bills_id)
                                                      .reduce((accumulator, currentElement) => accumulator + currentElement.amount, 0);
    this.allocatedBills = 0;
    this.runningTransport = this.$store.state.expensesList.filter(element => element.category_id = transport_id)
                                                          .reduce((accumulator, currentElement) => accumulator + currentElement.amount, 0);
    this.allocatedTransport = 0;
    this.runningMisc = this.$store.state.expensesList.filter(element => element.category_id = misc_id)
                                                     .reduce((accumulator, currentElement) => accumulator + currentElement.amount, 0);
    this.allocatedMisc = 0;
    this.savingsTarget = 10000;
    this.savingsLeeway = 110000;
  },
  methods: {
    focusField(name) {
      this.editField = name;
    },
    showField(name) {
      return (this.form[name] == '' || this.editField == name)
    },
    blurField() {
      this.editField = '';
    },
    getUserBudgetInput() {
      axios.patch('/api/users/:id/budget', this.form)
           .then((res) => {

           })
           .catch((error) => {
             console.alert(error);
           })
    }
  }
}
</script>

<style scoped>

</style>