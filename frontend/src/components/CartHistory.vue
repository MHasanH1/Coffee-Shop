<template>
    <div class="container mt-5">
      <h1 class="mb-4">Cart History</h1>
      <table class="table table-striped table-hover">
        <thead>
          <tr>
            <th scope="col">Cart ID</th>
            <th scope="col">Date</th>
            <th scope="col">Total Amount</th>
            <th scope="col">Items</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="cart in carts" :key="cart.id">
            <td>{{ cart.id }}</td>
            <td>{{ cart.datetime }}</td>
            <td>{{ cart.order.purchase_amount }}</td>
            <td>
              <button type="button" class="btn btn-info btn-sm" data-toggle="modal" data-target="#itemsModal" @click="selectCart(cart)">View Items</button>
            </td>
          </tr>
        </tbody>
      </table>
  
      <!-- Modal -->
      <div class="modal fade" id="itemsModal" tabindex="-1" role="dialog" aria-labelledby="itemsModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="itemsModalLabel">Cart Items</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <ul>
                <li v-for="item in selectedCartItems" :key="item.id">{{ item.name }} - {{ item.quantity }}</li>
              </ul>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
import axios from 'axios';

  export default {
    data() {
      return {
        carts: [
          {
            id: 0,
            datetime : null,
            order : {
              id : 0,
              purchase_amount : 0,
              products:[
              {
                id : 0,
                coffee : 0,
                flour : 0,
                sugar : 0,
                price : 0,
                vertical : '',
                name : ''
              },
            ],
            type : false,
            },


          }
        ],
        selectedCartItems: []
      };
    },
    methods: {
      selectCart(cart) {
        this.selectedCartItems = cart.items;
      },
      getCarts(){
        axios.get('http://localhost:8000/api/history/',{
          headers:{
            Authorization :`Token ${localStorage.getItem('token')}`
          }
        })
        .then(res=>{
          console.log(res.data);
          this.carts=res.data;
        })
        .catch(err=>{
          console.log(err);
        }
        
        )
      }
    },
    created(){
      this.getCarts();
    }
  };
  </script>
  
  <style scoped>
  .container {
    max-width: 800px;
  }
  </style>
  