<template>
  <div>
    <HeaderCmp :username="username" />
    <Slider />
    <Popular />
  </div>
</template>

<script>

import HeaderCmp from "./HeaderComponent.vue";
import Slider from "./SliderComponent.vue";
import Popular from "./PopularProducts.vue";

export default {
  components: {
    HeaderCmp,
    Slider,
    Popular,
  },
  data() {
    return {
      username: '',
      sharedData: null,
    };
  },
  mounted() {
    this.sharedData = JSON.parse(localStorage.getItem('sharedData'));
    this.username = JSON.parse(this.sharedData.config.data).username;
  }
}
</script>

<style>
* {
  margin: 0;
  box-sizing: border-box;
}
</style>
