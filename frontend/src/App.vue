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
  <div class="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-indigo-950 text-slate-100">
    <header class="sticky top-0 z-20 border-b border-white/10 bg-slate-900/70 backdrop-blur-xl">
      <div class="mx-auto flex max-w-5xl flex-wrap items-center justify-between gap-4 px-4 py-3">
        <RouterLink
          to="/"
          class="bg-gradient-to-r from-indigo-300 to-cyan-300 bg-clip-text text-lg font-semibold tracking-tight text-transparent"
        >
          JobTracker
        </RouterLink>
        <nav class="flex flex-wrap items-center gap-3 text-sm">
          <template v-if="auth.isLoggedIn">
            <RouterLink
              class="rounded-md px-3 py-1.5 text-slate-300 transition hover:bg-white/10 hover:text-white"
              active-class="bg-white/15 text-white"
              to="/dashboard"
            >
              Dashboard
            </RouterLink>
            <RouterLink
              class="rounded-md px-3 py-1.5 text-slate-300 transition hover:bg-white/10 hover:text-white"
              active-class="bg-white/15 text-white"
              to="/applications"
            >
              Applications
            </RouterLink>
            <RouterLink
              class="rounded-md px-3 py-1.5 text-slate-300 transition hover:bg-white/10 hover:text-white"
              to="/applications/new"
            >
              New
            </RouterLink>
            <span class="max-w-48 truncate text-slate-400">{{ auth.email }}</span>
            <button
              type="button"
              class="rounded-md border border-white/10 bg-white/5 px-3 py-1.5 text-slate-200 transition hover:bg-white/10"
              @click="handleLogout"
            >
              Log out
            </button>
          </template>
          <template v-else>
            <RouterLink class="rounded-md px-3 py-1.5 text-slate-300 transition hover:bg-white/10 hover:text-white" to="/login">
              Log in
            </RouterLink>
            <RouterLink
              class="rounded-md bg-indigo-600 px-3 py-1.5 font-medium text-white shadow-lg shadow-indigo-900/40 transition hover:-translate-y-0.5 hover:bg-indigo-500"
              to="/register"
            >
              Register
            </RouterLink>
          </template>
        </nav>
      </div>
    </header>
    <main class="mx-auto max-w-5xl px-4 py-10">
      <RouterView />
    </main>
  </div>
</template>
