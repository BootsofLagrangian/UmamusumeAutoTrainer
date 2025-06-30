<template>
  <div>
    <div class="card">
      <div class="card-body">
        <div class="d-flex bd-highlight">
          <h5 class="card-title">Scheduled Tasks</h5>
        </div>
      </div>
      <TaskList v-bind:task-list="cronJobList" v-bind:no-data-label="'No scheduled tasks'"></TaskList>
    </div>
  </div>
</template>

<script>
import TaskList from "./TaskList.vue";

export default {
  name: "CronJobList",
  props:["cronJobList"],
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