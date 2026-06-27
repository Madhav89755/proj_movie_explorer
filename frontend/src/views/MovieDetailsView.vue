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

const ratings=[{
  "id": 1,
  "ratings": 7,
  "comment": "Large stir fry pan with non-stick surface."
}, {
  "id": 2,
  "ratings": 3,
  "comment": "Silicone oven mitts designed for safe cooking and baking."
}, {
  "id": 3,
  "ratings": 7,
  "comment": "A mix of strawberries, blueberries, and raspberries, great for smoothies or desserts."
}, {
  "id": 4,
  "ratings": 7,
  "comment": "Compact yoga mat that folds for easy storage and transport."
}, {
  "id": 5,
  "ratings": 5,
  "comment": "Durable tarp for outdoor camping and protection."
}, {
  "id": 6,
  "ratings": 3,
  "comment": "Hanging bird feeder for backyard birds."
}, {
  "id": 7,
  "ratings": 9,
  "comment": "Pancake mix infused with seasonal pumpkin spice flavor."
}, {
  "id": 8,
  "ratings": 8,
  "comment": "Microwaveable heat pad for soothing muscle aches."
}, {
  "id": 9,
  "ratings": 1,
  "comment": "Convenient electric screwdriver for DIY projects at home."
}, {
  "id": 10,
  "ratings": 3,
  "comment": "A hearty vegetable curry for a quick and satisfying meal."
}, {
  "id": 11,
  "ratings": 5,
  "comment": "Customizable window cover for light control and privacy."
}, {
  "id": 12,
  "ratings": 1,
  "comment": "Eco-friendly bamboo cutting board for food prep."
}, {
  "id": 13,
  "ratings": 7,
  "comment": "Crunchy granola made with organic oats"
}, {
  "id": 14,
  "ratings": 9,
  "comment": "Crispy sweet potato bites, delicious as a side or snack."
}, {
  "id": 15,
  "ratings": 2,
  "comment": "Stylish wall art to enhance home decor."
}, {
  "id": 16,
  "ratings": 1,
  "comment": "Crunchy granola bars made with almond butter, oats, and honey, perfect for on-the-go snacking."
}, {
  "id": 17,
  "ratings": 1,
  "comment": "Artichoke hearts marinated in herbs and oil."
}, {
  "id": 18,
  "ratings": 8,
  "comment": "Stream music from your device to any speaker wirelessly."
}, {
  "id": 19,
  "ratings": 6,
  "comment": "Soft blanket that provides warmth with adjustable settings."
}, {
  "id": 20,
  "ratings": 6,
  "comment": "Elevated planter box for growing herbs or small plants easily."
}, {
  "id": 21,
  "ratings": 1,
  "comment": "Fast and convenient air pump for inflating toys and furniture."
}, {
  "id": 22,
  "ratings": 3,
  "comment": "Absorbent training pads for puppies and kittens."
}, {
  "id": 23,
  "ratings": 5,
  "comment": "A comforting soup filled with chicken and noodles in broth."
}, {
  "id": 24,
  "ratings": 2,
  "comment": "Indoor putting green for practicing your putting skills."
}, {
  "id": 25,
  "ratings": 8,
  "comment": "Durable toy designed for heavy chewers."
}, {
  "id": 26,
  "ratings": 4,
  "comment": "Savory sardines packed in olive oil."
}, {
  "id": 27,
  "ratings": 1,
  "comment": "Plant-based protein powder for post-workout recovery."
}, {
  "id": 28,
  "ratings": 6,
  "comment": "High-performance compression tights designed for optimal support and comfort."
}, {
  "id": 29,
  "ratings": 10,
  "comment": "Homemade ice cream maker for delicious desserts."
}, {
  "id": 30,
  "ratings": 4,
  "comment": "Comfortable pet bed for small to medium-sized dogs."
}, {
  "id": 31,
  "ratings": 10,
  "comment": "Juicy meatballs made with a blend of beef and pork, seasoned with Italian herbs."
}, {
  "id": 32,
  "ratings": 6,
  "comment": "Creamy peach-flavored yogurt with real fruit."
}, {
  "id": 33,
  "ratings": 5,
  "comment": "Compact jump starter for emergency vehicle starts."
}, {
  "id": 34,
  "ratings": 10,
  "comment": "Training tool for reinforcing commands and behavior in dogs."
}, {
  "id": 35,
  "ratings": 8,
  "comment": "Durable cover to protect your grill from the elements."
}, {
  "id": 36,
  "ratings": 9,
  "comment": "A sweet and tangy dressing made with figs and balsamic vinegar, great on salads."
}, {
  "id": 37,
  "ratings": 1,
  "comment": "Premium olive oil infused with herbs for enhanced flavor."
}, {
  "id": 38,
  "ratings": 10,
  "comment": "Compact towels that expand when wet, ideal for travel."
}, {
  "id": 39,
  "ratings": 3,
  "comment": "Ready-to-bake cookie dough packed with chocolate chips."
}, {
  "id": 40,
  "ratings": 7,
  "comment": "Powerful blender for smoothies and soups."
}, {
  "id": 41,
  "ratings": 5,
  "comment": "Eco-friendly bags for picking up after your pet."
}, {
  "id": 42,
  "ratings": 8,
  "comment": "Rechargeable electric toothbrush with smart timer."
}, {
  "id": 43,
  "ratings": 10,
  "comment": "Gentle brush for removing loose fur from pets."
}, {
  "id": 44,
  "ratings": 5,
  "comment": "Frozen green peas, a great addition to meals."
}, {
  "id": 45,
  "ratings": 3,
  "comment": "Fresh sushi rolls filled with a variety of vegetables."
}, {
  "id": 46,
  "ratings": 8,
  "comment": "Rich and creamy smoked Gouda cheese perfect for snacking."
}, {
  "id": 47,
  "ratings": 8,
  "comment": "Retro-style graphic tee with a soft wash for a vintage feel."
}, {
  "id": 48,
  "ratings": 10,
  "comment": "Pulled jackfruit in a smoky BBQ sauce for a tasty vegan dish."
}, {
  "id": 49,
  "ratings": 5,
  "comment": "Deliciously rich brownies made with almond flour."
}, {
  "id": 50,
  "ratings": 2,
  "comment": "A blend of spices perfect for seasoning steak."
}]


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
          <PillBadge tone="amber">Overall Rating {{ movie.movie_overall_rating }}</PillBadge>
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


        
        <section class="space-y-3 rounded-2xl border border-slate-200 bg-slate-50/70 p-5 md:col-span-2">
          <h3 class="text-lg font-semibold text-slate-900">Movie Ratings</h3>
          <div v-if="ratings.length" class="sm:grid sm:gap-2 sm:grid-cols-2">
            <div v-for="rate in ratings" :key="rate.id" class="bg-blue-50 p-2">
              {{rate.comment}} - {{rate.ratings}}
            </div>
          </div>
          <p v-else class="text-slate-600">No Ratings available.</p>
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
