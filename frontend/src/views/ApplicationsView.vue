<script setup>
import { onMounted, ref, watch } from 'vue'
import { api } from '../api/client'

const items = ref([])
const err = ref('')
const loading = ref(false)
const statusFilter = ref('')
const search = ref('')

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
      <h1 class="text-2xl font-semibold text-white">Applications</h1>
      <RouterLink
        to="/applications/new"
        class="rounded bg-indigo-600 px-4 py-2 text-sm font-medium text-white hover:bg-indigo-500"
      >
        Add
      </RouterLink>
    </div>

    <div class="mb-4 flex flex-wrap gap-3">
      <input
        v-model="search"
        type="search"
        placeholder="Company"
        class="rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm text-white placeholder:text-slate-500"
      />
      <select
        v-model="statusFilter"
        class="rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm text-white"
      >
        <option value="">All</option>
        <option value="applied">Applied</option>
        <option value="interview">Interview</option>
        <option value="offer">Offer</option>
        <option value="rejected">Rejected</option>
      </select>
    </div>

    <p v-if="err" class="mb-4 text-red-400">{{ err }}</p>

    <div class="overflow-x-auto rounded-lg border border-slate-800">
      <table class="w-full min-w-[640px] text-left text-sm">
        <thead class="border-b border-slate-800 bg-slate-900 text-slate-400">
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
            class="border-b border-slate-800 hover:bg-slate-900/50"
          >
            <td class="px-4 py-3 text-white">{{ row.company_name }}</td>
            <td class="px-4 py-3">{{ row.position }}</td>
            <td class="px-4 py-3 text-slate-400">{{ row.date_applied }}</td>
            <td class="px-4 py-3 capitalize">{{ row.status }}</td>
            <td class="px-4 py-3 text-right">
              <RouterLink :to="`/applications/${row.id}`" class="mr-2 text-indigo-400 hover:text-indigo-300">
                Edit
              </RouterLink>
              <button type="button" class="text-red-400 hover:text-red-300" @click="remove(row.id)">
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
