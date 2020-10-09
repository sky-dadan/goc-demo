import VueRouter from 'vue-router'
import Vue from 'vue'
import App from '../App.vue'

const Trouble = () => import("../components/Trouble.vue")
const Department = () => import("../components/Department.vue")
const TroubleType = () => import("../components/TroubleType.vue")

const originalPush = VueRouter.prototype.push
const originalReplace = VueRouter.prototype.replace
VueRouter.prototype.push = function push(location) {
   return originalPush.call(this, location).catch(err => err)
}
VueRouter.prototype.replace = function replace(location) {
  return originalReplace.call(this, location).catch(err=>err)
}

// 1, 通过Vue.use()安装插件
Vue.use(VueRouter)

// 2, 创建VueRouter对象
const routes = [
  {
    path: '/trouble',
    component:Trouble,
    meta: {
      title: "故障页面"
    }
  },
  {
    path: '/department',
    component: Department,
    meta: {
      title: "部门页面"
    }
  },
  {
    path: '/troubletype',
    component: TroubleType
  }
]

const router = new VueRouter({
  routes: routes,
  mode: "history"
})

export default router