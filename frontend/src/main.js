import { createApp } from 'vue';
import App from './App.vue';
import jQuery from 'jquery';
import router from "@/router";


import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'

window.$ = window.jQuery = jQuery;

import 'owl.carousel/dist/assets/owl.carousel.css';
import 'owl.carousel';

const app = createApp(App);
app.use(router);
app.mount('#app');
