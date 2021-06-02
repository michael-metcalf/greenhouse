<template>
  <div id="expense-input-container">
    <form id="expense-input-form" action="">
      <div>
      <label for="expense-input">
        <input class="expense-input-button" type="date" name="date-input">
        <br>
        <input class="expense-input-button" type="text" name="amount-input" placeholder="Amount">
        <br>
        <input class="expense-input-button" type="text" name="description-input" placeholder="Description">
      </label>
      </div>
      <div id="category-button-container">
        <input type="radio" id="none" name="category" value="none" checked>
        <label for="misc">None</label>

        <input type="radio" id="groceries" name="category" value="groceries">
        <label for="groceries">Groceries</label>

        <input type="radio" id="bills" name="category" value="bills">
        <label for="bills">Bills</label>

        <input type="radio" id="transport" name="category" value="transport">
        <label for="transport">Transport</label>

        <input type="radio" id="misc" name="category" value="misc">
        <label for="misc">Misc</label>
      </div>
      <div id="eco-action-container">
        <input id="eco-bag-no-bag" class="eco-action-checkbox" type="checkbox" name="eco-bag-no-bag" value="eco-bag-no-bag">
        <label for="eco-bag-no-bag">Eco bag/no bag</label>
        <br>
        <input id="no-impulse-buy" class="eco-action-checkbox" type="checkbox" name="no-impulse-buy" value="no-impulse-buy">
        <label for="no-impulse-buy">No impulse buy</label>
        <br>
        <input id="eco-conscious-transport" class="eco-action-checkbox" type="checkbox" name="eco-conscious-transport" value="eco-conscious-transport">
        <label for="eco-conscious-transport">Eco-conscious transport</label>
      </div>
      <button form="expense-input-form" type="submit" name="submit" value="submit">Submit</button>
    </form>
  </div>  
</template>

<script>
export default {
  name: "ExpenseInput",
  props: {
  },
  methods: {    
  },
}
</script>

<style scoped>

</style>