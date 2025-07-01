<template>
  <div>
    <div v-if="task.task_type === 1">
      <div>
        <span>시나리오: URA</span>
      </div>
      <div>
        <span>목표 스테이터스: {{task.detail?.expect_attribute}}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "UmamusumeTaskDetailInfo",
  props: ["task"],
}
</script>

<style scoped>

</style>