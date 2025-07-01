<template>
  <div>
    <div class="card">
      <div class="card-body">
        <div class="d-flex bd-highlight">
          <h5 class="card-title">완료된 작업</h5>
        </div>
      </div>
      <TaskList v-bind:task-list="historyTaskList" v-bind:no-data-label="'완료된 작업 없음'"></TaskList>
    </div>
  </div>
</template>

<script>
import TaskList from "./TaskList.vue";

export default {
  name: "HistoryTaskPanel",
  props:["historyTaskList"],
  components: {TaskList},
  data:function (){
    return{
    }
  }
}
</script>

<style scoped>
.card-title{
  margin-bottom: 0;
}
.start-time{
  color: #999;
}
.card-body{
  border-bottom: 1px solid rgba(0,0,0,.125);
}
</style>