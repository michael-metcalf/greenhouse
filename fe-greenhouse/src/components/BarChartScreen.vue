<template>
  <div>
    <h1>Your Eco Progress</h1>
    <div>
      <BarChart />
    </div>
    <p id="disclaimer">*Eco actions are shown as a percentage of monthly expenses.</p>
    <p>I have used my own bag or not used a bag <span class="percent-1">{{ ecoBagActionTotal }}%</span> of the time this month.</p>
    <p>I did not impulse shop <span class="percent-2">{{ noImpulseBuyActionTotal }}%</span> of the time this month.</p>
    <p>I took eco-conscious transport or walked <span class="percent-3">{{ transportActionTotal }}%</span> of the time month.</p>
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
p {
  font-weight: bold;
}
.percent-1 {
  color: #004D48;
}
.percent-2 {
  color: #00716A;
}
.percent-3 {
  color: #00968C;
}
</style>
