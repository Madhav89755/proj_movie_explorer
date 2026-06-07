<script setup>
import { computed, ref } from 'vue'

const props = defineProps({
  title: {
    type: String,
    required: true,
  },
  fieldLabel: {
    type: String,
    required: true,
  },
  placeholder: {
    type: String,
    default: '',
  },
  buttonText: {
    type: String,
    default: 'Add',
  },
  description: {
    type: String,
    default: '',
  },
  tone: {
    type: String,
    default: 'sky',
  },
  loading: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(['submit'])
const name = ref('')

const toneClassMap = {
  sky: {
    card: 'border-sky-200/70 bg-white/85',
    band: 'from-sky-500/15 to-cyan-400/10',
    button: 'bg-sky-700 hover:bg-sky-600',
  },
  emerald: {
    card: 'border-emerald-200/70 bg-white/85',
    band: 'from-emerald-500/15 to-lime-400/10',
    button: 'bg-emerald-700 hover:bg-emerald-600',
  },
}

const toneClasses = computed(() => toneClassMap[props.tone] || toneClassMap.sky)

function onSubmit() {
  const trimmed = name.value.trim()
  if (!trimmed) {
    return
  }

  emit('submit', trimmed)
  name.value = ''
}
</script>

<template>
  <form
    class="relative overflow-hidden rounded-2xl border p-5 shadow-sm backdrop-blur"
    :class="toneClasses.card"
    @submit.prevent="onSubmit"
  >
    <div class="absolute inset-x-0 top-0 h-12 bg-gradient-to-r" :class="toneClasses.band" />

    <div class="relative">
      <h3 class="text-lg font-semibold text-slate-900">{{ title }}</h3>
      <p v-if="description" class="mt-1 text-sm text-slate-600">{{ description }}</p>
    </div>

    <label class="relative mt-4 block space-y-2 text-sm text-slate-700">
      <span class="font-semibold">{{ fieldLabel }}</span>
      <input
        v-model="name"
        type="text"
        class="w-full rounded-xl border border-slate-200 bg-white px-3 py-2.5 outline-none transition focus:border-sky-400 focus:ring-2 focus:ring-sky-200"
        :placeholder="placeholder"
      />
    </label>

    <button
      type="submit"
      class="mt-4 w-full rounded-xl px-4 py-2.5 text-sm font-semibold text-white transition disabled:cursor-not-allowed disabled:opacity-60"
      :class="toneClasses.button"
      :disabled="loading"
    >
      {{ loading ? 'Saving...' : buttonText }}
    </button>
  </form>
</template>
