<template>
    <v-main>
         <v-container fluid fill-height v-if="doc_id==''">
            <v-layout align-center justify-center>
               <v-flex xs12 sm8 md4>
                   <v-tabs class="d-flex justify-center mb-6" grow  color=#C85250>
                     <v-tab >
                        
                           Validate Document
                     </v-tab>
                     <v-tab to='/'>
                        
                           Login
                     </v-tab>
                  </v-tabs>
                   <v-form @submit.prevent="onUploadFile">
                        <v-card>
                        
                            <v-card-title class="text-h5 red lighten-1 white--text">
                                Validate PDF Document
                            </v-card-title>
                            <v-container>
                                <v-file-input
                                required
                                accept=".pdf"
                                show-size
                                truncate-length="50"
                                placeholder="Upload your PDF"
                                @change="onFileSelect"
                                color=#C85250
                                >
                                </v-file-input>
                            </v-container>
                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn
                                dark
                                class="mr-4"
                                color="#C85250"
                                type="submit"
                                >
                                Confirm
                                </v-btn>
                            </v-card-actions>
                        </v-card>
                </v-form>
               </v-flex>
            </v-layout>
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
                            Signing This Document
                            </v-col>
                        </v-row>
                    </v-container>
                </v-dialog>
         </v-container>
         <v-container v-else>
             <v-col >
                <v-card class="elevation-12">
                    <v-card-title  class="text-h5 red lighten-1 white--text">
                                Document Validation Results
                        <v-spacer></v-spacer>
                         <v-btn
                             icon
                             dark
                             @click="doc_id=''"
                         >
                             <v-icon>mdi-close</v-icon>
                         </v-btn>
                    </v-card-title>
                     <v-tabs grow background-color=#C85250 color=white>
                        <v-tab>
                            <v-icon left>
                                mdi-text-box-search-outline
                            </v-icon>
                                Details
                        </v-tab>
                        <v-tab>
                            <v-icon left>
                                mdi-account-details-outline
                            </v-icon>
                                History
                        </v-tab>
                        <v-tab-item>
                            <v-card flat>
                                <v-container fluid>
                                    <v-container style="height: 400px;" v-if="!documentVal">
                                        <v-row
                                            class="fill-height"
                                            align-content="center"
                                            justify="center"
                                        >
                                            <v-col
                                            class="text-subtitle-1 text-center"
                                            cols="12"
                                            >
                                            Getting Document Validation
                                            </v-col>
                                            <v-col cols="6">
                                            <v-progress-linear
                                                color="#C85250"
                                                indeterminate
                                                rounded
                                                height="6"
                                            ></v-progress-linear>
                                            </v-col>
                                        </v-row>
                                    </v-container>
                                    <v-container v-if="documentVal">
                                        <v-alert
                                            v-if="documentVal['status']==true"
                                            type="success"
                                        >This Document is Valid</v-alert>
                                        <v-alert
                                            v-if="documentVal['status']==false"
                                            type="error"
                                        >This Document Invalid</v-alert>
                                        <v-card v-for="list in documentVal['details']" :key="list"
                                            class="ma-5"
                                            
                                            outlined
                                            elevation="10"
                                        >
                                            <v-list-item three-line>
                                            <v-list-item-content>
                                                

                                                <div class="text-overline mb-4">
                                                Signature 
                                                </div>
                                                <v-expansion-panels>
                                                    <v-expansion-panel>
                                                        <v-expansion-panel-header>
                                                            Signer
                                                        </v-expansion-panel-header>
                                                        <v-expansion-panel-content>
                                                            {{list['Penandatangan']}}
                                                        </v-expansion-panel-content>
                                                    </v-expansion-panel>
                                                    <v-expansion-panel>
                                                        <v-expansion-panel-header>
                                                            Time
                                                        </v-expansion-panel-header>
                                                        <v-expansion-panel-content>
                                                            {{list['Waktu TTE']}}
                                                        </v-expansion-panel-content>
                                                    </v-expansion-panel>
                                                    <v-expansion-panel>
                                                        <v-expansion-panel-header>
                                                            Modification
                                                        </v-expansion-panel-header>
                                                        <v-expansion-panel-content>
                                                            {{list['Perubahan']}}
                                                        </v-expansion-panel-content>
                                                    </v-expansion-panel>
                                                </v-expansion-panels>
                                                
                                            </v-list-item-content>
                                            
                                            </v-list-item>
                                        </v-card>
                                    </v-container>
                                    
                                </v-container>
                            </v-card>
                        </v-tab-item>
                        <v-tab-item>
                             <v-card flat>
                                <v-container fluid v-for="list in signer" :key="list">
                                    <v-card
                                        class="mx-auto"
                                        outlined

                                    >
                                        <v-list-item three-line>
                                        <v-list-item-content>
                                            <div class="text-overline mb-4">
                                            Signer
                                            </div>
                                            <v-list-item-title class="text-h5 mb-1">
                                            {{list.first_name+' '+list.last_name}}
                                            </v-list-item-title>
                                            <v-list-item-subtitle>{{list.email}}</v-list-item-subtitle>
                                        </v-list-item-content>

                                        
                                        </v-list-item>
                                        
                                    </v-card>
                                    <v-expansion-panels>
                                        <v-expansion-panel>
                                            <v-expansion-panel-header>
                                                Document Hash
                                            </v-expansion-panel-header>
                                            <v-expansion-panel-content>
                                            {{list.hash}}
                                            </v-expansion-panel-content>
                                        </v-expansion-panel>
                                    </v-expansion-panels>

                                </v-container>
                             </v-card>
                        </v-tab-item>
                     </v-tabs>
                </v-card>
            </v-col>
         </v-container>
    </v-main>
