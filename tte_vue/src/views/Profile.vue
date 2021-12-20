<template>
  <v-card>
      <v-toolbar
        flat
        color=#C85250
        dark
      >
        <v-toolbar-title>Profile</v-toolbar-title>
      </v-toolbar>
      <v-tabs grow background-color=transparant color=#C85250>
        <v-tab>
          <v-icon left>
            mdi-account
          </v-icon>
          Profile
        </v-tab>
        <v-tab>
          <v-icon left>
            mdi-lock
          </v-icon>
          Password
        </v-tab>
        <v-tab>
          <v-icon left>
            mdi-certificate
          </v-icon>
          Digital Certificate
        </v-tab>
  
        <v-tab-item>
          <v-card flat>
              <v-container fluid>

                <form>
                    <v-text-field
                        v-model="first_name"
                        :error-messages="first_name_error"
                        label="First Name"
                        required
                        @input="$v.name.$touch()"
                        @blur="$v.name.$touch()"
                    ></v-text-field>
                    <v-text-field
                        v-model="last_name"
                        :error-messages="last_name_error"
                        label="Last Name"
                        required
                        @input="$v.name.$touch()"
                        @blur="$v.name.$touch()"
                    ></v-text-field>
                    <v-text-field
                        v-model="email"
                        :error-messages="email_errors"
                        label="E-mail"
                        required
                        @input="$v.email.$touch()"
                        @blur="$v.email.$touch()"
                    ></v-text-field>
                    <v-text-field
                        v-model="address"
                        :error-messages="address_errors"
                        label="Address"
                        required
                        @change="$v.select.$touch()"
                        @blur="$v.select.$touch()"
                    ></v-text-field>
                    <v-text-field
                        v-model="organization"
                        :error-messages="organization_errors"
                        label="Organization"
                        required
                        @change="$v.select.$touch()"
                        @blur="$v.select.$touch()"
                    ></v-text-field>
                    <v-btn
                        dark
                        class="mr-4"
                        color="#C85250"
                        @click="submit"
                    >
                        Save Change
                    </v-btn>
                </form>
              </v-container>
          </v-card>
        </v-tab-item>
        <v-tab-item>
          <v-card flat>
            <v-container fluid>
                <form>
                    <v-text-field
                        v-model="password"
                        :error-messages="password_errors"
                        label="New Password"
                        :type="show1 ? 'text' : 'password'"
                        required
                        @change="$v.select.$touch()"
                        @blur="$v.select.$touch()"
                        >
                    </v-text-field>
                    <v-text-field
                        v-model="confirm_password"
                        :error-messages="password_errors"
                        label="Confirm New Password"
                        :type="show1 ? 'text' : 'password'"
                        required
                        @change="$v.select.$touch()"
                        @blur="$v.select.$touch()"
                        >
                    </v-text-field>
                </form>
                    <v-btn
                        dark
                        class="mr-4"
                        color="#C85250"
                        @click="submit"
                    >
                        Save Change
                    </v-btn>
            </v-container>
          </v-card>
        </v-tab-item>
        <v-tab-item>
            <v-container fluid>
                <v-card flat>
                    <v-dialog
                        v-model="dialog"
                        persistent
                        max-width="600px"
                    >
                        <template v-slot:activator="{ on, attrs }" >
                            <v-btn
                                v-if="!digCert && isVerified=='true'"
                                dark
                                class="mr-4"
                                color="#C85250"
                                v-bind="attrs"
                                v-on="on"
                            >
                                Create New
                            </v-btn>
                            <v-btn
                                v-if="digCert || isVerified=='false'"
                                
                                class="mr-4"
                                color="#C85250"
                                v-bind="attrs"
                                v-on="on"
                                disabled
                            >
                                Create New
                            </v-btn>
                        </template>
                        <v-card>
                            <v-card-title class="text-h5 red lighten-1 white--text">
                                Create Password for Digital Certificate
                                <v-spacer></v-spacer>
                                <v-btn
                                    icon
                                    dark
                                    @click="dialog = false"
                                >
                                    <v-icon>mdi-close</v-icon>
                                </v-btn>
                            </v-card-title>
                                <v-form @submit.prevent="createCert" v-bind="isValid" ref="form">
                                    <v-container>
                                            <v-text-field
                                                v-model="Cpassword"
                                                prepend-icon="lock"
                                                label="Password"
                                                type="password"
                                                :rules="passwordValidation"
                                                required
                                            ></v-text-field>
                                            <v-text-field
                                                v-model="Cconfirm_password"
                                                prepend-icon="lock"
                                                label="Confirm Password"
                                                type="password"
                                                :rules="confirmVal"
                                                required
                                            ></v-text-field>

                                    </v-container>
                                    <v-card-actions>
                                        <v-spacer></v-spacer>
                                        <v-btn                                     
                                        class="mr-4"
                                        color="#C85250"
                                        :disabled="!isValid"
                                        type="submit"
                                        dark
                                        >
                                        Confirm
                                        </v-btn>
                                    </v-card-actions>
                                </v-form>
                        </v-card>
                    </v-dialog>
                    <v-list-item three-line v-if="digCert">
                      <v-list-item-content >
                          <div class="text-overline mb-4">
                          Status
                          </div>
                          <v-list-item-title class="text-h5 mb-1">
                          Active
                          </v-list-item-title>
                      </v-list-item-content>
                  
                      <v-list-item-avatar tile size="80">
                          <v-sheet color="green" width="80" height="80" elevation="10">
                              <v-icon dark large>verified_user</v-icon>
                          </v-sheet>
                      </v-list-item-avatar>
                    </v-list-item>
                    <v-list-item three-line v-if="!digCert">
                      <v-list-item-content >
                          <div class="text-overline mb-4">
                          Status
                          </div>
                          <v-list-item-title class="text-h5 mb-1">
                          Not Active
                          </v-list-item-title>
                      </v-list-item-content>
                  
                      <v-list-item-avatar tile size="80">
                          <v-sheet color="red" width="80" height="80" elevation="10">
                              <v-icon dark large>mdi-close-circle</v-icon>
                          </v-sheet>
                      </v-list-item-avatar>
                    </v-list-item>
                </v-card>
                <!-- <v-btn @click="test">load</v-btn>
                <v-btn @click="getAccount">test</v-btn> -->
            </v-container>
        </v-tab-item>
      </v-tabs>
      <v-dialog
            v-model="loading"
            persistent
            width=500
            heigth=500
            
        >
            <v-container style="height: 400px;background-color:white" >
                <v-row
                    class="fill-height"
                    align-content="center"
                    justify="center"
                >
                    <v-col
                    class="text-subtitle-1 text-center"
                    cols="12"
                    >
                    Please Wait
                    </v-col>
                    <v-col cols="6">
                    <v-progress-linear
                        color="#C85250"
                        indeterminate
                        rounded
                        height="6"
                    ></v-progress-linear>
                    </v-col>
                    <v-col
                    class="text-subtitle-1 text-center"
                    cols="12"
                    >
                    Creating Digital Certificate
                    </v-col>
                </v-row>
            </v-container>
        </v-dialog>
    </v-card>
    
