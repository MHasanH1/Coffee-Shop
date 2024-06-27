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
            <td>{{ cart.date }}</td>
            <td>{{ cart.total }}</td>
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
  export default {
    data() {
      return {
        carts: [
          { id: 1, date: '2023-06-25', total: '$100', items: [{ id: 1, name: 'Item A', quantity: 2 }, { id: 2, name: 'Item B', quantity: 1 }] },
          { id: 2, date: '2023-06-26', total: '$150', items: [{ id: 3, name: 'Item C', quantity: 3 }, { id: 4, name: 'Item D', quantity: 2 }] }
        ],
        selectedCartItems: []
      };
    },
    methods: {
      selectCart(cart) {
        this.selectedCartItems = cart.items;
      }
    }
  };
  </script>
  
  <style scoped>
  .container {
    max-width: 800px;
  }
  </style>
  