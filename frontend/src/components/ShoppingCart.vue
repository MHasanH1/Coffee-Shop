<template>
    <div class="container mt-5">
      <h1 class="mb-4">Your Shopping Cart</h1>
      <div v-if="loading" class="text-center">
        <div class="spinner-border" role="status">
          <span class="sr-only">Loading...</span>
        </div>
      </div>
      <div v-else>
        <form action="" @submit="submitForm()">
        <div v-if="cart && cart.products.length>=1" class="list-group">
          <div v-for="item in cart.products" :key="item.id" class="list-group-item d-flex justify-content-between align-items-center">
            <div>
              <h5 class="mb-1">{{ item.name }}</h5>
              <p class="mb-1">{{ item.vertical }} x ${{ item.price }}</p>
            </div>
            <button @click="removeFromCart(item.id)" class="btn btn-danger btn-sm">Remove</button>
          </div>
          <label for="check">takeway</label>
          <input type="checkbox" name='check' v-model="takeway" id="" >
          <div class="d-flex justify-content-center">
            <button type="submit" class="btn btn-outline-success">Submit</button>
          </div>
        </div>

        <div v-else class="alert alert-warning">Your cart is empty.</div>
      </form>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        cart: {
          id : null,
          purchase_amount : 0,
          type : null,
          products :[{
                id: null,
                name : "",
                coffee : 0,
                price : 0,
                sugar:0,
                vertical : '',
                flour : 0,
            }]
        },
        loading: true,
        takeway: false,
      };
    },
    created() {
      this.fetchCartItems();
    },
    methods: {
      async fetchCartItems() {
        axios.get('http://localhost:8000/api/cart/',{
            headers:{
                Authorization : `Token ${localStorage.getItem('token')}`
            }
        })
        .then(res=>{
            // console.log(res.data);
            this.cart=res.data;
            console.log(res.data);
        })
        .catch(err=>{
            console.log(err);
        })
        .finally(()=>{
            this.loading = false;
        })
      },
      async removeFromCart(itemId) {
        try {
          await axios.delete(`/api/cart/${itemId}/`);
          this.cartItems = this.cartItems.filter(item => item.id !== itemId);
        } catch (error) {
          console.error('Error removing item from cart:', error);
        }
      },
      submitForm(){
      console.log(";skfnlsnflsfn");
      axios.get('http://localhost:8000/api/confirm-cart/',{
        headers :{
          Authorization : `Token ${localStorage.getItem('token')}`
        }
      })
      .then(res=>{
        console.log(res.data);
      })
      .catch(err=>{
        console.log(err);
      })
    }
    },

  };
  </script>
  
  <style scoped>
  .container {
    max-width: 800px;
  }
  </style>
  