</template>


<script>
import { mapState } from 'vuex'
import axios from 'axios'
import { create } from 'ipfs-http-client'
import swal from 'sweetalert';
import Web3 from 'web3'
import certificate from '/build/contracts/digitalCertificate.json'

export default {
  name:'Dashboard',
//   computed: {
//         ...mapState(['account'])
//     },

  data(){
    return{
        first_name:localStorage.getItem('first_name'),
        last_name:localStorage.getItem('last_name'),
        email:localStorage.getItem('email'),
        address:localStorage.getItem('address'),
        organization:localStorage.getItem('organization'),
        password:'',
        confirm_password:'',
        Cpassword:'',
        Cconfirm_password:'',
        dialog: false,
        key:'',
        pem:'',
        digCert:localStorage.getItem('cert_url'),
        isVerified:localStorage.getItem('is_verified'),

        isValid:true,
        passwordValidation:[
            v => !!v || 'Password is required',
            v => v.length <= 12 || 'Password must be less than 12 characters',
            v => v.length >= 4 || 'Password must more than 4 characters',
            
        ],
        confirmVal:[
            v => !!v || 'Password is required',
            v => v.length <= 12 || 'Password must be less than 12 characters',
            v => v.length >= 4 || 'Password must more than 4 characters',
            v => v ==  this.Cpassword|| 'Password must match',
        ],     
        loading:false
  }
},
  methods:{
      suksesAlert() {
            swal({
            icon: "success",
            title: "Succesfully",
            text: "Certificate was created",
            button: "Confirm",
            })
         },
      async createCert(){
        this.loading=true
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

        axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
        const data = {
            "first_name":this.first_name,
            "last_name":this.last_name,
            "password":this.Cpassword,
            "email":this.email,
            "organization":this.organization
        }
        // console.log(data)
        axios.post("http://localhost:8000/api/documents/createcert", data)
        .then(response => {
          this.dialog= false
          this.key = response.data.key
          this.pem = response.data.pem
          localStorage.setItem('cert_url',this.key)
          this.addCert()
              
        })
        .catch(error => {
                   console.log(error)
               })
        
      },

      async  addCert(){
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
        const accounts = await web3.eth.getAccounts()
        const networkId = await web3.eth.net.getId()
        const networkData = certificate.networks[networkId]
        if(networkData) {
          const abi = certificate.abi
          const address = networkData.address
          // console.log(accounts.toString())
          const contract = new web3.eth.Contract(abi,address)
          const getCertificate = await contract.methods.addCertificate(this.email,this.key,this.pem).send({from : accounts.toString()}).then((r)=>{
            this.loading=false
            this.suksesAlert()
          })
          console.log(getCertificate)
        } else {
          window.alert('Smart contract not deployed to detected network.')
        }
        
      },

      async  test(){
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
        const accounts = await web3.eth.getAccounts()
        const networkId = await web3.eth.net.getId()
        const networkData = certificate.networks[networkId]
        if(networkData) {
          const abi = certificate.abi
          const address = networkData.address
          // console.log(accounts.toString())
          const contract = new web3.eth.Contract(abi,address)
          const getCertificate = await contract.methods.certificates("ashtsaqofi@gmail.com").call()
          console.log(getCertificate)
        } else {
          window.alert('Smart contract not deployed to detected network.')
        }
        
      },

     
  }      
}
</script>