<template>
  <div>
    <Slider />
    <Popular />
  </div>
</template>

<script>

import Slider from "./SliderComponent.vue";
import Popular from "./PopularProducts.vue";

export default {
  components: {
    Slider,
    Popular,
  },
}
</script>

<style>
* {
  margin: 0;
  box-sizing: border-box;
}
</style>
