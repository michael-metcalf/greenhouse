<template>
  <div class="eco-goals-container">
    <p id="eco-goals">
      Your Eco Actions: <i id="sprout" class="fas fa-seedling"></i>
         {{ ecoScoreString }}
    </p>
    <p id="customerMessage">{{ customerMessage }}</p>
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

    const allMessages = [
      "You are doing great!",
      "The planet says thank you!",
      "We can do this!",
      "Be the change you want to see in the world.",
    ];
    this.customerMessage =
      allMessages[Math.floor(Math.random() * allMessages.length)];
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
  font-weight: bolder;
}
#customerMessage {
  font-weight: bolder;
  font-size: smaller;
}

#sprout {
  color: green;
}
</style>
