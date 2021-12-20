<template>
   <v-app id="inspire" >
      <v-content>
         <v-container fluid fill-height >
            <v-layout align-center justify-center>
               <v-flex xs12 sm8 md4>
                  <v-tabs class="d-flex justify-center mb-6" grow  color=#C85250>
                     <v-tab>
                        
                           Login
                     </v-tab>
                     <v-tab to='/documentvalidation'>
                        
                           Validate Document
                     </v-tab>
                  </v-tabs>
                  <v-card class="elevation-12">
                     <v-toolbar dark color="#C85250">
                        <v-toolbar-title>Login</v-toolbar-title>
                     </v-toolbar>
                        <v-form @submit.prevent="SubmitForm" v-model="isValid">
                           <v-card-text>
                                 <v-alert
                                 type="error"
                                 v-if="errors"
                                 >{{errors}}</v-alert>
                                 <v-text-field
                                       v-model="email"
                                       prepend-icon="email"
                                       name="email"
                                       label="Email"
                                       type="email"
                                       class=""
                                       :rules="emailValidation"
                                 ></v-text-field>
                                 <v-text-field
                                       v-model="password"
                                       id="password"
                                       prepend-icon="lock"
                                       name="password"
                                       label="Password"
                                       type="password"
                                       :rules="passwordValidation"
                                    ></v-text-field>
                           </v-card-text>
                           <v-card-actions>
                              <v-btn dark text color="#C85250" to="/register">Don't Have Account ?</v-btn>
                              <v-spacer></v-spacer>
                              <v-btn dark color="#C85250" type="submit">
                              <v-icon left>lock</v-icon>Login</v-btn>
                           </v-card-actions>
                        </v-form>
                  </v-card>
               </v-flex>
            </v-layout>
         </v-container>
      </v-content>
   </v-app>
</template>

<script>
import axios from 'axios'
import certificate from '/build/contracts/digitalCertificate.json'
import Web3 from 'web3'

export default {
   name: 'Login',
   props: {
      source: String,
   },

   data(){
      return{
         email:'',
         password:'',
         errors: '',
         emailValidation:[
               v => !!v || 'E-mail is required',
               v => /.+@.+/.test(v) || 'E-mail must be valid',
         ],
         passwordValidation:[
               v => !!v || 'Password is required',
         ],
         isValid:false,
      }
   },

   methods:{
      testStorage(){
         localStorage.setItem('name', this.email)
         console.log(localStorage.getItem('name'))
      },
      async SubmitForm(){
         this.$store.commit('setIsLoading',true)
         if (window.ethereum) {
            window.web3 = new Web3(window.ethereum)
            await window.ethereum.enable()
         }
         else if (window.web3) {
            window.web3 = new Web3(window.web3.currentProvider)
         }
         else {
            window.alert('Non-Ethereum browser detected. You should consider trying MetaMask!')
         }

         web3 = window.web3
         // const accounts = await web3.eth.getAccounts()
         const networkId = await web3.eth.net.getId()
         const networkData = certificate.networks[networkId]
         if(networkData) {
            const abi = certificate.abi
            const address = networkData.address
            // console.log(accounts.toString())
            const contract = new web3.eth.Contract(abi,address)
            const getCertificate = await contract.methods.certificates(this.email).call()
            localStorage.setItem('cert_url',getCertificate.cert_url)
            localStorage.setItem('key_url',getCertificate.key_url)
         } else {
            window.alert('Smart contract not deployed to detected network.')
         }

         axios.defaults.headers.common['Authorization'] = ''
         localStorage.removeItem('token')

         const formData={
            email:this.email,
            password:this.password
         }
         axios
         .post("http://localhost:8000/api/simple", formData)
         .then(Response =>{
               const token = Response.data.token
               localStorage.setItem('simple_token',token)
            })

         await axios
        .post("http://localhost:8000/api/login", formData)
        .then(Response =>{
          const token = Response.data.jwt
          this.$store.commit('setToken', token)
          
          axios.defaults.headers.common['Authorization'] = 'Token'+token
          localStorage.setItem('token',token)
          const formData={
                jwt:localStorage.getItem('token'),
            }

            axios
            .post("http://localhost:8000/api/account", formData)
            .then(response=>{
               this.$store.commit('setUser',response.data)
               localStorage.setItem('id',response.data.id)
               localStorage.setItem('first_name',response.data.first_name)
               localStorage.setItem('last_name',response.data.last_name)
               localStorage.setItem('email',response.data.email)
               localStorage.setItem('address',response.data.address)
               localStorage.setItem('organization',response.data.organization)
               localStorage.setItem('is_verified',response.data.is_verified)
               
               this.$router.push('/dashboard')
               
            })
         this.$store.commit('setIsLoading',false)
         //  console.log(this.$store.state)
        })
        .catch(error=>{
            if (error.response){
              for (const property in error.response.data){
                this.errors=`${error.response.data[property]}`
              }
            }else if(error.message){
              this.errors='Something went wrong. Please try again !'
            }
          })
         // localStorage.setItem('token',token)
      }
   }
};
</script>

<style>
   
</style>
