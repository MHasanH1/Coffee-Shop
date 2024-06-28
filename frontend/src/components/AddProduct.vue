<template>
  <div>
    <div class="d-flex justify-content-center align-items-center my-5">
      <img src="../assets/img/addProduct.png" style="width: 30%"/>

      <form class="form-signin mx-auto" style="width: 40%" @submit="submit">
        <div class="user-box">
          <input type="text" autocomplete required v-model="name"/>
          <label>Product Name</label>
        </div>

        <label for="vertical">Choose Vertical:</label>
        <div class="user-box">
          <select v-model="vertical" style="width: 100%; border: none; background-color: #f1f1f1; border-radius: 5px; padding: 10px">
            <option value="hot drink">Warm Drink</option>
            <option value="dold drink">Cold Drink</option>
            <option value="cake">Cake</option>
          </select>
        </div>

        <div class="mt-4">
          <label class="mb-2">Material Amount:</label>
          <div class="d-flex align-items-center gap-2 mb-3">
            <label>Sugar</label>
            <input v-model="sugarAmount" class="w-100" type="range" min="0" max="100" value="0" />
            <span>{{sugarAmount}}</span>
          </div>
          <div class="d-flex align-items-center gap-2 mb-3">
            <label>Coffee</label>
            <input v-model="coffeeAmount" class="w-100" type="range" min="0" max="100" value="0" />
            <span>{{coffeeAmount}}</span>
          </div>
          <div class="d-flex align-items-center gap-2 mb-3">
            <label>Flour</label>
            <input v-model="flourAmount" class="w-100" type="range" min="0" max="100" value="0" />
            <span>{{flourAmount}}</span>
          </div>
          <div class="d-flex align-items-center gap-2 mb-3">
            <label>Chocolate</label>
            <input v-model="chocolateAmount" class="w-100" type="range" min="0" max="100" value="0" />
            <span>{{chocolateAmount}}</span>
          </div>
        </div>

        <div class="user-box">
          <input v-model.number.lazy="price" type="text" autocomplete required />
          <label>Price</label>
        </div>

        <div class="">
          <label class="d-block mb-1">Image</label>
          <input type="file" id="fileInput" style="display: none">
          <button class="btn btn-primary" onclick="document.getElementById('fileInput').click()">Choose File</button>
        </div>

        <hr class="my-3" />
        <div class="d-flex justify-content-center">
          <button type="submit" class="btn btn-outline-success">Submit</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      sugarAmount: 0,
      coffeeAmount: 0,
      flourAmount: 0,
      chocolateAmount: 0,
      price: null,
      name : "",
      vertical : '',
    }
  },
  methods:{
    submit(){
      console.log(this.vertical);
      let body={
        sugar : this.sugarAmount,
        name : this.name,
        coffee : this.coffeeAmount,
        flour : this.flourAmount,
        chocolate : this.chocolateAmount,
        price : this.price,
        vertical : this.vertical
      }
      axios.post('http://localhost:8000/api/addproduct/',body,{
        headers : {
          Authorization : `Token ${localStorage.getItem('token')}`
        }
      })
      .then(res=>{
          console.log(res);
          alert('created!')
        })
        .catch(err=>{
          console.log(err);
        })
    }
  }
}
</script>

<style scoped>

@import url("https://fonts.googleapis.com/css?family=Poppins:400,500&display=swap");

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.alert {
  position: fixed;
  bottom: 4rem;
}

.signUp {
  transition: .1s;
  color: blue;
  border: none;
  box-shadow: none;
}

.signUp:hover {
  color: #0000c9;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}

body {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f1f1f1;
}

.container {
  width: 100%;
  max-width: 400px;
  padding: 20px;
}

.login-box {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.login-box h2 {
  margin: 0 0 15px;
  padding: 0;
  color: #333;
  text-align: center;
  text-transform: uppercase;
}

.user-box {
  position: relative;
}

.user-box input {
  width: 100%;
  padding: 10px 0;
  font-size: 16px;
  color: #333;
  margin-bottom: 30px;
  border: none;
  border-bottom: 2px solid #333;
  outline: none;
  background: transparent;
}

.user-box label {
  position: absolute;
  top: 0;
  left: 0;
  padding: 10px 0;
  font-size: 16px;
  color: #333;
  pointer-events: none;
  transition: 0.5s;
}

.user-box input:focus ~ label,
.user-box input:valid ~ label {
  transform: translateY(-20px);
  font-size: 14px;
  color: #333;
}

/*a {
  display: inline-block;
  background-color: #333;
  color: #fff;
  padding: 10px 20px;
  font-size: 16px;
  text-transform: uppercase;
  text-decoration: none;
  position: relative;
  overflow: hidden;
  transition: 0.5s;
  letter-spacing: 2px;
  border-radius: 5px;
}

a:hover {
  background-color: #fff;
  color: #333;
  border: 1px solid #333;
}*/

/*a span {
  position: absolute;
  display: block;
}

a span:nth-child(1) {
  top: 0;
  left: -100%;
  width: 100%;
  height: 2px;
  background-color: #333;
  animation: animate1 1s linear infinite;
}*/

@keyframes animate1 {
  0% {
    left: -100%;
  }
  50%,
  100% {
    left: 100%;
  }
}

a span:nth-child(2) {
  top: -100%;
  right: 0;
  width: 2px;
  height: 100%;
  background-color: #333;
  animation: animate2 1s linear infinite;
  animation-delay: 0.25s;
}

@keyframes animate2 {
  0% {
    top: -100%;
  }
  50%,
  100% {
    top: 100%;
  }
}

a span:nth-child(3) {
  bottom: 0;
  right: -100%;
  width: 100%;
  height: 2px;
  background-color: #333;
  animation: animate3 1s linear infinite;
  animation-delay: 0.5s;
}

@keyframes animate3 {
  0% {
    right: -100%;
  }
  50%,
  100% {
    right: 100%;
  }
}

a span:nth-child(4) {
  bottom: -100%;
  left: 0;
  width: 2px;
  height: 100%;
  background-color: #333;
  animation: animate4 1s linear infinite;
  animation-delay: 0.75s;
}

@keyframes animate4 {
  0% {
    bottom: -100%;
  }
  50%,
  100% {
    bottom: 100%;
  }
}

.password-toggle-icon {
  position: absolute;
  top: 50%;
  right: 10px;
  transform: translateY(-50%);
  cursor: pointer;
}

.password-toggle-icon i {
  font-size: 18px;
  line-height: 1;
  color: #333;
  transition: color 0.3s ease-in-out;
  margin-bottom: 20px;
}

.password-toggle-icon i:hover {
  color: #000;
}

</style>