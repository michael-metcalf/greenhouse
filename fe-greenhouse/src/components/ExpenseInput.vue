<template>
  <div id="expense-input-container">
    <div id="expense-input-form">
      <div class="verticalContainer">
        <h1>Add Expenses</h1>
        <p>Let's input an expense!</p>
        <div class="inputDiv">
          <input
            class="expense-input-button"
            type="date"
            name="date-input"
            v-model="posts.date"
          />
        </div>
        <div class="inputDiv">
          <input
            class="expense-input-button"
            type="text"
            name="amount-input"
            placeholder="Amount"
            v-model="posts.amount"
          />
        </div>
        <div class="inputDiv">
          <input
            class="expense-input-button"
            type="text"
            name="description-input"
            placeholder="Description"
            v-model="posts.description"
          />
        </div>
        <div id="category-button-container">
          <input
            @change="getCategory('Groceries')"
            type="radio"
            id="groceries"
            name="category"
            value="groceries"
          />
          <label class="category" for="groceries">Groceries</label>

          <input
            @change="getCategory('Bills')"
            type="radio"
            id="bills"
            name="category"
            value="bills"
          />
          <label class="category" for="bills">Bills</label>

          <input
            @change="getCategory('Transport')"
            type="radio"
            id="transport"
            name="category"
            value="transport"
          />
          <label class="category" for="transport">Transport</label>

          <input
            @change="getCategory('Misc')"
            type="radio"
            id="misc"
            name="category"
            value="misc"
          />
          <label class="category" for="misc">Misc</label>
        </div>
      </div>
      <div id="eco-action-container">
        <p>Did you take an eco action?</p>
        <div class="icon-box">
          <input
            id="eco-bag-no-bag"
            class="eco-action-checkbox"
            type="checkbox"
            name="eco-bag-no-bag"
            value="eco-bag-no-bag"
          />
          <label for="eco-bag-no-bag">
            <span class="eco-watch"></span>
            <i class="fas fa-shopping-bag" title="Eco bag/ No bag used"></i>
          </label>
        </div>
        <div class="icon-box">
          <input
            id="no-impulse-buy"
            class="eco-action-checkbox"
            type="checkbox"
            name="no-impulse-buy"
            value="no-impulse-buy"
          />
          <label for="no-impulse-buy">
            <span class="eco-watch"></span>
            <i class="fas fa-tags" title="No impulse purchase made"></i>
          </label>
        </div>
        <div class="icon-box">
          <input
            title="Eco conscious transport"
            id="eco-conscious-transport"
            class="eco-action-checkbox"
            type="checkbox"
            name="eco-conscious-transport"
            value="eco-conscious-transport"
          />
          <label for="eco-conscious-transport"
            ><span class="eco-watch"></span
            ><i class="fas fa-biking" title="Eco conscious transport"></i
          ></label>
        </div>
        <div class="icon-box">
          <p>I didn't take an eco action...</p>
          <input
            id="failed-eco-warrior"
            class="eco-action-checkbox"
            type="checkbox"
            name="failed-eco-warrior"
            value="failed-eco-warrior"
          />
          <label for="failed-eco-warrior"
            ><span class="eco-watch"></span
            ><i class="far fa-frown" title="No action taken"></i
          ></label>
        </div>
      </div>
      <button form="expense-input-form" type="submit" @click="postExpenseData">
        Submit
      </button>
    </div>
  </div>
</template>

<script>
// helper function for date padding
function display2Digits(number) {
  if (number < 10) {
    return "0" + number;
  } else {
    return number;
  }
}

export default {
  name: "ExpenseInput",
  // components: {FontAwesomeIcon},
  props: {},
  mounted() {
    // const externalScript = document.createElement("script");
    // externalScript.setAttribute(
    //   "src",
    //   "https://kit.fontawesome.com/e3cbc00358.js"
    // );
    // externalScript.setAttribute("crossorigin", "anonymous");
    // document.head.appendChild(externalScript);

    // setup the default date
    const currentDate = new Date();
    this.$data.posts.date = `${currentDate.getFullYear()}-${display2Digits(
      currentDate.getMonth() + 1
    )}-${display2Digits(currentDate.getDay())}`;
    console.log(this.$data.posts.date);
  },
  data() {
    return {
      posts: {
        date: null,
        amount: null,
        description: null,
        category: null,
      },
    };
  },
  methods: {
    postExpenseData(e) {
      const categoryFilter = this.$store.state.categoriesList.filter(
        (category) => category.category_id === this.posts.category
      );
      const expenseData = {
        user_id: this.$store.state.user.user_id,
        category_id: categoryFilter,
        expense_description: this.posts.description,
        amount: this.posts.amount,
      };

      this.$store.dispatch("createExpense", expenseData);

      console.warn(this.posts);
      e.preventDefault();
    },
    getCategory(category) {
      this.posts.category = category;
    },
  },
};
</script>

<style scoped>
#expense-input-container {
  --second-color: #368f8b;
  --button-color: #403d58;
}

p {
  font-weight: bold;
  color: var(--second-color);
}

.verticalContainer {
  display: flex;
  flex-direction: column;
}

.inputDiv {
  margin-bottom: 10px;
}

.inputDiv input {
  font-size: large;
}

input[type="radio"] {
  display: none;
  margin-top: 10px;
}
input[type="radio"]:not(:disabled) ~ label {
  cursor: pointer;
}
input[type="radio"]:disabled ~ label {
  color: #bcc2bf;
  border-color: #bcc2bf;
  box-shadow: none;
  cursor: not-allowed;
}

.category {
  height: 100%;
  display: inline-grid;
  width: 50px;
  background: white;
  border: 2px solid var(--second-color);
  border-radius: 20px;
  padding: 1rem;
  margin: 1px;
  text-align: center;
  justify-content: center;
  box-shadow: 0px 3px 10px -2px rgba(161, 170, 166, 0.5);
  position: relative;
  z-index: 0;
}

input[type="radio"]:checked + label {
  background: var(--button-color);
  border: 1px solid var(--second-color);
  color: white;
  border: 0px;
}
input[type="radio"]:checked + label::after {
  color: #3d3f43;
  font-family: FontAwesome;
  border: 1px solid var(--second-color);
  /* content: ""; */
  font-size: 22px;
  position: relative;
  top: -25px;
  left: 50%;
  transform: translateX(-50%);
  height: 20px;
  width: 0px;
  line-height: 20px;
  text-align: center;
  border-radius: 20%;
  background: white;
  box-shadow: 0px 2px 5px -2px rgba(0, 0, 0, 0.25);
}

input[type="checkbox"] + label {
  position: relative;
  padding-left: 24px;
}

input[type="checkbox"] + label .eco-watch {
  position: absolute;
  padding-left: 24px;
}

.fas,
.far {
  height: 50px;
  width: 50px;
  margin: 2px;
  font-size: 40px;
  display: inline-flex;
}

button {
  margin-top: 20px;
  margin-bottom: 100px;
  height: 2em;
  font-size: large;
  border-radius: 5px;
  border: 0px;
  background-color: #403d58;
  color: white;
  width: 100px;
}

@media only screen and (max-width: 700px) {
  section {
    flex-direction: column;
  }
}
</style>
