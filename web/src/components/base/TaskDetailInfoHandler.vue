<template>
  <div>
    <div v-if="task.app_name === 'umamusume'">
      <div>
        <span v-if="task.task_start_time !== undefined" class="small time">{{task.task_start_time}}</span>
        <span v-if="task.end_task_time !== undefined" class="small time"> ~ {{task.end_task_time}}</span>
        <span v-if= "task.task_start_time === undefined" class="small time">시작 안함</span>
        <div v-if="task.task_execute_mode === 'CRON_JOB'" class="small time">다음 실행 시간: {{task.cron_job_info?.next_time}} ({{task.cron_job_info?.cron}})</div>
      </div>
      <div class="btn-group float-right" role="group" aria-label="Basic example">
        <button type="button" class="btn auto-btn" v-on:click="resetTask">초기화</button>
        <button type="button" class="btn auto-btn" v-on:click="deleteTask">삭제</button>
      </div>
      <UmamusumeTaskDetailInfo :task="task"></UmamusumeTaskDetailInfo>
      <div v-if="task.end_task_reason !== undefined && task.end_task_reason != ''">
        <span>상태: {{task.task_status}} ({{task.end_task_reason}})</span>
      </div>
      <div v-if="task.detail.cultivate_result.factor_list !== undefined && task.detail.cultivate_result.factor_list.length !== 0">
        획득 인자: <span class="mr-1" v-for="factor in task.detail.cultivate_result.factor_list">
          <span v-if="factor[0] === 'Speed' || factor[0] === 'Stamina'|| factor[0] === 'Power'|| factor[0] === 'Guts'|| factor[0] === 'Wisdom'"  style="background-color: #49BFF7;" class="badge badge-pill badge-secondary">{{factor[0]}}({{factor[1]}})</span>
          <span v-if="factor[0] === 'Sprint' || factor[0] === 'Mile'|| factor[0] === 'Medium Distance'|| factor[0] === 'Long Distance'|| factor[0] === 'Dirt'|| factor[0] === 'Turf'|| factor[0] === 'Pace Setter'|| factor[0] === 'Front Runner'|| factor[0] === 'Mid-pack'|| factor[0] === 'Closer'"  style="background-color: #FF78B2;" class="badge badge-pill badge-secondary">{{factor[0]}}({{factor[1]}})</span>
          <span v-if="factor[0] !== 'Speed' && factor[0] !== 'Stamina'&& factor[0] !== 'Power'&& factor[0] !== 'Guts'&& factor[0] !== 'Wisdom'&& factor[0] !== 'Sprint' && factor[0] !== 'Mile'&& factor[0] !== 'Medium Distance'&& factor[0] !== 'Long Distance'&& factor[0] !== 'Dirt'&& factor[0] !== 'Turf' &&factor[0] !== 'Pace Setter'&& factor[0] !== 'Front Runner'&& factor[0] !== 'Mid-pack'&& factor[0] !== 'Closer'" 
            style="background-color: #E0E0E0; color: #794016;" class="badge badge-pill badge-secondary">{{factor[0]}}({{factor[1]}})</span>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import UmamusumeTaskDetailInfo from "@/components/umamusume/UmamusumeTaskDetailInfo.vue";
export default {
  name: "TaskDetailInfoHandler",
  components: {UmamusumeTaskDetailInfo},
  props: ["task"],
  methods: {
    resetTask: function (){
      let payload = {
        task_id: this.task.task_id
      }
      console.log(JSON.stringify(payload))
      this.axios.post("/action/bot/reset-task", JSON.stringify(payload)).then()
    },
    deleteTask: function (){
      let payload = {
        task_id: this.task.task_id
      }
      console.log(JSON.stringify(payload))
      this.axios.delete("/task", JSON.stringify(payload)).then()
    },
  }
}
</script>

<style scoped>
.time{
  color: #999;
}
</style>