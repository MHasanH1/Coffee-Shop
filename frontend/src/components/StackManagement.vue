<template>
  <div class="container mt-5">
    <h1 class="text-center mb-5">Storage Admin Panel</h1>
    <div class="row">
      <div class="col-md-3" v-for="item in items" :key="item.name">
        <div class="card mb-4 shadow-sm">
          <div class="card-body">
            <h5 class="card-title text-center">{{ item.name }}</h5>
            <form @submit.prevent="submitForm(item)">
              <div class="form-group">
                <label :for="`quantity-${item.name}`">Quantity</label>
                <input type="number" class="form-control" :id="`quantity-${item.name}`" v-model="item.amount" required>
              </div>
              <button type="submit" class="btn btn-primary btn-block">Submit</button>
            </form>
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
      items: [
        {
          name: '',
          amount : 0,
        }
      ],
      formValues: {
        sugar: '',
        coffee: '',
        flour: '',
        chocolate: ''
      }
    };
  },
  methods: {
    async submitForm(item) {

        const payload = {
          name: item.name,
          amount: item.amount
        };
        // console.log(payload);
        axios.post('http://localhost:8000/api/supply/',payload,{
          headers:{
            'Authorization': `Token ${localStorage.getItem('token')}`
          }
        })
        .then(res=>{
          console.log(res.data);
          alert(`${item.name.charAt(0).toUpperCase() + item.name.slice(1)} form submitted successfully!`);
        })
        .catch(err=>{
          console.log(err);
        })

    },
    getSupplies() {
      axios.get('http://localhost:8000/api/supply/')
      .then(res=>{
        console.log(res.data);
        this.items=res.data;
      })
      .catch(err=>{
        console.log(err);
      })
    }
  },
  created(){
    this.getSupplies();
  }
};
</script>

<style scoped>
.card {
  border-radius: 10px;
  transition: transform 0.2s;
}
.card:hover {
  transform: scale(1.05);
}
.card-title {
  font-weight: bold;
  color: #333;
}
button {
  margin-top: 10px;
}
</style>
