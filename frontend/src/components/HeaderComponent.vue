<template>
  <div>
    <header class="p-3 text-bg-dark">
      <div class="container">
        <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
          <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0 gap-5">
            <li class="d-flex align-items-center">
              <div class="dropdown">
                <button class="button d-flex align-items-center gap-1" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Menu
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="svgSize size-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
                  </svg>
                </button>
                <ul class="dropdown-menu pe-2">
                  <li>
                    <div class="d-flex dropend w-100 justify-content-between">
                      <button @click="this.$router.push('/products:Hot Drink')" type="button" class="btn w-100">
                        Hot Drink
                      </button>
<!--                      <div class="self-dropdown">-->
<!--                        <button type="button" class="self-dropbtn btn dropdown-toggle dropdown-toggle-split border-0">-->
<!--                          <span class="visually-hidden">Toggle Dropend</span>-->
<!--                        </button>-->
<!--                        <div class="self-dropdown-content">-->
<!--                          <a href="#">Link 1</a>-->
<!--                          <a href="#">Link 2</a>-->
<!--                          <a href="#">Link 3</a>-->
<!--                        </div>-->
<!--                      </div>-->
                    </div>
                  </li>
                  <li>
                    <div class="d-flex dropend w-100 justify-content-between">
                      <button @click="this.$router.push('/products:Cold Drink')" type="button" class="btn w-100">
                        Cold Drink
                      </button>
<!--                      <div class="self-dropdown">-->
<!--                        <button type="button" class="self-dropbtn btn dropdown-toggle dropdown-toggle-split border-0">-->
<!--                          <span class="visually-hidden">Toggle Dropend</span>-->
<!--                        </button>-->
<!--                        <div class="self-dropdown-content">-->
<!--                          <a href="#">Link 1</a>-->
<!--                          <a href="#">Link 2</a>-->
<!--                          <a href="#">Link 3</a>-->
<!--                        </div>-->
<!--                      </div>-->
                    </div>
                  </li>
                  <li>
                    <div class="d-flex dropend w-100 justify-content-between">
                      <button @click="this.$router.push('/products:Cakes')" type="button" class="btn w-100">
                        Cakes
                      </button>
<!--                      <div class="self-dropdown">-->
<!--                        <button type="button" class="self-dropbtn btn dropdown-toggle dropdown-toggle-split border-0">-->
<!--                          <span class="visually-hidden">Toggle Dropend</span>-->
<!--                        </button>-->
<!--                        <div class="self-dropdown-content">-->
<!--                          <a href="#">Link 1</a>-->
<!--                          <a href="#">Link 2</a>-->
<!--                          <a href="#">Link 3</a>-->
<!--                        </div>-->
<!--                      </div>-->
                    </div>
                  </li>
                  <li>
                    <div class="d-flex dropend w-100 justify-content-between">
                      <button @click="this.$router.push('/products:Milk')" type="button" class="btn w-100">
                        Milk
                      </button>
<!--                      <div class="self-dropdown">-->
<!--                        <button type="button" class="self-dropbtn btn dropdown-toggle dropdown-toggle-split border-0">-->
<!--                          <span class="visually-hidden">Toggle Dropend</span>-->
<!--                        </button>-->
<!--                        <div class="self-dropdown-content">-->
<!--                          <a href="#">Link 1</a>-->
<!--                          <a href="#">Link 2</a>-->
<!--                          <a href="#">Link 3</a>-->
<!--                        </div>-->
<!--                      </div>-->
                    </div>
                  </li>
                </ul>
              </div>
            </li>
            <li>
              <router-link to="/history" class="nav-link px-2 text-white d-flex align-items-center gap-1">
                cart History
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="svgSize size-6">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z" />
                </svg>
              </router-link>
            </li>
            <li>
              <router-link to="/cart" class="nav-link px-2 text-white d-flex align-items-center gap-1">
                my cart
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="svgSize size-6">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 10.5V6a3.75 3.75 0 1 0-7.5 0v4.5m11.356-1.993 1.263 12c.07.665-.45 1.243-1.119 1.243H4.25a1.125 1.125 0 0 1-1.12-1.243l1.264-12A1.125 1.125 0 0 1 5.513 7.5h12.974c.576 0 1.059.435 1.119 1.007ZM8.625 10.5a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm7.5 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z" />
                </svg>
              </router-link>
            </li>
            <li v-if="isAuthenticated">
              <router-link to="/profile" class="nav-link px-2 text-white d-flex align-items-center gap-1">
                profile
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="24px" height="24px">
                  <path d="M0 0h24v24H0z" fill="none"/>
                  <path d="M12 12c2.7 0 4.98-2.19 5-4.9V7c0-2.7-2.19-5-4.9-5h-.2C9.2 2 7 4.2 7 6.9V7c0 2.71 2.3 4.99 5 5zM12 14c-3.93 0-7 3.07-7 7h2c0-2.76 2.24-5 5-5s5 2.24 5 5h2c0-3.93-3.07-7-7-7z"/>
                </svg>
              </router-link>
            </li>
            <li v-if="isAdmin">
              <router-link to="/shopmanagement" class="nav-link px-2 text-white d-flex align-items-center gap-1">
                Admin panel


              </router-link>
            </li>
          </ul>

          <form class="col-12 col-lg-auto mb-3 mb-lg-0 me-lg-3" role="search">
            <input type="search" class="form-control form-control-dark" placeholder="Search..." aria-label="Search">
          </form>

          <div class="text-end">
