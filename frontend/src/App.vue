<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useAuthStore } from './stores/auth'
import { useRouter } from 'vue-router'

const auth = useAuthStore()
const router = useRouter()

async function handleLogout() {
  await auth.logout()
  router.push({ name: 'login' })
}
</script>

<template>
  <div class="min-h-screen bg-slate-950 text-slate-100">
    <header class="border-b border-slate-800 bg-slate-900/80">
      <div class="mx-auto flex max-w-5xl flex-wrap items-center justify-between gap-4 px-4 py-3">
        <RouterLink to="/" class="text-lg font-semibold tracking-tight text-white">
          JobTracker
        </RouterLink>
        <nav class="flex flex-wrap items-center gap-3 text-sm">
          <template v-if="auth.isLoggedIn">
            <RouterLink
              class="rounded px-2 py-1 text-slate-300 hover:bg-slate-800 hover:text-white"
              active-class="bg-slate-800 text-white"
              to="/dashboard"
            >
              Dashboard
            </RouterLink>
            <RouterLink
              class="rounded px-2 py-1 text-slate-300 hover:bg-slate-800 hover:text-white"
              active-class="bg-slate-800 text-white"
              to="/applications"
            >
              Applications
            </RouterLink>
            <RouterLink
              class="rounded px-2 py-1 text-slate-300 hover:bg-slate-800 hover:text-white"
              to="/applications/new"
            >
              New
            </RouterLink>
            <span class="text-slate-500">{{ auth.email }}</span>
            <button
              type="button"
              class="rounded bg-slate-800 px-3 py-1 text-slate-200 hover:bg-slate-700"
              @click="handleLogout"
            >
              Log out
            </button>
          </template>
          <template v-else>
            <RouterLink class="text-slate-300 hover:text-white" to="/login">Log in</RouterLink>
            <RouterLink
              class="rounded bg-indigo-600 px-3 py-1 text-white hover:bg-indigo-500"
              to="/register"
            >
              Register
            </RouterLink>
          </template>
        </nav>
      </div>
    </header>
    <main class="mx-auto max-w-5xl px-4 py-8">
      <RouterView />
    </main>
  </div>
</template>
