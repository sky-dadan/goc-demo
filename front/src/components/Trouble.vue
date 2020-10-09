<template>
<div class="content">
  <el-button @click="addTrouble" type="success">添加故障</el-button>    
    <el-table
      :data="troublelist"
      style="width: 80%"
      :row-class-name="tableRowClassName"
      >
      <el-table-column
        prop="title"
        label="故障名称"
        width="180">
      </el-table-column>
      <el-table-column
        prop="department_name"
        label="所属部门">
      </el-table-column>
      <el-table-column
        prop="troubletype_name"
        label="故障类型">
      </el-table-column>
      <el-table-column
        prop="createtime"
        label="日期"
        width="180">
      </el-table-column>
    </el-table>
</div>
</template>


<script>
import axios from "axios"
export default {
  name: "User",
  data(){
    return {
      troublelist: null,  
    }
  },
  methods: {
    tableRowClassName({rowIndex}) {
      if (rowIndex % 3 == 0) {
        return 'warning-row';
      } else if (rowIndex % 3 == 2) {
        return 'success-row';
      }
      return '';
    },
    addTrouble() {
      console.log("addTrouble")
    }
  },
  created: function(){
    console.log(this.nums)
    axios.get("http://127.0.0.1:8000/apiv1/troubles", {
      params:{}
    }).then((res) =>{
      this.troublelist = res.data.data
      console.log(this.troublelist)
    }).catch(function(error){
      console.log(error)
    })
  }
}
</script>


<style>
  .el-table .warning-row {
    background: oldlace;
  }

  .el-table .success-row {
    background: #f0f9eb;
  }
</style>