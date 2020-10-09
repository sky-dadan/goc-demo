<template>
  <div class="content">

  <el-button @click="showdialogForm" type="success">添加故障</el-button>
  <el-dialog title="添加故障类型" :visible.sync="dialogFormVisible">
  <el-form :model="form">
    <el-form-item label="故障类型" :label-width="formLabelWidth">
      <el-input v-model="form.name" autocomplete="off"></el-input>
    </el-form-item>
  </el-form>
  <div slot="footer" class="dialog-footer">
    <el-button @click="dialogFormVisible = false">取 消</el-button>
    <el-button type="primary" @click="addTroubletype">确 定</el-button>
  </div>
  </el-dialog>

  <el-table
    ref="filterTable"
    :data="troubletypes"
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
      troubletypes:null,
      dialogFormVisible: false,
      dialogTableVisible: false,
      formLabelWidth: '120px',
      form: {
          name: '',
          region: '',
          date1: '',
          date2: '',
          delivery: false,
          type: [],
          resource: '',
          desc: ''
        },
    }
  },
  created() {
    axios.get("http://127.0.0.1:8000/apiv1/troubletypes").then(
      (res) => {
        this.troubletypes = res.data.data
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
    addTroubletype(){
      console.log("addTroubletype")
      this.dialogFormVisible = false
      console.log(this.form.name)
    },
    showdialogForm(){
      this.dialogFormVisible = !this.dialogFormVisible
      console.log(this.dialogFormVisible)
      
    }
  }
}
</script>

<style>
  .content {
    margin-top: 10px;
  }
</style>
