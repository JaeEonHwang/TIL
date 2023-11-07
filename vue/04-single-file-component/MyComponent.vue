<template>
  <div class="greeting">
    {{ msg }}
    <input v-model="msg">
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const msg = ref('Hello World!')
</script>

<style scoped>
  .greeting {
    color: red;
  }
</style>