<template>
  <div>
    <h1>Eco Progress</h1>
    <div>
      <BarChart />
    </div>
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

<style scoped></style>
