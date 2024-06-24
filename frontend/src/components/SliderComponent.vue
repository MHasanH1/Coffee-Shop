<template>
  <div class="container">
    <div class="owl-carousel owl-theme">
      <div class="item"><h4>1</h4></div>
      <div class="item"><h4>2</h4></div>
      <div class="item"><h4>3</h4></div>
      <div class="item"><h4>4</h4></div>
      <div class="item"><h4>5</h4></div>
      <div class="item"><h4>6</h4></div>
      <div class="item"><h4>7</h4></div>
      <div class="item"><h4>8</h4></div>
      <div class="item"><h4>9</h4></div>
      <div class="item"><h4>10</h4></div>
      <div class="item"><h4>11</h4></div>
      <div class="item"><h4>12</h4></div>
    </div>
  </div>
</template>

<script>
import { onMounted } from 'vue';
import 'owl.carousel/dist/assets/owl.carousel.css';
import 'owl.carousel';

export default {
  name: 'CarouselComponent',
  setup() {
    onMounted(() => {
      if (typeof window !== 'undefined' && window.$) {
        window.$('.owl-carousel').owlCarousel({
          loop: true,
          margin: 10,
          autoplay:true,
          autoplayTimeout:2000,
          autoplayHoverPause:true,
          nav: true,
          navText: [
            '<span class="custom-prev">‹</span>',
            '<span class="custom-next">›</span>'
          ],
          responsive: {
            0: {
              items: 3
            },
            600: {
              items: 3
            },
            1000: {
              items: 3
            }
          }
        });
      }
    });
  },
};
</script>

<style>
/* Add any custom styles for your carousel */
.owl-carousel .item {
  background: #4a90e2;
  padding: 30px;
  margin: 3px;
  color: #FFF;
  border-radius: 3px;
  text-align: center;
}

.owl-nav {
  justify-content: center;
  display: flex;
  gap: 2rem;
}

.custom-prev {
  font-size: 30pt;
}

.custom-next {
  font-size: 30pt;
}

</style>
