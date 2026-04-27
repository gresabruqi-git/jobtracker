<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const name = ref('')
const email = ref('')
const password = ref('')
const err = ref('')
const loading = ref(false)

const auth = useAuthStore()
const router = useRouter()

async function submit() {
  err.value = ''
  loading.value = true
  try {
    await auth.register(email.value, password.value)
    await auth.login(email.value, password.value)
    router.push('/dashboard')
  } catch (e) {
    err.value =
      e.response?.data?.email?.[0] ||
      e.response?.data?.detail ||
      (typeof e.response?.data === 'object'
        ? JSON.stringify(e.response.data)
        : e.message)
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="mx-auto max-w-md">
    <h1 class="mb-2 text-3xl font-semibold tracking-tight text-white">Create your account</h1>
    <p class="mb-6 text-sm text-slate-300">Start organizing your job applications in one place.</p>
    <form class="space-y-4 rounded-2xl border border-white/10 bg-white/5 p-6 shadow-2xl shadow-black/25 backdrop-blur" @submit.prevent="submit">
      <div>
        <label class="mb-1 block text-sm text-slate-300" for="name">Name (optional)</label>
        <input
          id="name"
          v-model="name"
          type="text"
          autocomplete="name"
          class="w-full rounded-lg border border-white/15 bg-slate-950/70 px-3 py-2 text-white outline-none transition focus:border-indigo-300/60 focus:ring-2 focus:ring-indigo-400/40"
        />
      </div>
      <div>
        <label class="mb-1 block text-sm text-slate-300" for="email">Email</label>
        <input
          id="email"
          v-model="email"
          type="email"
          required
          autocomplete="email"
          class="w-full rounded-lg border border-white/15 bg-slate-950/70 px-3 py-2 text-white outline-none transition focus:border-indigo-300/60 focus:ring-2 focus:ring-indigo-400/40"
        />
      </div>
      <div>
        <label class="mb-1 block text-sm text-slate-300" for="password">Password (min 8)</label>
        <input
          id="password"
          v-model="password"
          type="password"
          required
          minlength="8"
          autocomplete="new-password"
          class="w-full rounded-lg border border-white/15 bg-slate-950/70 px-3 py-2 text-white outline-none transition focus:border-indigo-300/60 focus:ring-2 focus:ring-indigo-400/40"
        />
      </div>
      <p v-if="err" class="rounded-lg border border-red-400/30 bg-red-500/10 px-4 py-3 text-sm text-red-200">{{ err }}</p>
      <button
        type="submit"
        :disabled="loading"
        class="w-full rounded-md bg-indigo-600 py-2 font-medium text-white shadow-lg shadow-indigo-900/40 transition hover:-translate-y-0.5 hover:bg-indigo-500 disabled:opacity-50"
      >
        {{ loading ? '…' : 'Create account' }}
      </button>
    </form>
  </div>
</template>
