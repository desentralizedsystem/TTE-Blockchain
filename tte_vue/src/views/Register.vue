<template>
   <v-app id="inspire">
      <v-content>
         <v-container fluid fill-height>
            <v-layout align-center justify-center>
               <v-flex xs12 sm8 md4>
                  
                  <v-card class="elevation-12">
                     <v-toolbar dark color="#C85250">
                        <v-toolbar-title>Create an Account</v-toolbar-title>
                     </v-toolbar>
                     <v-form @submit.prevent="SubmitForm" v-model="isValid">
                        <v-card-text>
                              <v-text-field
                                 v-model="first_name"
                                 prepend-icon="person"
                                 name="first_name"
                                 label="First Name"
                                 type="text"
                                 class=""
                                 :rules="firstNameValidation"
                              ></v-text-field>
                              <v-text-field
                                 v-model="last_name"
                                 prepend-icon="person"
                                 name="first_name"
                                 label="Last Name"
                                 type="text"
                                 class=""
                                 :rules="lastNameValidation"
                              ></v-text-field>
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
                                 v-model="address"
                                 prepend-icon="mdi-map-marker"
                                 name="address"
                                 label="Address"
                                 type="text"
                                 class=""
                                 :rules="addressValidation"
                              ></v-text-field>
                              <v-text-field
                                 v-model="organization"
                                 prepend-icon="mdi-office-building-marker"
                                 name="organization"
                                 label="Organization"
                                 type="text"
                                 class=""
                                 :rules="organizationValidation"
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
                              <v-text-field
                                 v-model="confirm_password"
                                 id="confirm_password"
                                 prepend-icon="lock"
                                 name="confirm_password"
                                 label="Confirm Password"
                                 type="password"
                                 :rules="confirmPasswordValidation"
                              ></v-text-field>
                              <div class="notification" v-if="errors.length" style="color:red">
                                 <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                              </div>
                              <!-- <v-btn dark color="#C85250" @click="loadWeb3">
                              <v-icon left>mdi-wallet-plus</v-icon>Connect Metamask Wallet</v-btn> -->
                        </v-card-text>
                        <v-card-actions>
                           <v-btn dark text color="#C85250" to="/">Login</v-btn>
                           <v-spacer></v-spacer>
                           <v-btn  color="#C85250" type="submit" :disabled="!isValid">
                           <v-icon left>lock</v-icon>Sign Up</v-btn>
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
   import swal from 'sweetalert';
   import Web3 from 'web3';

   export default { 
      name: 'Login',
     
      data(){
         return{
            first_name:'',
            last_name:'',
            email:'',
            address:'',
            organization:'',
            password:'',
            confirm_password:'',
            wallet:'',
            errors: [],

            //validation
            firstNameValidation:[
               v => !!v || 'First name is required',
               v => v.length <= 30 || 'Fisrt name must be less than 30 characters',
            ],
            lastNameValidation:[
               v => !!v || 'last name is required',
               v => v.length <= 30 || 'Last name must be less than 30 characters',
            ],
            emailValidation:[
               v => !!v || 'E-mail is required',
               v => /.+@.+/.test(v) || 'E-mail must be valid',
               v => v.length <= 60 || 'E-mail must be less than 60 characters',
            ],
            addressValidation:[
               v => !!v || 'Address is required',
               v => v.length <= 120 || 'Address must be less than 120 characters',
            ],
            organizationValidation:[
               v => !!v || 'Organization is required',
               v => v.length <= 120 || 'Organization must be less than 120 characters',
            ],
            passwordValidation:[
               v => !!v || 'Password is required',
               v => v.length <= 12 || 'Password must be less than 12 characters',
               v => v.length >= 3 || 'Password must more than 3 characters',
            ],
            confirmPasswordValidation:[
               v => !!v || 'Password is required',
               v => v ==  this.password|| 'Password must match',
               v => v.length <= 12 || 'Password must be less than 12 characters',
               v => v.length >= 3 || 'Password must more than 3 characters',
            ],
            isValid:false,

            
            
         }
      },
      props: {
         source: String,
      },
      methods: {
         suksesAlert() {
            swal({
            icon: "success",
            title: "Succesfully",
            text: "Account was created, please log in",
            button: "Confirm",
            })
            .then((value) => {
               this.$router.push('/')
            });
         },
         async loadWeb3() {
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
         },
         SubmitForm(){
            const formData = {
               first_name: this.first_name,
               last_name: this.last_name,
               email: this.email,
               address: this.address,
               organization: this.organization,
               password: this.password,
               // wallet: this.wallet,
            }
            axios.post("http://localhost:8000/api/register", formData)
            .then(response => {
               this.suksesAlert()
               // this.$router.push('/')
            })
            .catch(error => {
               if (error.response) {
                  for (const property in error.response.data) {
                     this.errors.push(`${property}: ${error.response.data[property]}`)
                  }
               } else if (error.message) {
                  this.errors.push('Something went wrong. Please try again!')
               }
            });
            
         }
         
      }
   };
</script>

<style></style>
