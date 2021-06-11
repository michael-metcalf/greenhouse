<template>
  <div>
    <h1>Eco Progress</h1>
    <div>
      <BarChart />
    </div>
    <p id="disclaimer">*Eco actions are shown as a percentage of expenses.</p>
    <p>
      I have used my own bag or not used a bag
      <span class="percent">{{ ecoBagActionTotal }}%</span> of the time this
      month.
    </p>
    <p>
      I did not impulse shop
      <span class="percent">{{ noImpulseBuyActionTotal }}%</span> of the time
      this month.
    </p>
    <p>
      I took eco conscious transport or walked
      <span class="percent">{{ transportActionTotal }}%</span> of the time
      month.
    </p>
  </div>
</template>

<script>
import BarChart from "./BarChart.vue";

export default {
  name: "BarChartScreen",
  components: {
    BarChart,
  },
  data() {
    return {
      ecoBagActionTotal: null,
      noImpulseBuyActionTotal: null,
      transportActionTotal: null,
      ecoActionsList: this.$store.state.ecoActionsList,
    };
  },
  methods: {
    getEcoBagActionTotal() {
      let bagActionArray = this.ecoActionsList.filter(
        (element) => element.eco_goal_id == this.$store.state.ecoGoalsList.filter( (ecoGoalObj) => ecoGoalObj.goal_name === "Eco bag/no bag")[0].id
      );
      this.ecoBagActionTotal = Math.floor(
        (bagActionArray.length / this.ecoActionsList.length) * 100
      );
    },
    getNoImpulseBuyActionTotal() {
      let noImpulseBuyActionArray = this.ecoActionsList.filter(
        (element) => element.eco_goal_id == this.$store.state.ecoGoalsList.filter( (ecoGoalObj) => ecoGoalObj.goal_name === "No impulse purchase")[0].id
      );
      this.noImpulseBuyActionTotal = Math.floor(
        (noImpulseBuyActionArray.length / this.ecoActionsList.length) * 100
      );
    },
    getTransportActionTotal() {
      let transportActionArray = this.ecoActionsList.filter(
        (element) => element.eco_goal_id == this.$store.state.ecoGoalsList.filter( (ecoGoalObj) => ecoGoalObj.goal_name === "Eco conscious tranport")[0].id
      );
      this.transportActionTotal = Math.floor(
        (transportActionArray.length / this.ecoActionsList.length) * 100
      );
    },
  },
  mounted() {
    this.getEcoBagActionTotal();
    this.getNoImpulseBuyActionTotal();
    this.getTransportActionTotal();
  },
};
</script>

<style scoped>
#disclaimer {
  font-size: 12px;
}
.percent {
  font-weight: bold;
  color: teal;
}
</style>
