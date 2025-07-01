<template>
  <div>
    <div class="card">
      <div class="card-body">
        <div class="d-flex bd-highlight">
          <h5 class="card-title">UAT</h5>
          <span v-on:click="autoStart"  class="ml-auto btn auto-btn">시작</span>
          <span v-on:click="autoStop" class="btn auto-btn" >중지</span>
          <span class="btn auto-btn" data-target="#create-task-list-modal" data-toggle="modal">작업 생성</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AutoStatusPanel",
  methods:{
    autoStart:function (){
      this.axios.post("/action/bot/start").then(
          ()=>{
          }
      )
    },
    autoStop:function (){
      this.axios.post("/action/bot/stop").then(
          ()=>{
          }
      )
    }
  }
}
</script>

<style scoped>
  .btn+.btn{
    margin-left: 5px;
  }
</style>