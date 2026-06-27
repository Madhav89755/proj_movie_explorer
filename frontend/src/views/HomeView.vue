<script setup>
import { computed, onMounted, ref } from 'vue'
import { fetchMoviesWithDetails } from '@/api/movieApi'
import MovieCard from '@/components/movie/MovieCard.vue'
import MovieFilters from '@/components/movie/MovieFilters.vue'
import { fetchGenres, fetchStaffList } from '@/api/staffApi'
import EmptyState from '@/components/ui/EmptyState.vue'
import ErrorState from '@/components/ui/ErrorState.vue'
import LoadingState from '@/components/ui/LoadingState.vue'
import PaginationControls from '@/components/ui/PaginationControls.vue'

const movies = ref([])
const loading = ref(true)
const errorMessage = ref('')
const genres = ref([])
const staff = ref([])
const totalMovies = ref(0)
const pageSize = 12
const currentPage = ref(1)

const totalPages = computed(() => {
  if (!totalMovies.value) {
    return 1
  }

  return Math.ceil(totalMovies.value / pageSize)
})

const filters = ref({
  title: '',
  genre_id: '',
  actor_id: '',
  director_id: '',
  ordering: '-release_date',
  overall_rating:''
})

async function loadFilterOptions() {
  const [genreResults, staffResults] = await Promise.all([fetchGenres(), fetchStaffList()])
  genres.value = genreResults
  staff.value = staffResults
}

async function loadMovies() {
  loading.value = true
  errorMessage.value = ''

  try {
    const response = await fetchMoviesWithDetails({
      ...filters.value,
      limit: pageSize,
      offset: (currentPage.value - 1) * pageSize,
    })
    movies.value = response.results
    totalMovies.value = response.count
  } catch (error) {
    errorMessage.value = error.message || 'Unable to load movies right now.'
  } finally {
    loading.value = false
  }
}

function onApplyFilters() {
  currentPage.value = 1
  loadMovies()
}

function onResetFilters() {
  currentPage.value = 1
  filters.value = {
    title: '',
    genre_id: '',
    actor_id: '',
    director_id: '',
    ordering: '-release_date',
    overall_rating:''
  }
  loadMovies()
}

function onPageChange(page) {
  currentPage.value = page
  loadMovies()
}

onMounted(async () => {
  try {
    await loadFilterOptions()
  } catch {
    errorMessage.value = 'Could not load filter options. You can still browse available movies.'
  } finally {
    await loadMovies()
  }
})
</script>

<template>
  <section class="space-y-6">
    <div class="flex flex-col gap-2 md:flex-row md:items-end md:justify-between">
      <div>
        <p class="text-xs font-semibold uppercase tracking-[0.24em] text-slate-500">Catalog</p>
        <h2 class="mt-1 text-2xl font-semibold text-slate-900 md:text-3xl">Browse Movies</h2>
      </div>
      <p class="text-sm text-slate-600">
        Showing {{ movies.length }} of {{ totalMovies }} movies | Page {{ currentPage }} of
        {{ totalPages }}
      </p>
    </div>

    <MovieFilters
      v-model="filters"
      :genres="genres"
      :staff="staff"
      @apply="onApplyFilters"
      @reset="onResetFilters"
    />

    <div class="flex justify-end">
      <RouterLink
        to="/create"
        class="rounded-xl bg-slate-900 px-4 py-2 text-sm font-semibold text-white transition hover:bg-slate-700"
      >
        Add Movie
      </RouterLink>
    </div>

    <LoadingState v-if="loading" />
    <ErrorState v-else-if="errorMessage" :message="errorMessage" />

    <div v-else-if="movies.length" class="grid gap-5 sm:grid-cols-2 xl:grid-cols-3">
      <MovieCard v-for="movie in movies" :key="movie.id" :movie="movie" />
    </div>

    <EmptyState
      v-else
      title="No matching movies"
      message="Try broadening your filters to see more titles in the catalog."
    />

    <PaginationControls
      v-if="!loading && !errorMessage && movies.length && totalMovies > pageSize"
      :current-page="currentPage"
      :total-pages="totalPages"
      @change="onPageChange"
    />
  </section>
</template>
