import { defineStore } from 'pinia'
import axios from 'axios'

const baseURL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    access: localStorage.getItem('access') || '',
    refresh: localStorage.getItem('refresh') || '',
    email: localStorage.getItem('email') || '',
  }),
  getters: {
    isLoggedIn: (s) => Boolean(s.access),
  },
  actions: {
    setTokens(access, refresh) {
      this.access = access || ''
      this.refresh = refresh || ''
      if (access) localStorage.setItem('access', access)
      else localStorage.removeItem('access')
      if (refresh) localStorage.setItem('refresh', refresh)
      else localStorage.removeItem('refresh')
    },
    setEmail(email) {
      this.email = email || ''
      if (email) localStorage.setItem('email', email)
      else localStorage.removeItem('email')
    },
    async login(email, password) {
      const { data } = await axios.post(`${baseURL}/api/auth/login/`, { email, password })
      this.setTokens(data.access, data.refresh)
      this.setEmail(email)
    },
    async register(email, password) {
      await axios.post(`${baseURL}/api/auth/register/`, { email, password })
    },
    async logout() {
      try {
        if (this.refresh) {
          await axios.post(`${baseURL}/api/auth/logout/`, { refresh: this.refresh })
        }
      } catch {
        /* still clear local session */
      } finally {
        this.setTokens('', '')
        this.setEmail('')
      }
    },
  },
})
