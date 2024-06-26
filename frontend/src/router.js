import {createRouter, createWebHashHistory} from "vue-router";
import SignUp from "@/components/SignUp.vue";
import Home from "@/components/HomeComponent.vue";
import LogIn from "@/components/LogIn.vue";
import ShoppingCart from "./components/ShoppingCart.vue";
import ProfileComponent from "./components/ProfileComponent.vue";

const routes = [
    {path: "/", component: Home},
    {path: "/signup", component: SignUp},
    {path: "/login", component: LogIn},
    {path: "/cart", component: ShoppingCart},
    {path: "/profile", component: ProfileComponent},
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

export default router;