<template>
  <div class="content">
  <el-button @click="addDepartment" type="success">添加部门</el-button>    
  <el-table
    :data="departments"
    style="width: 100%"
    height="550">
    <el-table-column
      fixed
      prop="id"
      label="id"
      width="150">
    </el-table-column>
    <el-table-column
      prop="name"
      label="部门名称"
      width="120">
    </el-table-column>
    <el-table-column
      
      label="操作"
      width="100">
      <template slot-scope="scope">
        <el-button @click="handleClick(scope.row)" type="text" size="small">编辑</el-button>
        <el-button @click="deleteClick(scope.row)"type="text" size="small">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
  </div>
</template>


<script>
import axios from "axios"
export default {
  data() {
    return {
      departments:null
    }
  },
  created() {
    axios.get("http://127.0.0.1:8000/apiv1/departments").then(
      (res) => {
        this.departments = res.data.data
      }
    ).catch( err => console.log(err))
  },
  methods: {
    handleClick(row){
      console.log(row)
    },
    deleteClick(row){
      console.log(row)
    },
    addDepartment(){
      console.log("addDepartment")
    }
  }
}
</script>
