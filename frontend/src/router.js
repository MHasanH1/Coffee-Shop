import {createRouter, createWebHashHistory} from "vue-router";
import SignUp from "@/components/SignUp.vue";
import Home from "@/components/HomeComponent.vue";
import LogIn from "@/components/LogIn.vue";
import ShopManagement from '@/components/ShopManagement.vue'
import ShoppingCart from "./components/ShoppingCart.vue";
import ProfileComponent from "./components/ProfileComponent.vue";
import CartHistory from '@/components/CartHistory.vue';

import AddProduct from '@/components/AddProduct.vue'
import StackManagement from '@/components/StackManagement.vue'
import ProductComponent from "@/components/ProductComponent.vue";


const routes = [
    {path: "/", component: Home},
    {path: "/signup", component: SignUp},
    {path: "/login", component: LogIn},
    {path: "/shopManagement", component: ShopManagement},
    {path: "/cart", component: ShoppingCart},
    {path: "/profile", component: ProfileComponent},
    {path: "/addProduct", component: AddProduct},
    {path: "/history", component: CartHistory},
    {path: "/stackManagement", component: StackManagement},
    {path: "/products:vertical", component: ProductComponent},
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

router.beforeEach((to, from, next) => {
    // console.log(to);
    // console.log(from);
    // console.log(next);
    if (to.path === '/' && from.path !== '/') {
        if (!localStorage.getItem('reload')) {
            localStorage['reload'] = true;
            window.location.reload();
        } else
            localStorage.removeItem('reload');
    }
    next();
});

export default router;