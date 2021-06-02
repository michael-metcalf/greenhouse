import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    // DO NOT MODIFY THOSE!!!
    myTextColor: "blue",
    userName: "",
    isLoading: true,
    expensesList: [],
    ecoActionsList: [],
    ecoGoalsList: [],
    monthlyBudget: {},
  },
  mutations: {
    setUserName(state, payload) {
      state.userName = payload.userName;
    },
    clearUserName(state) {
      state.userName = "";
      state.isLoading = true;
    },
    setLoadingStatus(state, payload) {
      if (typeof payload === "boolean") {
        state.isLoading = payload;
      } else {
        state.isLoading = payload.isLoading;
      }
    },
    setMyTextColor(state, payload) {
      state.myTextColor = payload;
    },
    setExpensesList(state, payload) {
      state.expensesList = [...payload.expensesList];
    },
    setEcoActionsList(state, payload) {
      state.ecoActionsList = payload.ecoActionsList;
    },
    setEcoGoalsList(state, payload) {
      state.ecoGoalsList = payload.ecoGoalsList;
    },
    setMonthlyBudget(state, payload) {
      state.monthlyBudget = payload.monthlyBudget;
    },
  }, // Use mutations to modify the state variables synchronously
  actions: {
    // updateBudget(state, payload) {
    //   try {
    //     axios.
    //   } catch (error) {
        
    //   }  
    }
  }, // For asynchronous functions, called with this.$store.dispatch()
  // Actions cannot modify state variables. They need to call the mutations
  modules: {},
});
