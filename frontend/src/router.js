import {createRouter, createWebHashHistory} from "vue-router";
import SignUp from "@/components/SignUp.vue";
import Home from "@/components/HomeComponent.vue";
import LogIn from "@/components/LogIn.vue";
<<<<<<< HEAD
import ShopManagement from '@/components/ShopManagement.vue'
=======
import ShoppingCart from "./components/ShoppingCart.vue";
import ProfileComponent from "./components/ProfileComponent.vue";
>>>>>>> 8f4b209b8829b282107e0a297d9ec8e76368e402

const routes = [
    {path: "/", component: Home},
    {path: "/signup", component: SignUp},
    {path: "/login", component: LogIn},
<<<<<<< HEAD
    {path: "/ShopManagement", component: ShopManagement},
=======
    {path: "/cart", component: ShoppingCart},
    {path: "/profile", component: ProfileComponent},
>>>>>>> 8f4b209b8829b282107e0a297d9ec8e76368e402
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

export default router;