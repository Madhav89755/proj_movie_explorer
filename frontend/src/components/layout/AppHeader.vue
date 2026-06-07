<template>
  <header class="relative overflow-hidden rounded-3xl border border-white/30 bg-gradient-to-r from-sky-600 via-cyan-500 to-emerald-500 p-6 text-white shadow-xl md:p-8">
    <div class="absolute -right-6 -top-6 h-24 w-24 rounded-full bg-white/20 blur-2xl" />
    <div class="absolute -left-8 bottom-0 h-20 w-20 rounded-full bg-cyan-200/40 blur-2xl" />

    <div class="relative flex flex-col gap-4 md:flex-row md:items-end md:justify-between">
      <div>
        <p class="text-xs font-semibold uppercase tracking-[0.24em] text-cyan-100">Movie Explorer</p>
        <h1 class="mt-2 text-3xl font-semibold leading-tight md:text-4xl">
          Discover films, casts, and storytellers
        </h1>
      </div>
      <nav class="flex flex-wrap items-center gap-3 text-sm font-semibold">
        <RouterLink
          to="/"
          class="rounded-full border border-white/45 bg-white/15 px-4 py-2 transition hover:bg-white/25"
        >
          Movies
        </RouterLink>
      </nav>
    </div>
  </header>
</template>
