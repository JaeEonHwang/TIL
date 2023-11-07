<!-- <template>
  <div>
    <p>MyComponentItem</p>
  </div>
</template>

<script setup>

</script>

<style scoped>

</style> -->


<template>
  <div>
    <input type="text" ref="input">
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue'

  const input = ref('home')

  console.log(input.value)
</script>

<style scoped>

</style>