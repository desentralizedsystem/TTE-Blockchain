<template>
  <v-app>
    <Navbar v-if="!checkingPage()" @toggle="toggleSidebar = !toggleSidebar"/>
    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading }">
            <div class="lds-dual-ring"></div>
        </div>
    <v-content class="ma-4">
      <router-view></router-view>
    </v-content>
    <Footer/>
  </v-app>
</template>

<script>
import Navbar from '@/components/Navbar'
import Footer from '@/components/Footer'

import axios from 'axios';

axios.defaults.baseURL = 'http://localhost:8000'

export default {
  name: 'App',
  components:{
    Navbar,
    Footer
  },
  data() {
    return {
      toggleSidebar: false 
    };
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
  },
  methods: {
    checkingPage() {
      return this.$route.name == "login" || this.$route.name == "register"||this.$route.name =="documentvalidation";
    }
  },
  
}
</script>

<style lang="scss">


</style>