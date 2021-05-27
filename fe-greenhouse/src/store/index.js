import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    // DO NOT MODIFY THOSE!!!
    myTextColor: "blue",
  },
  mutations: {
    setMyTextColor(state, payload) {
      state.myTextColor = payload;
    },
  }, // Use mutations to modify the state variables synchronously
  actions: {}, // For asynchronous functions, called with this.$store.dispatch()
  // Actions cannot modify state variables. They need to call the mutations
  modules: {},
});
