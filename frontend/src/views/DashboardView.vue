<script setup>
import { onMounted, ref } from 'vue'
import { api } from '../api/client'

const stats = ref(null)
const err = ref('')

onMounted(async () => {
  try {
    const { data } = await api.get('/api/dashboard/stats/')
    stats.value = data
  } catch (e) {
    err.value = e.response?.data?.detail || e.message
  }
})

const labels = {
  applied: 'Applied',
  interview: 'Interview',
  offer: 'Offer',
  rejected: 'Rejected',
}
</script>

<template>
  <div>
    <div class="mb-6 flex items-center justify-between">
      <h1 class="text-3xl font-semibold tracking-tight text-white">Dashboard</h1>
      <span class="rounded-full border border-indigo-300/30 bg-indigo-500/10 px-3 py-1 text-xs font-medium uppercase tracking-wide text-indigo-200">
        Overview
      </span>
    </div>
    <p v-if="err" class="mb-4 rounded-lg border border-red-400/30 bg-red-500/10 px-4 py-3 text-red-200">
      {{ err }}
    </p>
    <div v-if="stats" class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
      <div class="rounded-2xl border border-white/10 bg-white/5 p-5 shadow-xl shadow-black/20 backdrop-blur">
        <p class="text-sm text-slate-300">Total applications</p>
        <p class="text-3xl font-semibold text-white">{{ stats.total }}</p>
      </div>
      <div
        v-for="(count, key) in stats.by_status"
        :key="key"
        class="rounded-2xl border border-white/10 bg-white/5 p-5 shadow-xl shadow-black/20 backdrop-blur"
      >
        <p class="text-sm text-slate-300">{{ labels[key] || key }}</p>
        <p class="text-3xl font-semibold text-white">{{ count }}</p>
      </div>
    </div>
    <p v-else-if="!err" class="text-slate-400">Loading dashboard…</p>
  </div>
</template>
