<template>
    <nav>
        <v-app-bar color="#c23f3d" dark app>
            <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
            <v-toolbar-title class="text-uppercase">
                <span class="font-weight-light">Digital</span>
                <span> Signer</span>
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <!-- <v-btn text @click="$router.push('/documents')"> -->
            <!-- <v-btn text @click="test()">
                <span>Log out</span>
                <v-icon>notifications</v-icon>
            </v-btn> -->
            <v-btn text @click="logout()">
                <span>Log out</span>
                <v-icon right>exit_to_app</v-icon>
            </v-btn>
        </v-app-bar>
        <v-navigation-drawer  v-model="drawer" dark app color="#E7625F">
          <v-layout column align-center>
               <v-flex class="mt-5"> 
                    <v-avatar size="100">
                            <img src="../assets/profile.png" alt="">
                    </v-avatar>

                    <p class="white--text subheading mt-1 text-center" >{{account.first_name}} {{account.last_name}}</p>
               </v-flex>
               
               <v-flex class="mt-4 mb-4">
                <!-- <Popup /> -->
               </v-flex>
          </v-layout>
          <v-list flat>
              <v-list-item v-for="link in links"  :key="link.text" router :to="link.route" active-class="border">
                  <v-list-item-action>
                     <v-icon >{{link.icon}}</v-icon>
                  </v-list-item-action>
                  <v-list-item-content >
                      <v-list-item-title >{{link.text}}</v-list-item-title>
                  </v-list-item-content>
              </v-list-item>
          </v-list>
      </v-navigation-drawer>
    </nav>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

export default {
    computed: {
        ...mapState(['account'])
    },
    data :()=>({
        drawer: true,
        nama:'test',
        // userAccount:JSON.parse(localStorage.getItem('account')),
        links:[
            {icon: 'dashboard', text:'Dashboard', route: '/dashboard'},
            {icon: 'account_circle', text:'Profile', route: '/profile'},
            {icon: 'document_scanner', text:'Documents', route: '/documents'},
            {icon: 'drive_file_rename_outline', text:'Signature Requests', route: '/request'}
        ],
        
    }),
    

    methods:{
        async logout(){
            axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
            await axios
                .post("http://localhost:8000/api/logout")
                .then(response => {
                    console.log('logout')
                })
                .catch(error=>{
                    console.log(JSON.stringify(error))
                })
            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('token')
            localStorage.removeItem('id')
            localStorage.removeItem('email')
            localStorage.removeItem('first_name')
            localStorage.removeItem('last_name')
            localStorage.removeItem('address')
            localStorage.removeItem('organization')
            localStorage.removeItem('simple_token')
            localStorage.removeItem('is_verified')
            localStorage.removeItem('pdfjs.history')
            localStorage.removeItem('cert_url')
            localStorage.removeItem('key_url')
            this.$store.commit('removeToken')
            this.$router.push('/')
        },
        test(){
            
            // console.log(this.$store.state)
            console.log(this.$store.state.isAuthenticated)
        },
        // getAccount(){
        //     const formData={
        //         jwt:localStorage.getItem('token'),
        //     }
        //     axios
        //         .post("http://localhost:8000/api/account",formData)
        //         .then(response =>{
        //             console.log(response)
        //         })
        //         .catch(error=>{
        //             console.log(JSON.stringify(error))
        //         })
        // }
    }
}
</script>

<style scoped>
.border {
  border-left: 4px solid #C85250;
}
</style>