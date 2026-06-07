<script setup>
import { computed, onMounted, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import { fetchMovieById } from '@/api/movieApi'
import EmptyState from '@/components/ui/EmptyState.vue'
import ErrorState from '@/components/ui/ErrorState.vue'
import LoadingState from '@/components/ui/LoadingState.vue'
import PillBadge from '@/components/ui/PillBadge.vue'
import { getReleaseYear, listNames } from '@/utils/movieFormatters'

const route = useRoute()
const movie = ref(null)
const loading = ref(true)
const errorMessage = ref('')

const cast = computed(() => movie.value?.actors || [])

async function loadMovie() {
  loading.value = true
  errorMessage.value = ''

  try {
    movie.value = await fetchMovieById(route.params.id)
  } catch (error) {
    errorMessage.value = error.message || 'Failed to load movie details.'
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadMovie()
})

watch(
  () => route.params.id,
  () => {
    loadMovie()
  },
)
</script>

<template>
  <section class="space-y-6">
    <RouterLink to="/" class="inline-flex text-sm font-semibold text-sky-700 hover:text-sky-900">
      ← Back to movies
    </RouterLink>

    <LoadingState v-if="loading" />
    <ErrorState v-else-if="errorMessage" :message="errorMessage" />

    <article
      v-else-if="movie"
      class="overflow-hidden rounded-3xl border border-white/30 bg-white/85 shadow-sm"
    >
      <div class="bg-gradient-to-r from-amber-100 via-sky-100 to-emerald-100 p-6 md:p-8">
        <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
          <div>
            <p class="text-xs font-semibold uppercase tracking-[0.24em] text-slate-500">Movie Detail</p>
            <h2 class="mt-2 text-3xl font-semibold text-slate-900 md:text-4xl">{{ movie.title }}</h2>
          </div>
          <PillBadge tone="amber">Released {{ getReleaseYear(movie.release_date) }}</PillBadge>
        </div>
      </div>

      <div class="grid gap-6 p-6 md:grid-cols-2 md:p-8">
        <section class="space-y-3 rounded-2xl border border-slate-200 bg-slate-50/70 p-5">
          <h3 class="text-lg font-semibold text-slate-900">Director</h3>
          <RouterLink
            v-if="movie.director"
            :to="`/staff/${movie.director.id}`"
            class="text-base font-medium text-sky-700 hover:text-sky-900"
          >
            {{ movie.director.name }}
          </RouterLink>
          <p v-else class="text-slate-600">N/A</p>
        </section>

        <section class="space-y-3 rounded-2xl border border-slate-200 bg-slate-50/70 p-5">
          <h3 class="text-lg font-semibold text-slate-900">Genres</h3>
          <p class="text-slate-700">{{ listNames(movie.genre) }}</p>
        </section>

        <section class="space-y-3 rounded-2xl border border-slate-200 bg-slate-50/70 p-5 md:col-span-2">
          <h3 class="text-lg font-semibold text-slate-900">Cast</h3>
          <ul v-if="cast.length" class="grid gap-2 sm:grid-cols-2 lg:grid-cols-3">
            <li v-for="actor in cast" :key="actor.id">
              <RouterLink
                :to="`/staff/${actor.id}`"
                class="block rounded-xl border border-white bg-white px-3 py-2 text-sm font-medium text-slate-700 transition hover:border-sky-300 hover:text-sky-800"
              >
                {{ actor.name }}
              </RouterLink>
            </li>
          </ul>
          <p v-else class="text-slate-600">No cast information available.</p>
        </section>
      </div>
    </article>

    <EmptyState
      v-else
      title="Movie not found"
      message="This movie may have been removed or is not available right now."
    />
  </section>
</template>
