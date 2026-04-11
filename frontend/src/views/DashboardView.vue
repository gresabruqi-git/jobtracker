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
    <h1 class="mb-6 text-2xl font-semibold text-white">Dashboard</h1>
    <p v-if="err" class="mb-4 text-red-400">{{ err }}</p>
    <div v-if="stats" class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
      <div class="rounded-lg border border-slate-800 bg-slate-900 p-4">
        <p class="text-sm text-slate-400">Total applications</p>
        <p class="text-3xl font-semibold text-white">{{ stats.total }}</p>
      </div>
      <div
        v-for="(count, key) in stats.by_status"
        :key="key"
        class="rounded-lg border border-slate-800 bg-slate-900 p-4"
      >
        <p class="text-sm text-slate-400">{{ labels[key] || key }}</p>
        <p class="text-3xl font-semibold text-white">{{ count }}</p>
      </div>
    </div>
    <p v-else-if="!err" class="text-slate-500">Loading…</p>
  </div>
</template>
