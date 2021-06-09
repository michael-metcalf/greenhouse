<template>
  <div class="eco-goals-container">
    <p id="eco-goals">
      Eco Goals: <i id="sprout" class="fas fa-seedling"></i>
      x {{ ecoScoreString }}
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
    console.log(`Props - eco score ${this.ecoScore}`);
    // const numberOfSprouts = this.ecoScore;
    this.ecoScoreString = 0;
    this.echoScoreString = this.$store.state.ecoActionsList
      .filter((element) => element.eco_goal_id == 1)
      .length;
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
  margin-top: 5px;
  margin-bottom: 5px;
  margin-left: 10px;
  margin-right: 10px;
  background-color: rgba(255, 255, 255, 0.5);
  border-radius: 10px;
}

#eco-goals {
  font-weight: bold;
}

#sprout {
  color: green;
}
</style>
