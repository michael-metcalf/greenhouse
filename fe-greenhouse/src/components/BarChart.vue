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
            label: "My Eco Goal Progress (as a percentage of total expenses)",
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
    this.ecoActionsList = this.$store.state.ecoActionsList;
    this.getEcoBagActionTotal = () => {
      let bagActionArray = this.ecoActionsList.filter(element => element.eco_goal_id == 1);
      return (bagActionArray.length/this.ecoActionsList.length) * 100;
    },
    this.getNoImpulseBuyActionTotal = () => {
      let noImpulseBuyActionArray = this.ecoActionsList.filter(element => element.eco_goal_id == 2);
      return (noImpulseBuyActionArray.length/this.ecoActionsList.length) * 100;
    },
    this.getTransportActionTotal = () => {
      let transportActionArray = this.ecoActionsList.filter(element => element.eco_goal_id == 3);
      return (transportActionArray.length/this.ecoActionsList.length) * 100;
    },
    this.setChartData();
    this.chartOptions = {
      scales: {
        yAxes: [{
          ticks: {
            min: 0,
            max: 100,
            beginAtZero: true,
          } 
        }]
      },
    };
    this.renderChart(this.setChartData, this.chartOptions);
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