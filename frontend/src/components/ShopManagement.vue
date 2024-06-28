<template>
  <div>
    <div class="header bg-dark d-flex justify-content-between align-items-center p-1">
      <button class="btn">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6 svgSize">
          <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
        </svg>
      </button>
      <button @click="this.$router.push('/')" class="btn">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6 svgSize">
          <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 9V5.25A2.25 2.25 0 0 0 13.5 3h-6a2.25 2.25 0 0 0-2.25 2.25v13.5A2.25 2.25 0 0 0 7.5 21h6a2.25 2.25 0 0 0 2.25-2.25V15m3 0 3-3m0 0-3-3m3 3H9" />
        </svg>
      </button>

    </div>
    <div class="d-flex gap-2">
      <div class="w-25 bg-info p-2">

        <button @click="this.$router.push('/stackManagement')" class="fw-bold d-block my-1 btn btn-outline-dark border-0">Stack Management</button>
        <button @click="this.$router.push('/addProduct')" class="fw-bold d-block btn btn-outline-dark border-0">Add Product</button>

      </div>
      <div class="chart-container w-75">
        <h1 class="text-center">{{!selectedOption ? 'Coffee' : selectedOption}}</h1>
        <Bar
            id="my-chart-id"
            :options="chartOptions"
            :data="chartData"
        />
          <fieldset class="d-flex align-items-center gap-5">
            <div class="d-flex align-items-center gap-1" v-for="product in products" :key="product.id">
              <input type="radio" :value="product.name" v-model="selectedOption" @click="select(product)"/>
              <label for="huey">{{ product.name }}</label>
            </div>

            <!-- <div class="d-flex align-items-center gap-1">
              <input type="radio" value="Cake" v-model="selectedOption" />
              <label for="dewey">Cake</label>
            </div>

            <div class="d-flex align-items-center gap-1">
              <input type="radio" value="Milk" v-model="selectedOption" />
              <label for="louie">Milk</label>
            </div> -->
          </fieldset>
      </div>
    </div>
  </div>
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
import axios from 'axios';

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChart',
  components: { Bar },
  data() {
    return {
      chartData: {
        labels: ['mmd'],
        datasets: [ { data: [1] } ]
      },
      chartOptions: {
        responsive: true
      },
      selectedOption: null,
      products:[
        {
          id : 0,
          name : '',
          history:{
            month : '',
            count : 0,
          }

        }
      ],
    }
  },
  methods:{
    getData(){
      axios.get('http://localhost:8000/api/chart/')
      .then(res=>{
        console.log(res.data);
        this.products=res.data;
      })
      .catch(err=>{
        console.log(err);
      })
    },
    select(product){
      console.log(product);
      this.chartData.labels = product.history.map(item => item.month);
      // this.chartData.labels=array;
      // this.chartData.datasets[0].data = product.history.map(item => item.count);
      console.log(this.chartData.labels);
      // console.log(this.chartData.datasets[0].data);
    }
  },
  mounted(){
    this.getData();
    console.log(this.chartData.labels);
    // console.log(this.chartData.datasets[0].data);
  }
}
</script>

<style scoped>

.chart-container {
  width: 75%;
  height: 100%; /* Ensure the chart container has a height */
}

.svgSize {
  width: 40px;
  height: 40px;
  color: white;
}
</style>
