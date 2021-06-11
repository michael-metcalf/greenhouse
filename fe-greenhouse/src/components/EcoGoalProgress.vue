<template>
  <div class="eco-goals-container">
    <p id="eco-goals">
      Eco Goals: <i id="sprout" class="fas fa-seedling"></i>
         {{ ecoScoreString }}
    </p>
    <p>{{ customerMessage }}</p>
  </div>
</template>

<script>
export default {
  name: "EcoGoalProgress",
  props: {
    ecoScore: Number,
  },
  data: () => {
    return {
      ecoScoreString: 0,
      customerMessage: "",
    };
  },
  mounted() {
    const externalScript = document.createElement("script");
    externalScript.setAttribute(
      "src",
      "https://kit.fontawesome.com/e3cbc00358.js"
    );
    externalScript.setAttribute("crossorigin", "anonymous");
    document.head.appendChild(externalScript);
    // const numberOfSprouts = this.ecoScore;
    this.ecoScoreString = 0;
    this.ecoScoreString = this.$store.state.ecoActionsList.filter(
      (element) =>
        element.eco_goal_id == 1 ||
        element.eco_goal_id == 2 ||
        element.eco_goal_id == 3
    ).length;
    // for (let i = 0; i < numberOfSprouts; i++) {
    //   this.ecoScoreString += 1;
    // }
    // switch (numberOfSprouts) {
    //   case 0:
    //     this.customerMessage = "Could do better?";
    //     break;
    //   case 1:
    //     this.customerMessage = "Just one!";
    //     break;
    //   case 2:
    //     this.customerMessage = "Just a little bit more";
    //     break;
    //   case 3:
    //     this.customerMessage = "On track!";
    //     break;
    //   case 4:
    //     this.customerMessage = "Thanks for the earth!";
    //     break;
    //   case 5:
    //     this.customerMessage = "PERFECT!!!";
    //     break;
    //   default:
    //     this.customerMessage = "You're on track!";
    // }
  },
};
</script>

<style scoped>
.eco-goals-container {
  margin: 5px 10px;
  background-color: rgba(255, 255, 255, 0.5);
  border-radius: 10px;
  height: 100px;
 
}

#eco-goals {
  font-size: larger;
  font-weight: bold;
}

#sprout {
  color: green;
}
</style>
