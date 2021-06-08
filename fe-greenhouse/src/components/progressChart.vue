<script>
import { Doughnut } from "vue-chartjs";

export default {
  extends: Doughnut,
  props: {
    savingsScore: Number,
  },
  name: "ProgressChart",
  data: () => ({
    chartOptions: {},
  }),
  methods: {
    setChartData(savingsScore) {
      this.chartData = {
        labels: ["Used", "Savings"],
        datasets: [
          {
            label: "First Dataset",
            backgroundColor: ["rgb(245,133,63)", "rgb(111,176,42)"],
            borderColor: ["rgba(255,255,255,0)", "rgba(255,255,255,0)"],
            data: [Number(savingsScore), Number(1 - savingsScore)],
          },
        ],
      };
    },
  },
  mounted() {
    this.setChartData(this.$props.savingsScore);
    this.chartOptions = {
      type: "doughnut",
      legend: {
        display: false,
      },
      plugins: {
        title: {
          display: true,
          text: "Test donut chart",
        },
      },
    };
    this.renderChart(this.chartData, this.chartOptions);
  },
  // watch: Vue.js function which forces the refresh when props value changes
  // (otherwise a change in props do not trigger a chart refresh)
  watch: {
    savingsScore: function (newVal, oldVal) {
      console.log(`Props changed! Old val = ${oldVal}, newVal = ${newVal}`);
      this.setChartData(this.$props.savingsScore);
      if (this.$data._chart) {
        this.$data._chart.destroy();
      }
      this.renderChart(this.chartData, this.chartOptions);
    },
  },
};
</script>

<style>
.chartContainer {
  width: 80%;
  max-width: 350px;
}
</style>
