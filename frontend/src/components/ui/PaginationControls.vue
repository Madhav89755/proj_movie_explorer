<script setup>
import { computed } from 'vue'

const props = defineProps({
  currentPage: {
    type: Number,
    required: true,
  },
  totalPages: {
    type: Number,
    required: true,
  },
})

const emit = defineEmits(['change'])

const visiblePages = computed(() => {
  if (props.totalPages <= 7) {
    return Array.from({ length: props.totalPages }, (_, index) => index + 1)
  }

  const pages = new Set([1, props.totalPages, props.currentPage])
  pages.add(Math.max(1, props.currentPage - 1))
  pages.add(Math.max(1, props.currentPage - 2))
  pages.add(Math.min(props.totalPages, props.currentPage + 1))
  pages.add(Math.min(props.totalPages, props.currentPage + 2))

  return Array.from(pages).sort((a, b) => a - b)
})

const pageItems = computed(() => {
  const items = []

  visiblePages.value.forEach((page, index) => {
    items.push({ type: 'page', value: page })

    const nextPage = visiblePages.value[index + 1]
    if (nextPage && nextPage - page > 1) {
      items.push({ type: 'ellipsis', value: `ellipsis-${page}` })
    }
  })

  return items
})

function goToPage(page) {
  if (page < 1 || page > props.totalPages || page === props.currentPage) {
    return
  }

  emit('change', page)
}
</script>

<template>
  <nav
    class="mt-2 flex flex-wrap items-center justify-center gap-2 rounded-2xl border border-white/40 bg-white/80 p-3 shadow-sm"
    aria-label="Movie pagination"
  >
    <button
      type="button"
      class="rounded-lg border border-slate-300 px-3 py-1.5 text-sm font-semibold text-slate-700 transition hover:bg-slate-100 disabled:cursor-not-allowed disabled:opacity-50"
      :disabled="currentPage === 1"
      @click="goToPage(currentPage - 1)"
    >
      Previous
    </button>

    <template v-for="item in pageItems" :key="item.value">
      <button
        v-if="item.type === 'page'"
        type="button"
        class="rounded-lg px-3 py-1.5 text-sm font-semibold transition"
        :class="
          item.value === currentPage
            ? 'bg-slate-900 text-white'
            : 'border border-slate-300 text-slate-700 hover:bg-slate-100'
        "
        @click="goToPage(item.value)"
      >
        {{ item.value }}
      </button>
      <span v-else class="px-1 text-slate-500">...</span>
    </template>

    <button
      type="button"
      class="rounded-lg border border-slate-300 px-3 py-1.5 text-sm font-semibold text-slate-700 transition hover:bg-slate-100 disabled:cursor-not-allowed disabled:opacity-50"
      :disabled="currentPage === totalPages"
      @click="goToPage(currentPage + 1)"
    >
      Next
    </button>
  </nav>
</template>
