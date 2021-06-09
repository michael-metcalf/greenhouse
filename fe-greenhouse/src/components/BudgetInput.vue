<template>
  <div id="budget-input-container">
    <div id="budget-input-form">
      <p>
        <span class="income">Monthly Income:</span>
        <span
          class="field-value"
          v-show="!showField('monthlyIncome')"
          @click="focusField('monthlyIncome')"
        >
          {{ form.monthlyIncome }}
        </span>
        <input
          v-model="form.monthlyIncome"
          v-show="showField('monthlyIncome')"
          id="monthly-income"
          type="text"
          class="field-value form-control"
          @focus="focusField('monthlyIncome')"
          @blur="blurField"
        />
        <i class="fas fa-edit"></i>
      </p>
      <div id="budget-input-grid">
        <div></div>
        <div class="grid-col-header" id="running">Running Total</div>
        <div class="grid-col-header">Amount Allocated</div>
        <div class="grid-row-header">Groceries</div>
        <div class="grid-content">{{ runningGroceries }}</div>
        <div class="grid-content-2">
          <span
            class="field-value"
            v-show="!showField('allocatedGroceries')"
            @click="focusField('allocatedGroceries')"
            >{{ form.allocatedGroceries }}</span
          >
          <input
            v-model="form.allocatedGroceries"
            v-show="showField('allocatedGroceries')"
            id="allocated-groceries"
            type="text"
            class="field-value form-control"
            @focus="focusField('allocatedGroceries')"
            @blur="blurField"
            maxlength="15"
          />
          <i class="fas fa-edit"></i>
        </div>
        <div class="row-header">Bills</div>
        <div class="grid-content">{{ runningBills }}</div>
        <div class="grid-content-2">
          <span
            class="field-value"
            v-show="!showField('allocatedBills')"
            @click="focusField('allocatedBills')"
            >{{ form.allocatedBills }}</span
          >
          <input
            v-model="form.allocatedBills"
            v-show="showField('allocatedBills')"
            id="allocated-bills"
            type="text"
            class="field-value form-control"
            @focus="focusField('allocatedBills')"
            @blur="blurField"
            maxlength="15"
          />
          <i class="fas fa-edit"></i>
        </div>
        <div class="row-header">Transport</div>
        <div class="grid-content">{{ runningTransport }}</div>
        <div class="grid-content-2">
          <span
            class="field-value"
            v-show="!showField('allocatedTransport')"
            @click="focusField('allocatedTransport')"
            >{{ form.allocatedTransport }}</span
          >
          <input
            v-model="form.allocatedTransport"
            v-show="showField('allocatedTransport')"
            id="allocated-transport"
            type="text"
            class="field-value form-control"
            @focus="focusField('allocatedTransport')"
            @blur="blurField"
            maxlength="15"
          />
          <i class="fas fa-edit"></i>
        </div>
        <div class="row-header">Misc</div>
        <div class="grid-content">{{ runningMisc }}</div>
        <div class="grid-content-2">
          <span
            class="field-value"
            v-show="!showField('allocatedMisc')"
            @click="focusField('allocatedMisc')"
            >{{ form.allocatedMisc }}</span
          >
          <input
            v-model="form.allocatedMisc"
            v-show="showField('allocatedMisc')"
            id="allocated-misc"
            type="text"
            class="field-value form-control"
            @focus="focusField('allocatedMisc')"
            @blur="blurField"
            maxlength="15"
          />
          <i class="fas fa-edit"></i>
        </div>
        <div class="row-header big-row two-columns">Savings Target</div>
        <div class="grid-content big-row">
          <span
            class="field-value"
            v-show="!showField('savingsTarget')"
            @click="focusField('savingsTarget')"
            >{{ form.savingsTarget }}</span
          >
          <input
            v-model="form.savingsTarget"
            v-show="showField('savingsTarget')"
            id="savings-target"
            type="text"
            class="field-value form-control"
            @focus="focusField('savingsTarget')"
            @blur="blurField"
            maxlength="15"
          />
          <i class="fas fa-edit"></i>
        </div>
      </div>

      <p><span class="savings">Savings Leeway:</span> {{ this.savingsLeeway }}</p>
      <div id="button-container">
        <button
          @click="patchUserBudgetInput"
          class="budget-submit-button"
          form="budget-input-form"
        >
          Update Budget
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "BudgetInput",
  props: {},
  data() {
    return {
      userBudget: {},
      runningGroceries: "",
      runningBills: "",
      runningTransport: "",
      runningMisc: "",
      savingsLeeway: "",
      editField: "",
      allocatedTotal: "",
      monthlyBudget: "",
      form: {
        allocatedGroceries: this.$store.state.monthlyBudget.groceries_alloc,
        allocatedBills: this.$store.state.monthlyBudget.bills_alloc,
        allocatedTransport: this.$store.state.monthlyBudget.transport_alloc,
        allocatedMisc: this.$store.state.monthlyBudget.misc_alloc,
        savingsTarget: this.$store.state.monthlyBudget.savings_target,
        monthlyIncome: this.$store.state.monthlyBudget.monthly_income,
      },
    };
  },
  mounted() {
    const groceries_id = 1;
    const transport_id = 2;
    const misc_id = 3;
    const bills_id = 4;
    this.monthlyIncome = 0;
    this.runningGroceries = this.$store.state.expensesList
      .filter((element) => element.category_id == groceries_id)
      .reduce(
        (accumulator, currentElement) => accumulator + currentElement.amount,
        0
      );
    this.allocatedGroceries = 0;
    this.runningBills = this.$store.state.expensesList
      .filter((element) => element.category_id == bills_id)
      .reduce(
        (accumulator, currentElement) => accumulator + currentElement.amount,
        0
      );
    this.allocatedBills = 0;
    this.runningTransport = this.$store.state.expensesList
      .filter((element) => element.category_id == transport_id)
      .reduce(
        (accumulator, currentElement) => accumulator + currentElement.amount,
        0
      );
    this.allocatedTransport = 0;
    this.runningMisc = this.$store.state.expensesList
      .filter((element) => element.category_id == misc_id)
      .reduce(
        (accumulator, currentElement) => accumulator + currentElement.amount,
        0
      );
    this.allocatedMisc = 0;
    this.savingsTarget = 0;
    this.savingsLeeway =
      Number(this.form.monthlyIncome) -
      Number(this.form.savingsTarget) -
      (Number(this.form.allocatedGroceries) +
        Number(this.form.allocatedBills) +
        Number(this.form.allocatedTransport) +
        Number(this.form.allocatedMisc));
  },
  methods: {
    focusField(name) {
      this.editField = name;
    },
    showField(name) {
      // showField returns TRUE if UI has to show the field whose name is passed in parameter
      // Function used in conjunction with vue directive v-show
      // https://vuejs.org/v2/api/#v-show
      return this.form[name] == "" || this.editField == name;
    },
    blurField() {
      this.editField = "";
    },
    getSavingsLeeway() {
      return (
        Number(this.form.monthlyIncome) -
        Number(this.form.savingsTarget) -
        (Number(this.form.allocatedGroceries) +
          Number(this.form.allocatedBills) +
          Number(this.form.allocatedTransport) +
          Number(this.form.allocatedMisc))
      );
    },
    patchUserBudgetInput() {
      this.savingsLeeway = this.getSavingsLeeway();

      this.$store.dispatch("updateBudget", {
        user_id: this.$store.state.user.user_id,
        monthly_budget: this.form.monthlyIncome,
        groceries_alloc: this.form.allocatedGroceries,
        bills_alloc: this.form.allocatedBills,
        transport_alloc: this.form.allocatedTransport,
        misc_alloc: this.form.allocatedMisc,
        savings_target: this.form.savingsTarget,
        monthly_income: this.form.monthlyIncome,
      });
    },
  },
};
</script>

<style scoped>
#monthly-income {
  font-weight: bold;
}
#savings-target {
  color: green;
  font-weight: bold;
}

#budget-input-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1.8fr;
  gap: 10px 0;
}

.big-row {
  margin-top: 1.3em;
  margin-left: 22px;
  width: 200px;
}

.two-columns {
  grid-column: span 2 / auto;
}

#budget-input-grid > input {
  max-width: 40px;
  color: red;
}

.budget-submit-button {
  height: 2em;
  font-size: large;
  border-radius: 5px;
  background-color: #403d58;
  color: white;
  width: 150px;
}

.grid-row-header, .row-header {
  width: 100px;
  text-align: left;
  padding: 2px;
  margin-left: 30px;
  font-weight: bold;
  /* border: 1px solid black; */
}

.grid-col-header, .income, .savings {
  font-weight: bold;
  padding: 10px;
  width: 100;
  /* border: 1px solid black; */
}

.grid-content {
  width: 150px;
  justify-content: center;
}

.fas {
  padding-left: 20px;
}

/* .grid-content {
  width: 50px;
}

.field-value {
  width: 100px;
} */
</style>
