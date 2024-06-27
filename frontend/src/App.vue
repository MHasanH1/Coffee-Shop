<template>
  <div>
    <headerComponent :username="username" :vertical="vertical" />
    <router-view></router-view>
  </div>
</template>


<script>
import HeaderComponent from "@/components/HeaderComponent.vue";

export default {
  components: {HeaderComponent},
  data() {
    return {
      username: '',
      sharedData: null,
      vertical: '',
    };
  },
  mounted() {
    this.sharedData = JSON.parse(localStorage.getItem('sharedData'));
    this.username = JSON.parse(this.sharedData.config.data).username;
  }
}

</script>


<style scoped>

</style>