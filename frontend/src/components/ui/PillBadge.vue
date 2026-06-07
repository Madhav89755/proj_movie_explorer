<script setup>
defineProps({
  tone: {
    type: String,
    default: 'blue',
  },
})

const toneClassMap = {
  blue: 'bg-sky-100 text-sky-900',
  amber: 'bg-amber-100 text-amber-900',
  green: 'bg-emerald-100 text-emerald-900',
  slate: 'bg-slate-100 text-slate-900',
}
</script>

<template>
  <span
    class="inline-flex rounded-full px-3 py-1 text-xs font-semibold uppercase tracking-wide"
    :class="toneClassMap[tone] || toneClassMap.slate"
  >
    <slot />
  </span>
</template>
