<template>
    <div class="p-5">
      <div v-if="loading" class="loading">
        <div class="spinner"></div>
        Loading...
      </div>
      <div v-else>
        <h1 class="text-center mb-5">Vertical: {{vertical}}</h1>
        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
          <div v-for="(card, index) in cards" :key="index" class="col">
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
                    <button type="button" class="btn btn-sm btn-outline-success" @click="addToCart(card.id)">Add to cart</button>
                  </div>
                  <!--                <small class="text-body-secondary">9 mins</small>-->
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>

import axios from "axios";

export default {
  data() {
    return {
      cards: [
        {
          name:'',
          sugar:0,
          coffee: 0,
          flour: 0 ,
        }
      ],
      filteredCards: [
        {
          name:'',
          sugar:0,
          coffee: 0,
          flour: 0 ,
        }
      ],
      alertWarning: 'alert-warning',
      alertSuccess: 'alert-success',
      loading: true,
      vertical: "",
    };
  },
  mounted() {
    this.vertical = this.$route.params.vertical.slice(1);
    this.getPopulars();
  },
  updated() {
    this.vertical = this.$route.params.vertical.slice(1);
  },
  methods: {
    addToCart(id) {
      axios.post(`http://localhost:8000/api/add-to-cart/${id}/`,{}, {
        headers: {
          'Authorization': `Token ${localStorage.getItem('token')}`
        }
      })
          .then(res => {
            console.log(res);
            this.addStatus = "add successfully";
            this.$refs.alertS.style.opacity = 1;
            setTimeout(() => {
              this.$refs.alertS.style.opacity = 0;
            }, 2500);
          })
          .catch(err => {
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
      console.log(this.vertical.toLowerCase())
      axios.post('http://localhost:8000/api/vertical/',{
        ver: this.vertical.toLowerCase()
      })
          .then(res => {
            this.cards = res.data;
          }).catch(err => {
        console.log(err);
      })
      this.loading = false;
    },
  },
  watch: {
    vertical(nval, oval) {
      if (oval !== '') {
        this.getPopulars();
      }
    }
  }
};
</script>

<style scoped>
.loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  font-size: 1.5em;
}

.spinner {
  border: 6px solid #f3f3f3;
  border-top: 6px solid #3498db;
  border-radius: 50%;
  width: 70px;
  height: 70px;
  animation: spin .8s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.status {
  width: 15px;
  height: 15px;
}

</style>
