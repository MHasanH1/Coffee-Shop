<template>
    <div class="container mt-5">
      <div class="profile-header d-flex align-items-center mb-4">
        <div class="profile-picture">
          <img :src="getAbsouluteURL(user.profile)" alt="Profile Picture" class="rounded-circle" width="150" height="150">
        </div>
        <!-- <div class="profile-info ml-4">
          <h1>{{ user.name }}</h1>
          <p class="text-muted">{{ user.email }}</p>
        </div> -->
      </div>
  
      <h2>Edit Profile</h2>
      <form @submit.prevent="updateProfile">
        <div class="form-group">
          <label for="name">Name</label>
          <input type="text" class="form-control" id="name" v-model="user.username">
        </div>
        <div class="form-group">
          <label for="email">Email</label>
          <input type="email" class="form-control" id="email" v-model="user.email">
        </div>
        <div class="form-group">
          <label for="profilePicture">Phone number</label>
          <input type="text" class="form-control" id="profilePicture" v-model="user.phonenumber">
        </div>
        <div class="form-group">
          <label for="profilePicture">first name</label>
          <input type="text" class="form-control" id="profilePicture" v-model="user.first_name">
        </div>
        <div class="form-group">
          <label for="profilePicture">last name</label>
          <input type="text" class="form-control" id="profilePicture" v-model="user.last_name">
        </div>
        <button type="submit" class="btn btn-primary">Update Profile</button>
      </form>
    </div>
  </template>
  
  <script>
import axios from 'axios';
  
export default {
    data() {
      return {
        user: {
          name: '',
          email: '',
          phonenumber: '',
          first_name: '',
          last_name:'',
          profile:'',
        },
        loading: true,
      };
    },
    created() {
      this.fetchUserProfile();
    },
    methods: {
      fetchUserProfile() {
      axios.get('http://localhost:8000/api/profile',{
        headers:{
            Authorization : `Token ${localStorage.getItem('token')}`
        }
      }).then(response => {
        console.log(response.data);
        this.user = response.data;
      })
      .catch(err=>{
        console.log(err);
      })
      },
      async updateProfile() {
        try {
          await axios.put('/api/user/profile/', this.user);
          alert('Profile updated successfully!');
        } catch (error) {
          console.error('Error updating profile:', error);
        }
      },

      getAbsouluteURL(url){
        return "http://localhost:8000" + url
      }
    },
};
  </script>
  
  <style scoped>
  .container {
    max-width: 800px;
  }
  
  .profile-header {
    display: flex;
    align-items: center;
  }
  
  .profile-picture img {
    border: 2px solid #ddd;
    padding: 5px;
  }
  
  .profile-info h1 {
    margin: 0;
    font-size: 2rem;
  }
  
  .profile-info p {
    margin: 0;
    font-size: 1.2rem;
  }
  </style>
  