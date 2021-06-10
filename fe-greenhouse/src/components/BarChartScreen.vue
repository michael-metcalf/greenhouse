<template>
  <div>
    <h1>Eco Progress</h1>
    <div>
      <BarChart />
    </div>
    <p>*Eco actions are shown as a percentage of expenses.</p>
  </div>
</template>

<script>
import BarChart from "./BarChart.vue";

export default {
  name: "BarChartScreen",
  components: {
    BarChart,
  },
};
</script>

<style scoped>
p {
  font-size: 12px;
}
</style>
