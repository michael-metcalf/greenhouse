<template>
  <div class="env-fact-container">
    <p>
      <span class="did-you-know-header">Did you know?</span>
      <br />
      <span class="env-fact">An env fact from the array</span>
    </p>
  </div>
</template>

<script>
  let environmentalFactArray = [
    "35% of food is thrown away.", 
    "27,000 trees are cut down each day so we can have toilet paper.", 
    "Aluminium can be recycled continuously.", 
    "200 species of plant, insect, bird and mammal go extinct every 24 hours.", 
    "Recycling one aluminium can save enough energy to run a TV for 3 hours.", 
    "Rainforests are being cut down at a rate of 100 acres a minute.",
    "As of 2021, there is an estimated 78 years until the end of rainforests.",
    "As of 2021, there is an estimated 18 years until the world runs out of freshwater.",
  ];

export default {
  name: "EnvironmentalFact",
  props: {
    msg: String,
  },
  methods: {
  },
  mounted() {
    console.log(environmentalFactArray[0]);
  }
  
};
</script>  

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.did-you-know-header {
  font-size: larger;
  font-weight: strong;
}

</style>