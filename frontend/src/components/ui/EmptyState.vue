<script setup>
defineProps({
  title: {
    type: String,
    default: 'No data found',
  },
  message: {
    type: String,
    default: 'Try adjusting your filters to discover more results.',
  },
})
</script>

<template>
  <div class="rounded-2xl border border-dashed border-slate-300 bg-white/70 p-8 text-center shadow-sm">
    <p class="text-lg font-semibold text-slate-800">{{ title }}</p>
    <p class="mt-2 text-sm text-slate-600">{{ message }}</p>
  </div>
</template>
