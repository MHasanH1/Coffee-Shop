<template>
  <div class="album py-5 bg-body-tertiary">
    <div class="container">
      <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
        <div v-for="(card, index) in visibleCards" :key="index" class="col">
          <div class="card shadow-sm">
            <svg class="bd-placeholder-img card-img-top" width="100%" height="225" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Thumbnail" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#55595c"></rect><text x="50%" y="50%" fill="#eceeef" dy=".3em">Thumbnail</text></svg>
            <div class="card-body">
              <h4>{{card?.name}}</h4>
              <p class="card-text">coffee {{card?.coffee}}</p>
              <p class="card-text">flour {{card?.flour}}</p>
              <p class="card-text">price {{card?.price}}</p>
              <p class="card-text">sugar {{card?.sugar}}</p>
              <p class="card-text">vertical {{card?.vertical}}</p>

              <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                  <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                  <button type="button" class="btn btn-sm btn-outline-secondary" v-if="isAdmin">Edit</button>
                  <button type="button" class="btn btn-sm btn-outline-secondary" @click="addToCart(card.id)">add to cart</button>
                </div>
                <small class="text-body-secondary">9 mins</small>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="d-flex my-4">
        <button class="btn btn-outline-primary" v-if="!showAll" @click="showAllCards">See More</button>
        <button class="btn btn-success" v-if="showAll" @click="showLessCards">See Less</button>
      </div>
    </div>
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

        }
      ],
      showAll: false,
      isAdmin: false,
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
    addToCart(id){
      axios.post(`http://localhost:8000/api/add-to-cart/${id}/`,{}, {
        headers:{
          'Authorization': `Token ${localStorage.getItem('token')}`
        }
      })
      .then(res=>{
        // console.log("in then");
        console.log(res);
        alert('add successfully')
      })
      .catch(err=>{
        if (err.response.status===302){
          alert('already exists in cart')
        }
        console.log(err);
      })
    },
    getPopulars(){
      axios.get('http://localhost:8000/api/get-populars/',{
        headers:{
          Authorization : `Token ${localStorage.getItem('token')}`
        }
      })
      .then(res=>{
        console.log(res);
        this.cards=res.data;
      }).catch(err=>{

        console.log(err);
      })
    }
  },
  mounted(){
    this.getPopulars();
  }
}
</script>

<style scoped>

</style>