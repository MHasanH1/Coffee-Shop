<template>
  <div class="album py-5 bg-body-tertiary">
    <div class="container">
      <h2 class="text-center mb-4">Popular Products</h2>
      <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
        <div v-for="(card, index) in visibleCards" :key="index" class="col">
          <div class="card shadow-sm">
            <img class="bd-placeholder-img card-img-top" :src="card?.image" :alt="card?.name" :title="card?.name" width="100%" height="225" />
            <div class="card-body">
              <h4>{{card?.name}}</h4>
              <div class="d-flex align-items-center gap-1 mb-3 mt-1">
                <h6 class="card-text m-0">Vertical: {{card?.vertical}}</h6>
                <img v-if="card?.vertical === 'hot drink'" class="svgSize" src="../assets/hot.png" alt="vertical" />
                <img v-else-if="card?.vertical === 'cold drink'" class="svgSize" src="../assets/cold.png" alt="vertical" />
              </div>
              <div class="d-flex align-items-center gap-2 my-3">
                <svg
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                      d="M6 2.5C5.44772 2.5 5 2.94772 5 3.5V5.5C5 6.05228 5.44772 6.5 6 6.5C6.55228 6.5 7 6.05228 7 5.5V3.5C7 2.94772 6.55228 2.5 6 2.5Z"
                      fill="currentColor"
                  />
                  <path
                      fill-rule="evenodd"
                      clip-rule="evenodd"
                      d="M13 21.5C15.973 21.5 18.441 19.3377 18.917 16.5H19C21.2091 16.5 23 14.7091 23 12.5C23 10.2909 21.2091 8.5 19 8.5V7.5H1V15.5C1 18.8137 3.68629 21.5 7 21.5H13ZM3 9.5V15.5C3 17.7091 4.79086 19.5 7 19.5H13C15.2091 19.5 17 17.7091 17 15.5V9.5H3ZM21 12.5C21 13.6046 20.1046 14.5 19 14.5V10.5C20.1046 10.5 21 11.3954 21 12.5Z"
                      fill="currentColor"
                  />
                  <path
                      d="M9 3.5C9 2.94772 9.44771 2.5 10 2.5C10.5523 2.5 11 2.94772 11 3.5V5.5C11 6.05228 10.5523 6.5 10 6.5C9.44771 6.5 9 6.05228 9 5.5V3.5Z"
                      fill="currentColor"
                  />
                  <path
                      d="M14 2.5C13.4477 2.5 13 2.94772 13 3.5V5.5C13 6.05228 13.4477 6.5 14 6.5C14.5523 6.5 15 6.05228 15 5.5V3.5C15 2.94772 14.5523 2.5 14 2.5Z"
                      fill="currentColor"
                  />
                </svg>
                <p class="card-text m-0">Coffee: {{card?.coffee}}%</p>
                <div v-if="card?.coffee >= 75" class="bg-danger status"></div>
                <div v-else-if="card?.coffee >= 25" class="bg-warning status"></div>
                <div v-else class="bg-success status"></div>
              </div>
              <div class="d-flex align-items-center gap-2 my-3">
                <img src="../assets/flour.png" class="svgSize" alt="flour" />
                <p class="card-text m-0">Flour: {{card?.flour}}%</p>
                <div v-if="card?.flour >= 75" class="bg-danger status"></div>
                <div v-else-if="card?.flour >= 25" class="bg-warning status"></div>
                <div v-else class="bg-success status"></div>
              </div>
              <div class="d-flex align-items-center gap-2 my-3">
                <img src="../assets/sugar.png" class="svgSize" alt="sugar" />
                <p class="card-text m-0">Sugar: {{card?.sugar}}%</p>
                <div v-if="card?.sugar >= 75" class="bg-danger status"></div>
                <div v-else-if="card?.sugar >= 25" class="bg-warning status"></div>
                <div v-else class="bg-success status"></div>
              </div>

              <div class="d-flex align-items-center gap-2 my-2">
                <img src="../assets/price.png" class="svgSize" alt="price" />
                <p class="card-text fw-bold">Price: {{card?.price}}$</p>
              </div>

              <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
