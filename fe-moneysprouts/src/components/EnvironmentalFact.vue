<template>
  <div class="env-fact-container">
    <h2 class="did-you-know-header">Did you know?</h2>
    <p id="did-you-know-text">
      <span class="env-fact">{{ displayFact() }}</span>
    </p>
  </div>
</template>

<script>
let environmentalFactArray = [
  {
    source: "https://www.theworldcounts.com/",
    fact: "35% of food is thrown away.",
  },
  {
    source:
      "https://www.theworldcounts.com/stories/amazing_environmental_facts",
    fact: "27,000 trees are cut down each day so we can have toilet paper.",
  },
  {
    source:
      "https://www.theworldcounts.com/stories/amazing_environmental_facts",
    fact: "Aluminium cans can be recycled continuously.",
  },
  {
    source:
      "https://www.theworldcounts.com/stories/amazing_environmental_facts",
    fact: "200 species of plant, insect, bird and mammal go extinct every 24 hours.",
  },
  {
    source:
      "https://www.theworldcounts.com/stories/amazing_environmental_facts",
    fact: "Recycling one aluminium can save enough energy to run a TV for 3 hours.",
  },
  {
    source:
      "https://www.theworldcounts.com/stories/amazing_environmental_facts",
    fact: "Rainforests are being cut down at a rate of 100 acres a minute.",
  },
  {
    source:
      "https://www.theworldcounts.com/stories/amazing_environmental_facts",
    fact: "As of 2021, there is an estimated 78 years until the end of rainforests.",
  },
  {
    source:
      "https://www.theworldcounts.com/stories/amazing_environmental_facts",
    fact: "As of 2021, there is an estimated 18 years until the world runs out of freshwater.",
  },
  {
    source:
      "https://www.conservation.org/stories/11-climate-change-facts-you-need-to-know",
    fact: "Just 0.7% of the world's forests are coastal mangroves, but store up to 10x as much carbon as tropical forests.",
  },
  {
    source:
      "https://www.conservation.org/stories/11-climate-change-facts-you-need-to-know",
    fact: "It would cost $140 billion per year to make the changes humanity needs to adapt to a warming planet. That's less than 0.2% of global GDP.",
  },
  {
    source:
      "https://www.conservation.org/stories/11-climate-change-facts-you-need-to-know",
    fact: "11% of global greenhouse gas emissions caused by humans are due to deforestation. This is comparable to the emissions from all of the passenger vehicles on the planet.",
  },
  {
    source:
      "https://www.conservation.org/stories/11-climate-change-facts-you-need-to-know",
    fact: "The 5 warmest years between 1880 and 2019 have all occurred since 2015.",
  },
  {
    source:
      "https://www.conservation.org/stories/11-climate-change-facts-you-need-to-know",
    fact: "As of May 2020, the concentration of carbon dioxide in our atmosphere is the highest it has been in human history.",
  },
  {
    source:
      "https://www.conservation.org/stories/11-climate-change-facts-you-need-to-know",
    fact: "Natural climate change solutions can create more than 39 jobs per million dollars spent - 6 times more than the oil and gas industry.",
  },
  {
    source:
      "https://www.conservation.org/stories/11-climate-change-facts-you-need-to-know",
    fact: "Roughly 3.2 billion people are impacted by land degradation worldwide.",
  },
  {
    source:
      "https://www.conservation.org/stories/11-climate-change-facts-you-need-to-know",
    fact: "For every $1 spent in land restoration, an average of 10 times that amount in benefits is returned.",
  },
  {
    source:
      "https://www.wwf.org.uk/learn/fascinating-facts/bees#:~:text=Busy%20bees,than%20those%20that%20do%20not.",
    fact: "Almost 75% of leading global crops depend on animal pollinators like bees.",
  },
  {
    source:
      "https://www.wwf.org.uk/learn/fascinating-facts/bees#:~:text=Busy%20bees,than%20those%20that%20do%20not.",
    fact: "Almost 90% of wild plants depend on animal pollinators like bees.",
  },
  {
    source:
      "https://www.wwf.org.uk/learn/fascinating-facts/bees#:~:text=Busy%20bees,than%20those%20that%20do%20not.",
    fact: "Numbers of bees have declined by 60% in the US, this is commonly attributed to the use of neonicotinoid pesticides.",
  },
  {
    source: "https://www.theworldcounts.com/",
    fact: "1.3 billion tonnes of food is wasted globally every year.",
  },
  {
    source: "https://www.theworldcounts.com/",
    fact: "300 million tonnes of plastic waste is produced every year.",
  },
  {
    source:
      "https://populationmatters.org/population-numbers?gclid=Cj0KCQjw78yFBhCZARIsAOxgSx0OH4IpWKXUqoKawWUf5QuiV_8C1Iq_u0vLowSTvHGNB7ZJcOvH6PAaAqsLEALw_wcB",
    fact: "Since WW2 the global population has increased by 1 billion people every 12-15 years.",
  },
  {
    source: "https://ourworldindata.org/per-capita-co2",
    fact: "As of 2019, Australia, the US and Canada's per capita carbon footprint was more than 3 times higher than the global average.",
  },
];

export default {
  name: "EnvironmentalFact",
  props: {
    msg: String,
  },
  methods: {
    displayFact: function () {
      let randomFactIndex = Math.floor(
        Math.random() * environmentalFactArray.length
      );
      return environmentalFactArray[randomFactIndex].fact;
    },
  },
  mounted() {},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.did-you-know-header {
  font-size: larger;
  font-weight: strong;
}
.env-fact {
  font-weight: bolder;
  font-size: smaller !important;
}
.env-fact-container {
  border-radius: 5px;
  background-color: rgba(255, 255, 255, 0.5);
  padding-left: 5px;
  padding-right: 5px;
  margin: 5px 10px;
}
</style>
