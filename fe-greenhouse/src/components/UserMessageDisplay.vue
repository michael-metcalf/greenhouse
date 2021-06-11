<template>
  <div class="userMessage" v-if="this.$store.state.userMessage.message !== ''">
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
        info: 
          this.$store.state.userMessage.msgType === "info" &&
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
  width: 90%;
}

p {
  margin: 0px; /* No need margin as we have padding in the parent component */
  padding: 1em;
  border-radius: 10px;
}

p.error {
  color: black;
  background-color: lightcoral;
}

p.warning {
  background-color: lightyellow;
}

p.info {
  background-color: #d7efbd;
}
</style>
