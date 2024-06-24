<template>
  <div>
    <HeaderCmp />
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
    };
  }
}
</script>

<style>
* {
  margin: 0;
  box-sizing: border-box;
}
</style>