<!--            <div v-show="username" class="d-flex align-items-center gap-3">-->
<!--              <h4 class="m-0">Hello {{username}}!</h4>-->
<!--              <button @click="this.$router.push('/login')" type="button" class="btn btn-outline-danger me-2">Logout</button>-->
<!--            </div>-->
<!--            <div v-show="!username">-->
<!--              <button @click="this.$router.push('/login')" type="button" class="btn btn-outline-light me-2">Login</button>-->
<!--              <button @click="this.$router.push('/signup')" type="button" class="btn btn-warning">Sign-up</button>-->
<!--            </div>-->

            <div class="d-flex align-items-center gap-3">
              <h4 v-if="isAuthenticated" class="m-0">Hello {{user.username}}!</h4>
              <button v-if="!isAuthenticated" @click="this.$router.push('/login')" type="button" class="btn btn-outline-light me-2">Login</button>
              <button v-if="!isAuthenticated" @click="this.$router.push('/signup')" type="button" class="btn btn-warning">Sign-up</button>
              <button v-else @click="this.$router.push('/login')" type="button" class="btn btn-outline-danger me-2 d-flex">Logout</button>
            </div>
          </div>
        </div>
      </div>
    </header>
  </div>
</template>


<script>
import axios from "axios";
import {checkAuthentication} from "../services";
import {checkAdministary} from "../services";
export default ({
  // props: ['username'],
  data(){
    return {
      isAuthenticated: false,
      isAdmin:false,
      user : {
        username :'',
      },
    }
  },
  mounted() {
    // const dropdown = document.getElementsByClassName("dropdown-menu")[0];
    // dropdown.addEventListener('click', (e) => {
    //   e.stopPropagation();
    // });
  },
  async beforeCreate(){
    this.isAuthenticated=await checkAuthentication();
    console.log(this.isAuthenticated);
    this.isAdmin=await checkAdministary();
    if (this.isAuthenticated){
      axios.get('http://localhost:8000/api/profile/',{
      headers:{
        Authorization : `Token ${localStorage.getItem('token')}`
      }
    })
    .then(res=>{
      this.user=res.data
    })
    .catch(err=>{
      console.log(err);
    })
    }

  }
  
})
</script>

<style>
.button {
  background: none;
  color: white;
  border: none;
}

.svgSize {
  width: 20px;
  height: 20px;
}

.self-dropdown {
  position: relative;
  display: inline-block;
}

.self-dropbtn {
  background-color: #3498db;
  color: white;
  padding: 16px;
  font-size: 16px;
  border: none;
  cursor: pointer;
}

.self-dropdown-content {
  display: none;
  position: absolute;
  left: 100%;
  top: 0;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  background-color: white;
  z-index: 1;
}

.self-dropdown-content a {
  color: black;
  padding: 10px;
  text-decoration: none;
  display: block;
}

.self-dropdown-content a:hover {
  background-color: #ddd;
}

.self-dropdown:hover .self-dropdown-content {
  display: block;
}

</style>