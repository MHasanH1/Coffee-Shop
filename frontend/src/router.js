import {createRouter, createWebHashHistory} from "vue-router";
import SignUp from "@/components/SignUp.vue";
import Home from "@/components/HomeComponent.vue";
import LogIn from "@/components/LogIn.vue";
import ShopManagement from '@/components/ShopManagement.vue'

const routes = [
    {path: "/", component: Home},
    {path: "/signup", component: SignUp},
    {path: "/login", component: LogIn},
    {path: "/ShopManagement", component: ShopManagement},
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

export default router;