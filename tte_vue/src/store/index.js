import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isLoading: false,
    isAuthenticated: false,
    token: '',
    account: {
      id: 0,
      email: '',
      first_name:'',
      last_name:'',
      address:'',
      organization:'',
    },
      contractInstance: null
  },

  mutations: {
    initializeStore(state) {
      
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
        state.account.email = localStorage.getItem('email')
        state.account.id = localStorage.getItem('id')
        state.account.first_name = localStorage.getItem('first_name')
        state.account.last_name = localStorage.getItem('last_name')
        state.account.address = localStorage.getItem('address')
        state.account.organization = localStorage.getItem('organization')
      } else {
        state.token = ''
        state.isAuthenticated = false
        state.account.id = 0
        state.account.email = ''
        state.account.first_name = ''
        state.account.last_name = ''
        state.account.address = ''
        state.account.organization = ''
      }
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
    },
    setUser(state, account) {
      state.account.first_name = account.first_name
      state.account.last_name = account.last_name
      state.account.email = account.email
      state.account.address = account.address
      state.account.organization = account.organization
      state.account.id = account.id
    },
  },
  actions: {
  },
  modules: {
  }
})
