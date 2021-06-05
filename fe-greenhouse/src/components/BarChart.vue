<script>
import { Bar } from "vue-chartjs";

export default {
  extends: Bar,
  props: {},
  name: "EcoActionsProgress",
  data: () => ({
    chartOptions: {},
  }),
  methods: {
    setChartData() {
      this.setChartData = {
        labels: ["Eco-bag/No bag", "No impulse purchase", "Eco-conscious transport"],
        datasets: [
          {
            label: "My Eco Goal Progress",
            barPercentage: 1,
            barThickness: 50,
            data: [
              this.getEcoBagActionTotal(),
              this.getNoImpulseBuyActionTotal(),
              this.getTransportActionTotal(),
            ],
            backgroundColor: [
              "rgb(25,25,255)",
              "rgb(25,25,255)",
              "rgb(25,25,255)",
            ],
            borderColor: [
              "rgb(255, 99, 132)",
            ]
          },
        ]
      }
    }
  },
  mounted() {
    this.getEcoBagActionTotal = () => {
      let bagActionTotal = 0;
      let bagActionArray = this.$store.state.ecoActionsList.filter(element => element.eco_goal_id == 1)
      for (let i = 0; i < bagActionArray.length; i++) {
        bagActionTotal++;
      }
      return bagActionTotal;
    },
    this.getNoImpulseBuyActionTotal = () => {
      let noImpulseBuyActionTotal = 0;
      let noImpulseBuyActionArray = this.$store.state.ecoActionsList.filter(element => element.eco_goal_id == 2)
      for (let i = 0; i < noImpulseBuyActionArray.length; i++) {
        noImpulseBuyActionTotal++;
      }
      return noImpulseBuyActionTotal;
    },
    this.getTransportActionTotal = () => {
      let transportActionTotal = 0;
      let transportActionArray = this.$store.state.ecoActionsList.filter(element => element.eco_goal_id == 3)
      for (let i = 0; i < transportActionArray.length; i++) {
        transportActionTotal++;
      }
      return transportActionTotal;
    },
    this.setChartData();
    this.chartOptions = {
      type: "bar",
      options: {
        scales: {
          y: {
            min: 0,
            max: 100,
            beginAtZero: true,
          },
        },
      },
    },
    this.renderChart(this.setChartData, this.chartOptions)
  },
  watch: {
    savingsScore: function (newVal, oldVal) {
      console.log(`Props changed! Old val = ${oldVal}, newVal = ${newVal}`);
      this.setChartData(this.$props.savingsScore);
      if (this.$data._chart) {
        this.$data._chart.destroy();
      }
      this.renderChart(this.setChartData, this.chartOptions);
    },
  },
}
</script>

<style scoped>
  .chartContainer {
  width: 80%;
  max-width: 350px;
}
</style>