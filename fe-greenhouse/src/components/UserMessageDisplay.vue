<template>
  <div class="userMessage">
    <p v-bind:class="classObject">
      {{ this.$store.state.userMessage.message }}
    </p>
  </div>
</template>

<script>
export default {
  name: "UserMessageDisplay",
  data: () => ({}),
  computed: {
    classObject: function () {
      return {
        error:
          this.$store.state.userMessage.msgType === "error" &&
          this.$store.state.userMessage !== "",
      };
    },
  },
};
</script>

<style scoped>
div.userMessage {
  margin-top: 1em;
  margin-bottom: 1em;
  padding: 0.5em;
}

p.error {
  color: black;
  background-color: lightcoral;
}

p.warning {
  background-color: lightyellow;
}
</style>
