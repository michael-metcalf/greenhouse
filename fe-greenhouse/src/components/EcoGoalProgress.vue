<template>
  <div class="eco-goals-container">
    <p id="eco-goals">Eco Goals:  {{ecoScoreString}} </p>
    <p> {{ customerMessage}} </p>
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
      ecoScoreString: '',
      customerMessage: '',
    }
  },
  mounted() {
    console.log(`Props - eco score ${this.ecoScore}`)
    const numberOfSprouts = this.ecoScore;
    this.ecoScoreString = '';
    for (let i=0; i<numberOfSprouts; i++) {
      this.ecoScoreString += '🌱';
    }
    switch(numberOfSprouts) {
      case 0:
        this.customerMessage = 'Could do better?';
        break;
      case 1:
        this.customerMessage = 'Just one!';
        break;
      case 2:
        this.customerMessage = 'Just a little bit more';
        break;
      case 3:
        this.customerMessage = 'On track!';
        break;
      case 4:
        this.customerMessage = 'Thanks for the earth!';
        break;
      case 5:
        this.customerMessage = 'PERFECT!!!';
        break;
      default:
        this.customerMessage = 'You\'re on track!';
    }
  }
}
</script>

<style scoped>

.eco-goals-container {
  border: 2px solid red;
  margin-bottom: 10px;
}

#eco-goals {
  font-weight: bold;
}

</style>