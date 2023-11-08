<template>
  <div>
    <ParentChild
      @update-name="updateName"
      @some-event="someCallback" 
      @emit-args="getNumbers"
      my-msg="message" 
      :dynamic-props="name"/>
  </div>
</template>

<script setup>
  import ParentChild from '@/components/ParentChild.vue'
  import { ref } from 'vue'

  const name = ref('Alice')
  const someCallback = function () {
    console.log('parentchild가 발실한 이벤트를 수신함')
  }
  const getNumbers = function (...args) {
    console.log(args)
  }
  
  const updateName = function () {
    name.value = 'Bella'
  }
</script>

<style scoped>

</style>