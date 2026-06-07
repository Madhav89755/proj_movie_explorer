<script setup>
import { onMounted, ref } from 'vue'
import CreateMovieForm from '@/components/movie/CreateMovieForm.vue'
import { createMovie } from '@/api/movieApi'
import { fetchGenres, fetchStaffList } from '@/api/staffApi'
import ErrorState from '@/components/ui/ErrorState.vue'
import LoadingState from '@/components/ui/LoadingState.vue'

const genres = ref([])
const staff = ref([])
const loading = ref(true)
const actionMessage = ref('')
const actionError = ref('')
const creatingMovie = ref(false)

async function loadFormOptions() {
  const [genreResults, staffResults] = await Promise.all([fetchGenres(), fetchStaffList()])
  genres.value = genreResults
  staff.value = staffResults
}

async function onCreateMovie(payload) {
  creatingMovie.value = true
  actionError.value = ''
  actionMessage.value = ''

  try {
    await createMovie(payload)
    actionMessage.value = 'Movie added successfully.'
    await loadFormOptions()
  } catch (error) {
    actionError.value = error.message || 'Failed to create movie.'
  } finally {
    creatingMovie.value = false
  }
}

onMounted(async () => {
  loading.value = true
  actionError.value = ''

  try {
    await loadFormOptions()
  } catch (error) {
    actionError.value = error.message || 'Failed to load form options.'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <section class="space-y-6">
    <LoadingState v-if="loading" />

    <template v-else>
      <div>
        <CreateMovieForm :genres="genres" :staff="staff" :loading="creatingMovie" @submit="onCreateMovie" />
      </div>

      <div
        v-if="actionMessage"
        class="rounded-2xl border border-emerald-200 bg-emerald-50 px-4 py-3 text-sm font-medium text-emerald-900"
      >
        {{ actionMessage }}
      </div>

      <ErrorState v-if="actionError" :message="actionError" />
    </template>
  </section>
</template>
