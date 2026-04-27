<script setup>
import { onMounted, ref, watch } from 'vue'
import { api } from '../api/client'

const items = ref([])
const err = ref('')
const loading = ref(false)
const statusFilter = ref('')
const search = ref('')
const statusPillClasses = {
  applied: 'border-sky-300/30 bg-sky-400/10 text-sky-200',
  interview: 'border-amber-300/30 bg-amber-400/10 text-amber-200',
  offer: 'border-emerald-300/30 bg-emerald-400/10 text-emerald-200',
  rejected: 'border-rose-300/30 bg-rose-400/10 text-rose-200',
}

async function load() {
  err.value = ''
  loading.value = true
  try {
    const params = {}
    if (statusFilter.value) params.status = statusFilter.value
    if (search.value.trim()) params.search = search.value.trim()
    const { data } = await api.get('/api/applications/', { params })
    items.value = data
  } catch (e) {
    err.value = e.response?.data?.detail || e.message
    items.value = []
  } finally {
    loading.value = false
  }
}

onMounted(load)
watch([statusFilter, search], load)

async function remove(id) {
  if (!confirm('Delete this row?')) return
  err.value = ''
  try {
    await api.delete(`/api/applications/${id}/`)
    await load()
  } catch (e) {
    err.value = e.response?.data?.detail || e.message
  }
}
</script>

<template>
  <div>
    <div class="mb-6 flex flex-wrap items-end justify-between gap-4">
      <h1 class="text-3xl font-semibold tracking-tight text-white">Applications</h1>
      <RouterLink
        to="/applications/new"
        class="rounded-md bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-lg shadow-indigo-900/40 transition hover:-translate-y-0.5 hover:bg-indigo-500"
      >
        Add
      </RouterLink>
    </div>

    <div class="mb-4 flex flex-wrap gap-3 rounded-2xl border border-white/10 bg-white/5 p-4 shadow-xl shadow-black/20 backdrop-blur">
      <input
        v-model="search"
        type="search"
        placeholder="Company"
        class="w-full rounded-lg border border-white/15 bg-slate-950/70 px-3 py-2 text-sm text-white placeholder:text-slate-400 outline-none transition focus:border-indigo-300/60 focus:ring-2 focus:ring-indigo-400/40 sm:w-64"
      />
      <select
        v-model="statusFilter"
        class="rounded-lg border border-white/15 bg-slate-950/70 px-3 py-2 text-sm text-white outline-none transition focus:border-indigo-300/60 focus:ring-2 focus:ring-indigo-400/40"
      >
        <option value="">All</option>
        <option value="applied">Applied</option>
        <option value="interview">Interview</option>
        <option value="offer">Offer</option>
        <option value="rejected">Rejected</option>
      </select>
    </div>

    <p v-if="err" class="mb-4 rounded-lg border border-red-400/30 bg-red-500/10 px-4 py-3 text-red-200">{{ err }}</p>

    <div class="overflow-x-auto rounded-2xl border border-white/10 bg-slate-900/40 shadow-2xl shadow-black/30">
      <table class="w-full min-w-[640px] text-left text-sm">
        <thead class="border-b border-white/10 bg-white/5 text-slate-300">
          <tr>
            <th class="px-4 py-3">Company</th>
            <th class="px-4 py-3">Position</th>
            <th class="px-4 py-3">Date</th>
            <th class="px-4 py-3">Status</th>
            <th class="px-4 py-3"></th>
          </tr>
        </thead>
        <tbody>
          <tr v-if="loading">
            <td colspan="5" class="px-4 py-6 text-slate-500">Loading…</td>
          </tr>
          <tr
            v-else
            v-for="row in items"
            :key="row.id"
            class="border-b border-white/10 transition hover:bg-white/5"
          >
            <td class="px-4 py-3 text-white">{{ row.company_name }}</td>
            <td class="px-4 py-3 text-slate-100">{{ row.position }}</td>
            <td class="px-4 py-3 text-slate-400">{{ row.date_applied }}</td>
            <td class="px-4 py-3">
              <span
                class="inline-flex rounded-full border px-2.5 py-1 text-xs font-medium capitalize"
                :class="statusPillClasses[row.status] || 'border-white/20 bg-white/10 text-slate-200'"
              >
                {{ row.status }}
              </span>
            </td>
            <td class="px-4 py-3 text-right">
              <RouterLink :to="`/applications/${row.id}`" class="mr-2 text-indigo-300 hover:text-indigo-200">
                Edit
              </RouterLink>
              <button type="button" class="text-rose-300 hover:text-rose-200" @click="remove(row.id)">
                Delete
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <p v-if="!loading && !err && !items.length" class="mt-4 text-slate-500">
      {{ search.trim() || statusFilter ? 'No matches.' : 'Nothing here yet.' }}
    </p>
  </div>
</template>
