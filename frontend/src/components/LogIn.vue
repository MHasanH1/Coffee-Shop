<template>
  <div class="d-flex justify-content-center align-items-center">
    <main class="form-signin w-25 mx-auto">
      <form @submit.prevent="logIn">
        <img class="mb-4" src="../assets/img/Login.jpg" alt="" width="182" height="177">
        <h1 class="h3 mb-3 fw-normal">Login</h1>

        <div class="user-box">
          <input type="text" autocomplete required v-model="body.username"/>
          <label>username</label>
          <span class="password-toggle-icon"><i class="fa fa-eye"></i></span>
        </div>

        <div class="user-box">
          <input type="password" autocomplete required v-model="body.password"/>
          <label>Password</label>
          <span class="password-toggle-icon"><i class="fa fa-eye"></i></span>
        </div>

        <div class="form-check text-start my-3">
          <input class="form-check-input" type="checkbox" value="remember-me" id="flexCheckDefault">
          <label class="form-check-label" for="flexCheckDefault">
            Remember me
          </label>
        </div>
        <button class="btn btn-primary w-100 py-2" type="submit">Login</button>
        <div class="d-flex justify-content-center align-items-center">
          <p class="mt-4 mb-0">Don't have any account?</p>
          <button class="btn mt-4 signUp" @click="this.$router.push('/signup')">sign up</button>
        </div>
      </form>
    </main>
    <transition name="fade">
      <div v-show="loginErr !== 'You logged in successful' && loginErr !== ''" ref="alert" class="alert alert-danger alert-dismissible fade show" role="alert">
        <strong>Error!</strong> {{ loginErr }}
        <button type="button" class="btn-close" @click="this.$refs.alert.style.opacity = 0" aria-label="Close"></button>
      </div>
    </transition>

    <transition name="fade">
      <div v-show="loginErr === 'You logged in successful'" ref="alertS" class="alert alert-success alert-dismissible fade show" role="alert">
        <strong>Success!</strong> {{ loginErr }}
        <button type="button" class="btn-close" @click="this.$refs.alertS.style.opacity = 0" aria-label="Close"></button>
      </div>
    </transition>

<!--    <div v-show="!loginErr" class="alert alert-success alert-dismissible fade show" role="alert">-->
<!--      <strong>Success!</strong> You logged in successful.-->
<!--    </div>-->
  </div>
</template>

<script>

import axios from "axios";

export default {
  data() {
    return {
      body:{
        username:'',
        password:'',
      },
      loginErr: "",
    }
  },
  methods: {
    logIn(){
      axios.post(`http://localhost:8000/api/login/`,this.body)
      .then(res=>{
        localStorage.setItem('token',res.data.token);
        // localStorage.setItem('info', JSON.stringify(res));
        this.loginErr = "You logged in successful";
        this.$refs.alertS.style.opacity = 1;
        setTimeout(() => {
          this.$refs.alertS.style.opacity = 0;
        }, 1800);
        setTimeout(()=> {
          this.$router.push('/');
        }, 2000);
      })
      .catch(err=>{
        this.loginErr = err.response.data.error;
        this.$refs.alert.style.opacity = 1;
        setTimeout(() => {
          this.$refs.alert.style.opacity = 0;
        }, 3000);
      })
    }
  },
  mounted() {

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