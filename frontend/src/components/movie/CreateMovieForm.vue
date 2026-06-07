<script setup>
import { reactive, ref, watch } from 'vue'
import { createGenre, createStaff, fetchGenres, fetchStaffList } from '@/api/staffApi'

const props = defineProps({
  genres: {
    type: Array,
    default: () => [],
  },
  staff: {
    type: Array,
    default: () => [],
  },
  loading: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(['submit'])

const form = reactive({
  title: '',
  release_date: '',
  director: '',
  genre: [],
  actors: [],
})

const localGenres = ref([])
const localStaff = ref([])
const showAddGenre = ref(false)
const showAddActor = ref(false)
const newGenreName = ref('')
const newActorName = ref('')
const addingGenre = ref(false)
const addingActor = ref(false)
const inlineError = ref('')
const inlineMessage = ref('')

watch(
  () => props.genres,
  (value) => {
    localGenres.value = [...value]
  },
  { immediate: true },
)

watch(
  () => props.staff,
  (value) => {
    localStaff.value = [...value]
  },
  { immediate: true },
)

function normalizeIds(values) {
  return values.map((value) => Number(value)).filter((value) => Number.isInteger(value))
}

function onSubmit() {
  if (!form.title.trim() || !form.release_date || !form.director) {
    return
  }

  const payload = {
    title: form.title.trim(),
    release_date: form.release_date,
    director: Number(form.director),
    genre: normalizeIds(form.genre),
    actors: normalizeIds(form.actors),
  }

  emit('submit', payload)
}

async function refreshGenres() {
  localGenres.value = await fetchGenres()
}

async function refreshStaff() {
  localStaff.value = await fetchStaffList()
}

async function addGenre() {
  const name = newGenreName.value.trim()
  if (!name) {
    return
  }

  addingGenre.value = true
  inlineError.value = ''
  inlineMessage.value = ''

  try {
    const created = await createGenre({ name })
    await refreshGenres()
    form.genre = [...new Set([...form.genre, created.id])]
    newGenreName.value = ''
    showAddGenre.value = false
    inlineMessage.value = 'Genre added Successful.'
  } catch (error) {
    inlineError.value = error.message || 'Could not add genre.'
  } finally {
    addingGenre.value = false
  }
}

async function addActor() {
  const name = newActorName.value.trim()
  if (!name) {
    return
  }

  addingActor.value = true
  inlineError.value = ''
  inlineMessage.value = ''

  try {
    const created = await createStaff({ name })
    await refreshStaff()
    form.actors = [...new Set([...form.actors, created.id])]
    newActorName.value = ''
    showAddActor.value = false
    inlineMessage.value = 'Actor added and refreshed.'
  } catch (error) {
    inlineError.value = error.message || 'Could not add actor.'
  } finally {
    addingActor.value = false
  }
}
</script>

<template>
  <form
    class="relative overflow-hidden rounded-3xl border border-white/40 bg-white/85 p-5 shadow-sm backdrop-blur md:p-6"
    @submit.prevent="onSubmit"
  >
    <div class="absolute inset-x-0 top-0 h-16 bg-gradient-to-r from-amber-500/15 via-sky-500/10 to-emerald-500/15" />

    <div class="relative">
      <h3 class="text-xl font-semibold text-slate-900">Add Movie</h3>
      <p class="mt-1 text-sm text-slate-600">
        Fill in production details and attach cast information to publish a new title.
      </p>
    </div>

    <div class="mt-5 grid gap-4 md:grid-cols-2">
      <div class="rounded-2xl border border-slate-200 bg-white/75 p-4 md:col-span-2">
        <p class="text-xs font-semibold uppercase tracking-[0.2em] text-slate-500">Basics</p>
        <div class="mt-3 grid gap-4 md:grid-cols-2">
          <label class="space-y-2 text-sm text-slate-700">
            <span class="font-semibold">Title</span>
            <input
              v-model="form.title"
              type="text"
              class="w-full rounded-xl border border-slate-200 bg-white px-3 py-2.5 outline-none transition focus:border-sky-400 focus:ring-2 focus:ring-sky-200"
              placeholder="Enter movie title"
              required
            />
          </label>

          <label class="space-y-2 text-sm text-slate-700">
            <span class="font-semibold">Release Date</span>
            <input
              v-model="form.release_date"
              type="date"
              class="w-full rounded-xl border border-slate-200 bg-white px-3 py-2.5 outline-none transition focus:border-sky-400 focus:ring-2 focus:ring-sky-200"
              required
            />
          </label>
        </div>
      </div>

      <div class="rounded-2xl border border-slate-200 bg-white/75 p-4">
        <p class="text-xs font-semibold uppercase tracking-[0.2em] text-slate-500">Direction</p>
        <label class="mt-3 block space-y-2 text-sm text-slate-700">
          <span class="font-semibold">Director</span>
          <select
            v-model="form.director"
            class="w-full rounded-xl border border-slate-200 bg-white px-3 py-2.5 outline-none transition focus:border-sky-400 focus:ring-2 focus:ring-sky-200"
            required
          >
            <option value="">Select a director</option>
            <option
              v-for="person in localStaff"
              :key="`director-create-${person.id}`"
              :value="person.id"
            >
              {{ person.name }}
            </option>
          </select>
        </label>
      </div>

      <div class="rounded-2xl border border-slate-200 bg-white/75 p-4">
        <p class="text-xs font-semibold uppercase tracking-[0.2em] text-slate-500">Classification</p>
        <label class="mt-3 block space-y-2 text-sm text-slate-700">
          <span class="flex items-center justify-between">
            <span class="font-semibold">Genres (multi-select)</span>
            <button
              type="button"
              class="inline-flex h-7 w-7 items-center justify-center rounded-full border border-slate-300 text-base font-semibold text-slate-700 transition hover:bg-slate-100"
              @click="showAddGenre = !showAddGenre"
            >
              +
            </button>
          </span>

          <div v-if="showAddGenre" class="rounded-xl border border-slate-200 bg-slate-50 p-3">
            <p class="text-xs text-slate-600">Add a new genre and refresh options.</p>
            <div class="mt-2 flex gap-2">
              <input
                v-model="newGenreName"
                type="text"
                class="w-full rounded-lg border border-slate-200 bg-white px-3 py-2 text-sm outline-none transition focus:border-sky-400"
                placeholder="Example: Sci-Fi"
              />
              <button
                type="button"
                class="rounded-lg bg-sky-700 px-3 py-2 text-sm font-semibold text-white transition hover:bg-sky-600 disabled:opacity-60"
                :disabled="addingGenre"
                @click="addGenre"
              >
                {{ addingGenre ? 'Adding...' : 'Add' }}
              </button>
            </div>
          </div>

          <select
            v-model="form.genre"
            multiple
            class="h-32 w-full rounded-xl border border-slate-200 bg-white px-3 py-2 outline-none transition focus:border-sky-400 focus:ring-2 focus:ring-sky-200"
          >
            <option v-for="genre in localGenres" :key="`genre-create-${genre.id}`" :value="genre.id">
              {{ genre.name }}
            </option>
          </select>
          <p class="text-xs text-slate-500">Tip: Hold Ctrl (Windows) to choose multiple genres.</p>
        </label>
      </div>

      <div class="rounded-2xl border border-slate-200 bg-white/75 p-4 md:col-span-2">
        <p class="text-xs font-semibold uppercase tracking-[0.2em] text-slate-500">Cast</p>
        <label class="mt-3 block space-y-2 text-sm text-slate-700">
          <span class="flex items-center justify-between">
            <span class="font-semibold">Actors (multi-select)</span>
            <button
              type="button"
              class="inline-flex h-7 w-7 items-center justify-center rounded-full border border-slate-300 text-base font-semibold text-slate-700 transition hover:bg-slate-100"
              @click="showAddActor = !showAddActor"
            >
              +
            </button>
          </span>

          <div v-if="showAddActor" class="rounded-xl border border-slate-200 bg-slate-50 p-3">
            <p class="text-xs text-slate-600">Add a new actor and refresh options.</p>
            <div class="mt-2 flex gap-2">
              <input
                v-model="newActorName"
                type="text"
                class="w-full rounded-lg border border-slate-200 bg-white px-3 py-2 text-sm outline-none transition focus:border-sky-400"
                placeholder="Example: Emma Stone"
              />
              <button
                type="button"
                class="rounded-lg bg-emerald-700 px-3 py-2 text-sm font-semibold text-white transition hover:bg-emerald-600 disabled:opacity-60"
                :disabled="addingActor"
                @click="addActor"
              >
                {{ addingActor ? 'Adding...' : 'Add' }}
              </button>
            </div>
          </div>

          <select
            v-model="form.actors"
            multiple
            class="h-36 w-full rounded-xl border border-slate-200 bg-white px-3 py-2 outline-none transition focus:border-sky-400 focus:ring-2 focus:ring-sky-200"
          >
            <option v-for="person in localStaff" :key="`actor-create-${person.id}`" :value="person.id">
              {{ person.name }}
            </option>
          </select>
          <p class="text-xs text-slate-500">Select every cast member that appears in this movie.</p>
        </label>
      </div>
    </div>

    <p v-if="inlineMessage" class="mt-4 rounded-xl border border-emerald-200 bg-emerald-50 px-3 py-2 text-sm text-emerald-900">
      {{ inlineMessage }}
    </p>
    <p v-if="inlineError" class="mt-4 rounded-xl border border-rose-200 bg-rose-50 px-3 py-2 text-sm text-rose-900">
      {{ inlineError }}
    </p>

    <button
      type="submit"
      class="mt-5 w-full rounded-xl bg-slate-900 px-4 py-2.5 text-sm font-semibold text-white transition hover:bg-slate-700 disabled:cursor-not-allowed disabled:opacity-60"
      :disabled="loading"
    >
      {{ loading ? 'Saving...' : 'Add Movie' }}
    </button>
  </form>
</template>
