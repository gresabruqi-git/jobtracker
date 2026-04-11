<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const email = ref('')
const password = ref('')
const err = ref('')
const loading = ref(false)

const auth = useAuthStore()
const route = useRoute()
const router = useRouter()

async function submit() {
  err.value = ''
  loading.value = true
  try {
    await auth.login(email.value, password.value)
    const redirect = route.query.redirect || '/dashboard'
    router.push(typeof redirect === 'string' ? redirect : '/dashboard')
  } catch (e) {
    err.value =
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
    <h1 class="mb-6 text-2xl font-semibold text-white">Log in</h1>
    <form class="space-y-4 rounded-lg border border-slate-800 bg-slate-900 p-6" @submit.prevent="submit">
      <div>
        <label class="mb-1 block text-sm text-slate-400" for="email">Email</label>
        <input
          id="email"
          v-model="email"
          type="email"
          required
          autocomplete="email"
          class="w-full rounded border border-slate-700 bg-slate-950 px-3 py-2 text-white outline-none ring-indigo-500 focus:ring-2"
        />
      </div>
      <div>
        <label class="mb-1 block text-sm text-slate-400" for="password">Password</label>
        <input
          id="password"
          v-model="password"
          type="password"
          required
          autocomplete="current-password"
          class="w-full rounded border border-slate-700 bg-slate-950 px-3 py-2 text-white outline-none ring-indigo-500 focus:ring-2"
        />
      </div>
      <p v-if="err" class="text-sm text-red-400">{{ err }}</p>
      <button
        type="submit"
        :disabled="loading"
        class="w-full rounded bg-indigo-600 py-2 font-medium text-white hover:bg-indigo-500 disabled:opacity-50"
      >
        {{ loading ? '…' : 'Log in' }}
      </button>
    </form>
  </div>
</template>
