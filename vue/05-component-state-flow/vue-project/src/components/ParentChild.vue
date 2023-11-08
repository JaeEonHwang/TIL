<template>
  <div>
    <p>{{ myMsg }}</p>
    <p>{{ dynamicProps }}</p>
    <ParentGrandChild @update-name="updateName" :my-msg="myMsg"/>
    <button @click="buttonClick">클릭</button>
    <button @click="emitArgs">추가 인자 전달</button>
  </div>
</template>

<script setup>
  import ParentGrandChild from '@/components/ParentGrandChild.vue'
  defineProps({
    myMsg: String,
    dynamicProps: String,
  })

  const emit = defineEmits(['someEvent', 'emitArgs', 'updateName'])

  const buttonClick = function () {
    emit('someEvent')
  }

  const emitArgs = function () {
    emit('emitArgs', 1, 2, 3)
  }

  const updateName = function () {
    emit('updateName')
  }

</script>

<style scoped>

</style>