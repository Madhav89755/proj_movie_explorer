<script setup>
import AppHeader from '@/components/layout/AppHeader.vue'
</script>

<template>
  <div class="min-h-screen bg-app-gradient px-4 py-6 md:px-6 md:py-8">
    <div class="mx-auto flex w-full max-w-7xl flex-col gap-6">
      <AppHeader />
      <main class="rounded-3xl border border-white/45 bg-white/60 p-4 shadow-xl backdrop-blur md:p-6">
        <RouterView />
      </main>
    </div>
  </div>
</template>
