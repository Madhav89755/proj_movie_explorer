<script setup>
import { computed, reactive, watch } from 'vue'

const props = defineProps({
  genres: {
    type: Array,
    default: () => [],
  },
  staff: {
    type: Array,
    default: () => [],
  },
  modelValue: {
    type: Object,
    required: true,
  },
})

const emit = defineEmits(['update:modelValue', 'apply', 'reset'])

const localFilters = reactive({
  title: props.modelValue.title || '',
  genre_id: props.modelValue.genre_id || '',
  actor_id: props.modelValue.actor_id || '',
  director_id: props.modelValue.director_id || '',
  ordering: props.modelValue.ordering || '-release_date',
  overall_rating : props.modelValue.overall_rating || ''
})

watch(
  () => props.modelValue,
  (value) => {
    localFilters.title = value.title || ''
    localFilters.genre_id = value.genre_id || ''
    localFilters.actor_id = value.actor_id || ''
    localFilters.director_id = value.director_id || ''
    localFilters.ordering = value.ordering || '-release_date'
    localFilters.overall_rating = value.overall_rating || ''
  },
)

const availableDirectors = computed(() => props.staff)
const availableActors = computed(() => props.staff)

function submitFilters() {
  emit('update:modelValue', { ...localFilters })
  emit('apply')
}

function resetFilters() {
  const empty = {
    title: '',
    genre_id: '',
    actor_id: '',
    director_id: '',
    ordering: '-release_date',  
    overall_rating:''
  }

  emit('update:modelValue', empty)
  emit('reset')
}
</script>

<template>
  <form
    class="grid gap-4 rounded-2xl border border-white/40 bg-white/80 p-5 shadow-sm backdrop-blur md:grid-cols-2 xl:grid-cols-6"
    @submit.prevent="submitFilters"
  >
    <label class="space-y-2 text-sm text-slate-700">
      <span class="font-semibold">Search by title</span>
      <input
        v-model="localFilters.title"
        type="text"
        class="w-full rounded-xl border border-slate-200 bg-white px-3 py-2 outline-none ring-0 transition focus:border-sky-400"
        placeholder="Example: Hidden Horizon"
      />
    </label>

    <label class="space-y-2 text-sm text-slate-700">
      <span class="font-semibold">Search by Rating</span>
      <input
        v-model="localFilters.overall_rating"
        type="text"
        class="w-full rounded-xl border border-slate-200 bg-white px-3 py-2 outline-none ring-0 transition focus:border-sky-400"
        placeholder="Example: 5"
      />
    </label>

    <label class="space-y-2 text-sm text-slate-700">
      <span class="font-semibold">Genre</span>
      <select
        v-model="localFilters.genre_id"
        class="w-full rounded-xl border border-slate-200 bg-white px-3 py-2 outline-none transition focus:border-sky-400"
      >
        <option value="">All genres</option>
        <option v-for="genre in props.genres" :key="genre.id" :value="genre.id">{{ genre.name }}</option>
      </select>
    </label>

    <label class="space-y-2 text-sm text-slate-700">
      <span class="font-semibold">Actor</span>
      <select
        v-model="localFilters.actor_id"
        class="w-full rounded-xl border border-slate-200 bg-white px-3 py-2 outline-none transition focus:border-sky-400"
      >
        <option value="">All actors</option>
        <option v-for="person in availableActors" :key="`actor-${person.id}`" :value="person.id">
          {{ person.name }}
        </option>
      </select>
    </label>

    <label class="space-y-2 text-sm text-slate-700">
      <span class="font-semibold">Director</span>
      <select
        v-model="localFilters.director_id"
        class="w-full rounded-xl border border-slate-200 bg-white px-3 py-2 outline-none transition focus:border-sky-400"
      >
        <option value="">All directors</option>
        <option
          v-for="person in availableDirectors"
          :key="`director-${person.id}`"
          :value="person.id"
        >
          {{ person.name }}
        </option>
      </select>
    </label>

    <label class="space-y-2 text-sm text-slate-700">
      <span class="font-semibold">Sort by</span>
      <select
        v-model="localFilters.ordering"
        class="w-full rounded-xl border border-slate-200 bg-white px-3 py-2 outline-none transition focus:border-sky-400"
      >
        <option value="-release_date">Newest release</option>
        <option value="release_date">Oldest release</option>
        <option value="title">Title A to Z</option>
        <option value="-title">Title Z to A</option>
      </select>
    </label>

    <div class="flex items-end gap-2 xl:justify-end">
      <button
        type="button"
        class="w-full rounded-xl border border-slate-300 px-4 py-2 text-sm font-semibold text-slate-700 transition hover:bg-slate-100 xl:w-auto"
        @click="resetFilters"
      >
        Reset
      </button>
      <button
        type="submit"
        class="w-full rounded-xl bg-slate-900 px-4 py-2 text-sm font-semibold text-white transition hover:bg-slate-700 xl:w-auto"
      >
        Apply
      </button>
    </div>
  </form>
</template>
