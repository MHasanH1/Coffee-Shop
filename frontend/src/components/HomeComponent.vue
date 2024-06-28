<template>
  <div>
    <HeaderCmp />
    <Slider />
    <Popular />
  </div>
</template>

<script>

import Slider from "./SliderComponent.vue";
import Popular from "./PopularProducts.vue";
import HeaderCmp from "@/components/HeaderComponent.vue";

export default {
  components: {
    Slider,
    Popular,
    HeaderCmp
  },
}
</script>

<style>
* {
  margin: 0;
  box-sizing: border-box;
}
</style>
