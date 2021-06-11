<template>
  <div>
    <h1>Eco Progress</h1>
    <div>
      <BarChart />
    </div>
    <p id="disclaimer">*Eco actions are shown as a percentage of expenses.</p>
    <p>I have used my own bag or not used a bag {{ ecoBagActionTotal }}% of the time this month.</p>
    <p>I did not impulse shop {{ noImpulseBuyActionTotal }}% of the time this month.</p>
    <p>I took eco conscious transport or walked {{ transportActionTotal }}% of the time month.</p>
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
    }
  },
  methods: {
    getEcoBagActionTotal() {
      console.log("I have been called");
      let bagActionArray = this.ecoActionsList.filter(
        (element) => element.eco_goal_id == 1
      );
      this.ecoBagActionTotal = (bagActionArray.length / this.ecoActionsList.length) * 100;
    },
    getNoImpulseBuyActionTotal() {
      let noImpulseBuyActionArray = this.ecoActionsList.filter(
          (element) => element.eco_goal_id == 2
      );
      this.noImpulseBuyActionTotal = (noImpulseBuyActionArray.length / this.ecoActionsList.length) * 100
    },
    getTransportActionTotal() {
      let transportActionArray = this.ecoActionsList.filter(
          (element) => element.eco_goal_id == 3
      );
      this.transportActionTotal = (transportActionArray.length / this.ecoActionsList.length) * 100;
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
</style>
