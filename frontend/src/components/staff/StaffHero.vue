<script setup>
import PillBadge from '@/components/ui/PillBadge.vue'

defineProps({
  person: {
    type: Object,
    required: true,
  },
  roleLabel: {
    type: String,
    required: true,
  },
})
</script>

<template>
  <section
    class="rounded-3xl border border-white/35 bg-gradient-to-r from-slate-900 via-slate-700 to-sky-700 p-6 text-white shadow-lg"
  >
    <p class="text-xs font-semibold uppercase tracking-[0.24em] text-sky-100">Staff Profile</p>
    <h2 class="mt-2 text-3xl font-semibold">{{ person.name }}</h2>
    <div class="mt-4">
      <PillBadge tone="green">{{ roleLabel }}</PillBadge>
    </div>
  </section>
</template>
