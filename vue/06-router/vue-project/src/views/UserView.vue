<template>
  <div>
    <h1>UserView</h1>
    <h2>{{ userId }}번 유저의 페이지입니다.</h2>
    <button @click="goHome">홈</button>
    <button @click="routeUpdate">다른 유저</button>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'

  const route = useRoute()
  const userId = ref(route.params.id)
  const router = useRouter()
  const goHome = function () {
    // router.push({ name: 'home' })
    router.replace({ name: 'home' })
  }

  onBeforeRouteLeave((to, from) => {
    const answer = window.confirm('가지마')
    if (!answer) {
      return false
    }
  })

  const routeUpdate = function () {
    router.push({ name: 'user', params: { id: 100 } })
  }

  onBeforeRouteUpdate((to, from) => {
    userId.value = to.params.id
  })
</script>

<style scoped>

</style>