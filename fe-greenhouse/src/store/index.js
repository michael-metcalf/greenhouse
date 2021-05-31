import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    // DO NOT MODIFY THOSE!!!
    myTextColor: "blue",
    expensesList: [],
    ecoActionsList: [],
    monthlyBudget: {},
  },
  mutations: {
    setMyTextColor(state, payload) {
      state.myTextColor = payload;
    },
    setExpensesList(state, payload) {
      state.expensesList = [...payload.expensesList];
    },
    setEcoActionsList(state, payload) {
      state.ecoActionsList = payload.ecoActionsList;
    },
    setMonthlyBudget(state, payload) {
      state.monthlyBudget = payload.monthlyBudget;
    },
  }, // Use mutations to modify the state variables synchronously
  actions: {}, // For asynchronous functions, called with this.$store.dispatch()
  // Actions cannot modify state variables. They need to call the mutations
  modules: {},
});
