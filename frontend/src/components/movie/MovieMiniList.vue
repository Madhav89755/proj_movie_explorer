<script setup>
import { getReleaseYear } from '@/utils/movieFormatters'

defineProps({
  title: {
    type: String,
    required: true,
  },
  movies: {
    type: Array,
    default: () => [],
  },
  tone: {
    type: String,
    default: 'slate',
  },
})

const toneMap = {
  slate: 'border-slate-200 bg-white/90',
  sky: 'border-sky-200 bg-sky-50/70',
  emerald: 'border-emerald-200 bg-emerald-50/70',
}
</script>

<template>
  <section class="rounded-2xl border p-5 shadow-sm" :class="toneMap[tone] || toneMap.slate">
    <h3 class="text-xl font-semibold text-slate-900">{{ title }}</h3>

    <ul v-if="movies.length" class="mt-4 space-y-3">
      <li v-for="movie in movies" :key="movie.id" class="rounded-xl border border-white/70 bg-white/80 p-3">
        <RouterLink :to="`/movies/${movie.id}`" class="font-semibold text-slate-900 hover:text-sky-700">
          {{ movie.title }}
        </RouterLink>
        <p class="mt-1 text-sm text-slate-600">Release year: {{ getReleaseYear(movie.release_date) }}</p>
      </li>
    </ul>

    <p v-else class="mt-4 text-sm text-slate-600">No movies found in this category.</p>
  </section>
</template>
