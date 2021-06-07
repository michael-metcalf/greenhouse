<template>
  <div id="footer-button-container">
    <button class="footer-button" name="profile" value="profile">😀</button>
    <button class="footer-button" name="expense-input" value="expense-input">
      💲
    </button>
    <button class="footer-button" name="monthly-budget" value="monthly-budget">
      📆
    </button>
    <button class="footer-button" name="eco-goals" value="eco-goals">🌍</button>
    <button class="footer-button" name="logout" value="logout">👋</button>
  </div>
</template>

<script>
export default {
  name: "FooterNav",
  props: {},
  methods: {},
};
</script>

<style scoped>
#footer-button-container {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  padding: 10px;
}

.footer-button {
  font-size: 2em;
  min-width: 60px;
  min-height: 60px;
  padding: 5px;
  text-align: center;
  border-radius: 12%;
  border: 2px solid red;
}
</style>
