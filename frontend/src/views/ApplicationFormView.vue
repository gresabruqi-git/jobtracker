<script setup>
import { computed, onMounted, ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import { api } from '../api/client'

const props = defineProps({
  id: { type: String, default: '' },
})

const router = useRouter()
const isEdit = computed(() => Boolean(props.id))

const form = ref({
  company_name: '',
  position: '',
  date_applied: '',
  status: 'applied',
  notes: '',
})
const err = ref('')
const loading = ref(false)

async function load() {
  if (!isEdit.value) return
  err.value = ''
  try {
    const { data } = await api.get(`/api/applications/${props.id}/`)
    form.value = {
      company_name: data.company_name,
      position: data.position,
      date_applied: data.date_applied,
      status: data.status,
      notes: data.notes || '',
    }
  } catch (e) {
    err.value = e.response?.data?.detail || e.message
  }
}

onMounted(load)
watch(() => props.id, load)

async function save() {
  err.value = ''
  loading.value = true
  try {
    if (isEdit.value) {
      await api.put(`/api/applications/${props.id}/`, form.value)
    } else {
      await api.post('/api/applications/', form.value)
    }
    router.push('/applications')
  } catch (e) {
    err.value =
      typeof e.response?.data === 'object'
        ? JSON.stringify(e.response.data)
        : e.message
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="mx-auto max-w-lg">
    <h1 class="mb-6 text-2xl font-semibold text-white">
      {{ isEdit ? 'Edit application' : 'New application' }}
    </h1>
    <form class="space-y-4 rounded-lg border border-slate-800 bg-slate-900 p-6" @submit.prevent="save">
      <div>
        <label class="mb-1 block text-sm text-slate-400" for="company">Company</label>
        <input
          id="company"
          v-model="form.company_name"
          required
          class="w-full rounded border border-slate-700 bg-slate-950 px-3 py-2 text-white"
        />
      </div>
      <div>
        <label class="mb-1 block text-sm text-slate-400" for="position">Position</label>
        <input
          id="position"
          v-model="form.position"
          required
          class="w-full rounded border border-slate-700 bg-slate-950 px-3 py-2 text-white"
        />
      </div>
      <div>
        <label class="mb-1 block text-sm text-slate-400" for="date">Date applied</label>
        <input
          id="date"
          v-model="form.date_applied"
          type="date"
          required
          class="w-full rounded border border-slate-700 bg-slate-950 px-3 py-2 text-white"
        />
      </div>
      <div>
        <label class="mb-1 block text-sm text-slate-400" for="status">Status</label>
        <select
          id="status"
          v-model="form.status"
          class="w-full rounded border border-slate-700 bg-slate-950 px-3 py-2 text-white"
        >
          <option value="applied">Applied</option>
          <option value="interview">Interview</option>
          <option value="offer">Offer</option>
          <option value="rejected">Rejected</option>
        </select>
      </div>
      <div>
        <label class="mb-1 block text-sm text-slate-400" for="notes">Notes</label>
        <textarea
          id="notes"
          v-model="form.notes"
          rows="3"
          class="w-full rounded border border-slate-700 bg-slate-950 px-3 py-2 text-white"
        />
      </div>
      <p v-if="err" class="text-sm text-red-400">{{ err }}</p>
      <div class="flex gap-3">
        <button
          type="submit"
          :disabled="loading"
          class="rounded bg-indigo-600 px-4 py-2 font-medium text-white hover:bg-indigo-500 disabled:opacity-50"
        >
          {{ loading ? '…' : 'Save' }}
        </button>
        <RouterLink to="/applications" class="rounded border border-slate-600 px-4 py-2 text-slate-300 hover:bg-slate-800">
          Cancel
        </RouterLink>
      </div>
    </form>
  </div>
</template>
