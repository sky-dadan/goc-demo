<template>
  <div id="app">
    <el-button @click="troubleClick" type="primary">故障列表</el-button>
    <el-button @click="depClick" type="primary">部门列表</el-button>
    <el-button @click="troubletypeClick" type="primary">故障类型</el-button>
    
    
    <router-view></router-view>

  </div>
</template>


<script>
export default {
  name: "App",
  methods: {
    troubleClick(){
      console.log("troubleClick")
      this.$router.push("/trouble")
    },
    depClick(){
      console.log("depClick")
      this.$router.replace("/department")
    },
    troubletypeClick(){
      console.log("troubletypeClick")
      this.$router.replace("/troubletype")
    }
  }
}
</script>