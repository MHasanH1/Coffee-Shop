<template>
  <div class="album py-5 bg-body-tertiary">
    <div class="container">
      <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
        <div v-for="(card, index) in visibleCards" :key="index" class="col">
          <div class="card shadow-sm">
            <svg class="bd-placeholder-img card-img-top" width="100%" height="225" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Thumbnail" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#55595c"></rect><text x="50%" y="50%" fill="#eceeef" dy=".3em">Thumbnail</text></svg>
            <div class="card-body">
              <h4>{{card?.title}}</h4>
              <p class="card-text">{{card?.content}}</p>
              <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                  <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                  <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
                </div>
                <small class="text-body-secondary">9 mins</small>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="d-flex my-4">
        <button class="btn btn-outline-primary" v-if="!showAll" @click="showAllCards">See More</button>
        <button class="btn btn-success" v-if="showAll" @click="showLessCards">See Less</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cards: [
        { title: 'Card 1', content: 'This is the content of card 1.' },
        { title: 'Card 2', content: 'This is the content of card 2.' },
        { title: 'Card 3', content: 'This is the content of card 3.' },
        { title: 'Card 4', content: 'This is the content of card 4.' },
        { title: 'Card 5', content: 'This is the content of card 5.' },
        { title: 'Card 6', content: 'This is the content of card 6.' },
        { title: 'Card 7', content: 'This is the content of card 7.' },
        { title: 'Card 8', content: 'This is the content of card 8.' },
        { title: 'Card 9', content: 'This is the content of card 9.' },
        { title: 'Card 10', content: 'This is the content of card 10.' },
        { title: 'Card 11', content: 'This is the content of card 11.' },
        { title: 'Card 12', content: 'This is the content of card 12.' },
      ],
      showAll: false,
    }
  },
  computed: {
    visibleCards() {
      return this.showAll ? this.cards : this.cards.slice(0, 3);
    }
  },
  methods: {
    showAllCards() {
      this.showAll = true;
    },
    showLessCards() {
      this.showAll = false;
    }
  }
}
</script>

<style scoped>

</style>