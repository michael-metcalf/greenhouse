import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    // DO NOT MODIFY THESE!!!
    myTextColor: "blue",
    userName: "",
    user: {},
    isLoading: true,
    isAuthenticated: false,
    expensesList: [],
    ecoActionsList: [],
    ecoGoalsList: [],
    categoriesList: [],
    monthlyBudget: {},
    userMessage: { message: "", msgType: "" },
  },
  mutations: {
    setUser(state, payload) {
      state.user = payload;
    },
    setUserName(state, payload) {
      state.userName = payload;
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
    setUserMessage(state, payload) {
      state.userMessage = payload;
    },
    setAuthenticated(state, payload) {
      state.isAuthenticated = payload;
    },
    setCategoriesList(state, payload) {
      state.categoriesList = payload;
    },
  }, // Use mutations to modify the state variables synchronously
  actions: {
    async verifyLogin({ commit, dispatch }, payload) {
      try {
        const res = await axios.post("/api/user/login", payload);
        console.log(res);
        if (res.data.error === -1) {
          commit("setUserMessage", {
            message: "Could not login",
            msgType: "error",
          });
        } else {
          commit("setUserName", res.data.username);
          commit("setUser", res.data);
          dispatch("receiveLoginSignal");
        }
          const res = await axios.post("/api/user/login", payload)
          if (res.data.error === -1) { 
            commit("setUserMessage", {message: "Could not login", msgType: "error" })                    
          } else {
            commit("setUserName", res.data.username)
            commit("setUser", res.data)
            dispatch("receiveLoginSignal")
          }
      } catch (err) {
        console.error(err);
      }
    },

    async receiveLoginSignal({ commit, state }) {
    async receiveLoginSignal({commit, dispatch, state}) {
      // Need to download the data related to the current user
      console.log(`Received login signal...${state.userName}`);
      commit("setLoadingStatus", true);
      try {
        const api_address = "/api/";
        const budget_response = await axios.get(
          `${api_address}user/${state.user.user_id}/user_budget`
        );
        console.log(`Monthly budget : ${JSON.stringify(budget_response.data)}`);
        commit("setMonthlyBudget", { monthlyBudget: budget_response.data });
        const expenses_response = await axios.get(
          `${api_address}user/${state.user.user_id}/expenses`
        );
        console.log(`Expenses list: ${JSON.stringify(expenses_response.data)}`);
        commit("setExpensesList", {
          expensesList: expenses_response.data.expenses,
        });
        const eco_goals_response = await axios.get(
          `${api_address}user/${state.user.user_id}/eco_goals`
        );
        console.log(
          `Eco Goals list: ${JSON.stringify(eco_goals_response.data)}`
        );
        if (eco_goals_response.data.eco_goals) {
          commit("setEcoGoalsList", {
            ecoGoalsList: eco_goals_response.data.eco_goals,
          });
        }
        const eco_actions_response = await axios.get(
          `${api_address}user/${state.user.user_id}/eco_actions`
        );
        if (eco_actions_response.data.eco_actions) {
          commit("setEcoActionsList", {
            ecoActionsList: eco_actions_response.data.eco_actions,
          });
        }
        const categories_response = await axios.get(
          `${api_address}user/${state.user.user_id}/categories`
        );
        if (categories_response.data.categories) {
          commit("setCategoriesList", {
            categoriesList: categories_response.data.categories,
          });
        }
        commit("setLoadingStatus", false);
        commit("setAuthenticated", true);
      } catch (err) {
        console.error(`ERROR in the back-end API download! ${err}`);
      }
    },
  },
       
        await dispatch("getBudgets")
        await dispatch("getExpenses")
        await dispatch("getEcoGoals")
        await dispatch("getEcoActions")
        await dispatch("getCategories")

        commit("setLoadingStatus", false);
        commit("setAuthenticated", true)   
        console.log("setLoading and setAuthenticated is done")           
      } catch(err) {
        console.error(`ERROR in the back-end API download! ${err}`);
      }
    },

    async createExpense({ dispatch, state }, payload) {
      try {
        const res = await axios.post(`/api/user/${state.user.user_id}/expense`, payload)
        console.log(res.data)
        dispatch("getExpenses")        
      } catch (err) {
        console.error(`ERROR in createExpense! ${err}`); 
      }
    },

    async updateExpense({ dispatch, state }, payload) {
      try {
        await axios.patch(`/api/user/${state.user.user_id}/expenses`, payload)
        dispatch("getExpenses")                
      } catch (err) {
        console.error(`ERROR in updateExpense ${err}`)
      }
    },

    async getExpenses({ commit, state }) {
      try {
        const res = await axios.get(`/api/user/${state.user.user_id}/expenses`)
        commit("setExpensesList", { expensesList: res.data.expenses });        
      } catch (err) {
        console.error(`ERROR in getExpenses ${err}`)
      }
    },

    async updateBudget({dispatch, state}, payload) {
      try {
        await axios.patch(`/api/user/${state.user.user_id}/user_budget`, payload)
        dispatch("getBudgets")
      } catch (err) {
        console.error(`ERROR in updateBudget ${err}`)
      }
    },

    async getBudgets({commit, state}) {
      try {
        const res = await axios.get(`/api/user/${state.user.user_id}/user_budget`);
        commit("setMonthlyBudget", { monthlyBudget: res.data });
        console.log("THIS IS WHEN THE API CALL IS SETTING MONTHLY INCOME", state.monthlyBudget.monthly_income)
      } catch (err) {
        console.error(`ERROR in the getBudgets ${err}`)
      }
    },

    async getEcoGoals({ commit, state }) {
      try {
        const res = await axios.get(`/api/user/${state.user.user_id}/eco_goals`)
        if(res.data.eco_goals) {
          commit("setEcoGoalsList", { ecoGoalsList: res.data.eco_goals });
        }
      } catch (err) {
        console.error(`ERROR in the getEcoGoals ${err}`)
      }
    },

    async getEcoActions({ commit, state }) {
      try {
        const res = await axios.get(`/api/user/${state.user.user_id}/eco_actions`)
        if(res.data.eco_actions) {
          commit("setEcoActionsList", { ecoActionsList: res.data.eco_actions });
        }
      } catch (err) {
        console.error(`ERROR in the getEcoGoals ${err}`)
      }
    },
  
    async getCategories({ commit, state }) {
      try {
        const res = await axios.get(`/api/user/${state.user.user_id}/categories`);
        if (res.data.categories) {
          commit("setCategoriesList", { categoriesList: res.data.categories})
        }        
      } catch (err) {
        console.error(`ERROR in the getCategories ${err}`)
      }
    }

  }
});
