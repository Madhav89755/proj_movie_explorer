<script setup>
import { computed, onMounted, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import { fetchMoviesWithDetails } from '@/api/movieApi'
import { fetchStaffById } from '@/api/staffApi'
import MovieMiniList from '@/components/movie/MovieMiniList.vue'
import StaffHero from '@/components/staff/StaffHero.vue'
import EmptyState from '@/components/ui/EmptyState.vue'
import ErrorState from '@/components/ui/ErrorState.vue'
import LoadingState from '@/components/ui/LoadingState.vue'
import { personRoleLabel } from '@/utils/movieFormatters'

const route = useRoute()

const person = ref(null)
const actorMovies = ref([])
const directorMovies = ref([])
const loading = ref(true)
const errorMessage = ref('')

const roleLabel = computed(() => personRoleLabel(actorMovies.value, directorMovies.value))

async function loadProfile() {
  loading.value = true
  errorMessage.value = ''

  try {
    person.value = await fetchStaffById(route.params.id)

    const [actorResponse, directorResponse] = await Promise.all([
      fetchMoviesWithDetails({ actor_id: route.params.id, limit: 50, ordering: '-release_date' }),
      fetchMoviesWithDetails({ director_id: route.params.id, limit: 50, ordering: '-release_date' }),
    ])

    actorMovies.value = actorResponse.results
    directorMovies.value = directorResponse.results
  } catch (error) {
    errorMessage.value = error.message || 'Unable to load profile information.'
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadProfile()
})

watch(
  () => route.params.id,
  () => {
    loadProfile()
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

    <template v-else-if="person">
      <StaffHero :person="person" :role-label="roleLabel" />

      <div class="grid gap-5 lg:grid-cols-2">
        <MovieMiniList title="As Actor" :movies="actorMovies" tone="sky" />
        <MovieMiniList title="As Director" :movies="directorMovies" tone="emerald" />
      </div>
    </template>

    <EmptyState
      v-else
      title="Staff profile not found"
      message="The selected actor or director does not exist anymore."
    />
  </section>
</template>
