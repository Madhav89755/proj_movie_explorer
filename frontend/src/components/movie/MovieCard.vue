<script setup>
import PillBadge from '@/components/ui/PillBadge.vue'
import { getReleaseYear, listNames } from '@/utils/movieFormatters'

const props = defineProps({
  movie: {
    type: Object,
    required: true,
  },
})
</script>

<template>
  <article
    class="group h-full rounded-2xl border border-slate-200 bg-white/90 p-5 shadow-sm transition duration-200 hover:-translate-y-0.5 hover:shadow-lg"
  >
    <div class="flex items-start justify-between gap-3">
      <h3 class="text-xl font-semibold text-slate-900">{{ props.movie.title }}</h3>
      <PillBadge tone="amber">{{ getReleaseYear(props.movie.release_date) }}</PillBadge>
    </div>

    <p class="mt-3 text-sm text-slate-600">
      <span class="font-semibold text-slate-800">Director:</span>
      <RouterLink
        v-if="props.movie.director"
        :to="`/staff/${props.movie.director.id}`"
        class="ml-1 font-medium text-sky-700 hover:text-sky-900"
      >
        {{ props.movie.director.name }}
      </RouterLink>
      <span v-else class="ml-1">N/A</span>
    </p>

    <p class="mt-2 text-sm text-slate-600">
      <span class="font-semibold text-slate-800">Genres:</span> {{ listNames(props.movie.genre) }}
    </p>

    <div class="mt-5 flex items-center justify-between">
      <RouterLink
        :to="`/movies/${props.movie.id}`"
        class="inline-flex rounded-full bg-slate-900 px-4 py-2 text-sm font-semibold text-white transition hover:bg-slate-700"
      >
        View details
      </RouterLink>
      <p class="text-xs uppercase tracking-wide text-slate-500">Cast: {{ props.movie.actors?.length || 0 }}</p>
    </div>
  </article>
</template>
