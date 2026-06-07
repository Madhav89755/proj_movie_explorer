<script setup>
defineProps({
  message: {
    type: String,
    default: 'Something went wrong while loading data.',
  },
})
</script>

<template>
  <div class="rounded-2xl border border-rose-200 bg-rose-50 p-6 text-rose-900">
    <p class="text-sm font-semibold uppercase tracking-[0.2em]">Error</p>
    <p class="mt-1 text-base">{{ message }}</p>
  </div>
</template>