</template>


<script>
import axios from 'axios'
import { create } from 'ipfs-http-client'
import swal from 'sweetalert';
import Web3 from 'web3'
import sign from '/build/contracts/sign.json'

export default {
    data: () => ({
        file: [],
        signedFile: [],
        
        errors:[],
        fileUpload:[],
        status:{
            buffer:''
        },
        file_url:'',
        doc_hash:'',
        doc_id:'',
        documentVal:null,
        loading:false,
        signer:[]

    }) ,
    methods:{
        onFileSelect(event){
            this.fileUpload=event
           
            
            
            
            const reader= new window.FileReader()
            reader.readAsArrayBuffer(this.fileUpload)
            reader.onloadend = ()=>{
                this.buffer=Buffer(reader.result)
                // console.log('buffer', Buffer(reader.result))
            }
        },
        async onUploadFile(){
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

            const projectId = '20dxCr0ToSu5lgXBJbEqJNHMS2i'
            const projectSecret = '712c4dd9c8ea398c359e9877f781dcfb'
            const auth ='Basic ' + Buffer.from(projectId + ':' + projectSecret).toString('base64')

            this.client = create({
                host: 'ipfs.infura.io',
                port: 5001,
                protocol: 'https',
                headers: {
                    authorization: auth
                }
            })

            this.client.add(this.buffer)
            .then(response=>{
                
                this.file_url="https://ipfs.infura.io/ipfs/"+response.path
                this.getDocHash().then(r=>{
                    this.getDocId().then(r=>{
                        this.loading=false
                        if(this.doc_id!=''){
                            const data={
                                "file_url":this.file_url
                            }
                            axios
                                .post("http://localhost:8000/api/documents/signvalidation",data)
                                .then(response=>{
                                    this.documentVal=response.data
                                })
                            
                            this.getValidation()
                        }else{
                            swal({
                            icon:"error",
                            title: "Document Not Valid",
                            text:"Your document unidentified or already change",
                            button: "Confirm",
                        })
                        }
                        
                    })
                })
                
                
            })
            
            .catch(error=>{
                if (error.response){
                    for (const property in error.response.data){
                        // this.errors.push(`${property}:${error.response.data[property]}`)
                        this.loading=false
                        swal({
                            icon:"error",
                            title: "Upload File",
                            text: `${property}:${error.response.data[property]}`,
                            button: "Confirm",
                        })
                    }
                    }else if(error.message){
                        swal({
                            icon:"error",
                            title: "Upload File",
                            text: "Something went wrong. Please try again !",
                            button: "Confirm",
                        })
                        // this.errors.push('Something went wrong. Please try again !')
                    }
            })
            
            
        },
        async getDocHash(){
            let data={
                "file_url":this.file_url
            }
            await axios
                .post('api/documents/getdochash',data)
                .then(response => {
                       this.doc_hash = response.data.hash
                       return this.doc_hash
                   })
                   .catch(error => {
                       console.log(error)
                   })
            
        },
        async getDocId(){
            let id=''
            await axios
                .get('/api/documents/hashlist/',{ params: { hash: this.doc_hash } })
                .then(response => {
                    this.doc_id=response.data[0].doc_id
                   
                })
                .catch(error => {
                    console.log(error)
                })
            
        },
        async getValidation(){
            web3 = window.web3
            // const accounts = await web3.eth.getAccounts()
            const networkId = await web3.eth.net.getId()
            const networkData = sign.networks[networkId]
            if(networkData) {
                const abi = sign.abi
                const address = networkData.address
                
                // console.log(accounts.toString())
                const contract = new web3.eth.Contract(abi,address)
                const countSigner = await contract.methods.countSigner(this.doc_id).call()
                for(let i=0;i<countSigner;i++){
                    const getSigner = await contract.methods.document(this.doc_id,i).call()
                    this.signer.push(getSigner)
                }
            } else {
                window.alert('Smart contract not deployed to detected network.')
            }
        },
        async test(){
            
            console.log("ISINYA",this.doc_id)
        }
    }   
}
</script>