<!--                  <button type="button" class="btn btn-sm btn-outline-secondary">View</button>-->
                  <button type="button" class="btn btn-sm btn-outline-warning" v-if="isAdmin">Edit</button>
<!--                  <button type="button" class="btn btn-sm btn-outline-success" @click="addToCart(card.id)">{{addBtnText}}</button>-->
                  <button type="button" class="btn btn-sm btn-outline-success" v-if="!card.in_cart" @click="addToCart(card)">add to cart</button>
                  <button type="button" class="btn btn-sm btn-outline-success" v-else @click="removeFromCart(card)">remove from the cart</button>
                </div>
<!--                <small class="text-body-secondary">9 mins</small>-->
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="d-flex my-4" v-if="cards.length > 3">
        <button class="btn btn-outline-primary" v-if="!showAll" @click="showAllCards">See More</button>
        <button class="btn btn-success" v-if="showAll" @click="showLessCards">See Less</button>
      </div>
    </div>
    <transition name="fade">
        <div v-show="addStatus === 'already exists in cart'" ref="alertW" class="alert alert-warning alert-dismissible fade show" role="alert">
          <strong>Warning!</strong> {{ addStatus }}
          <button type="button" class="btn-close" @click="this.$refs.alertW.style.opacity = 0" aria-label="Close"></button>
        </div>
    </transition>

    <transition name="fade">
      <div v-show="addStatus === 'add successfully'" ref="alertS" class="alert alert-success alert-dismissible fade show" role="alert">
        <strong>Success!</strong> {{ addStatus }}
        <button type="button" class="btn-close" @click="this.$refs.alertS.style.opacity = 0" aria-label="Close"></button>
      </div>
    </transition>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      cards: [
        {
          name:'',
          sugar:0,
          coffee: 0,
          flour: 0 ,
          vertical : '',
          in_cart : false

        }
      ],
      alertWarning: 'alert-warning',
      alertSuccess: 'alert-success',
      showAll: false,
      isAdmin: false,
      addStatus: "",
      cartItems: [],
      addBtnText: "Add to cart",
    }
  },
  computed: {
    visibleCards() {
      return this.showAll ? this.cards : this.cards.slice(0, 3);
    },
  },
  methods: {
    showAllCards() {
      this.showAll = true;
    },
    showLessCards() {
      this.showAll = false;
    },
    addToCart(cart) {
      let id=cart.id;
      axios.post(`http://localhost:8000/api/add-to-cart/${id}/`,{}, {
        headers: {
          'Authorization': `Token ${localStorage.getItem('token')}`
        }
      })
      .then(res => {
        // console.log("in then");
        console.log(res);
        cart.in_cart=true; 
        this.addStatus = "add successfully";
        this.$refs.alertS.style.opacity = 1;
        setTimeout(() => {
          this.$refs.alertS.style.opacity = 0;
        }, 2500);
      })
      .catch(err => {
        if (err.response.status===406){
          this.addStatus=err.response.data["message"];

        }
        if (err.response.status===302) {
          this.addStatus = "already exists in cart";
        }
        this.$refs.alertW.style.opacity = 1;
        setTimeout(() => {
          this.$refs.alertW.style.opacity = 0;
        }, 2500);
      })
    },
    getPopulars() {
      axios.get('http://localhost:8000/api/get-populars/',{
        headers: {
          Authorization : `Token ${localStorage.getItem('token')}`
        }
      })
      .then(res => {
        console.log(res.data);
        this.cards = res.data;
      }).catch(err => {
        console.log(err);
      })
    },
    removeFromCart(cart){
      let id=cart.id;
      axios.post('http://localhost:8000/api/remove-from-cart/',{
        id:id
      },{
        headers:{
          Authorization : `Token ${localStorage.getItem('token')}`
        }
      })
      .then(res=>{
        console.log(res.data);
        cart.in_cart=false;
        // this.cards=res.data;
      })
      .catch(err=>{
        console.log(err);
      })
    }
  },
  mounted() {
    this.getPopulars();
  },
}
</script>

<style scoped>
.alert {
  width: 50%;
  margin: 0 auto;
  bottom: 5rem;
}

.svgSize {
  width: 25px;
  height: 25px;
}

.status {
  width: 15px;
  height: 15px;
}

</style>