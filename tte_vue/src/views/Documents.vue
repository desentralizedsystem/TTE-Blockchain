<template>
    <div>
        <h1 class="subheading grey--text">Documents</h1>
        <v-dialog
            v-model="dialog"
            
            max-width="600px"
        >
            <template v-slot:activator="{ on, attrs }">
                <v-btn
                    
                    class="mr-4"
                    color="#C85250"
                    v-bind="attrs"
                    v-on="on"
                    disabled
                    v-if="isVerified=='false'"
                >
                    Upload New Document 
                </v-btn>
                <v-btn
                    dark
                    class="mr-4"
                    color="#C85250"
                    v-bind="attrs"
                    v-on="on"
                    v-else-if="isVerified=='true'"
                >
                    Upload New Document 
                </v-btn>
            </template>
            <v-form @submit.prevent="onUploadFile">
                <v-card>
                    <!-- <v-toolbar
                    dark
                    color="primary"
                    ></v-toolbar> -->
                    <v-card-title class="text-h5 red lighten-1 white--text">
                        Upload Document
                        <v-spacer></v-spacer>
                        <v-btn
                            icon
                            dark
                            @click="dialog = false"
                        >
                            <v-icon>mdi-close</v-icon>
                        </v-btn>
                    </v-card-title>
                    <v-container>
                        <v-file-input
                        required
                        accept=".pdf"
                        show-size
                        truncate-length="50"
                        placeholder="Upload your PDF"
                        @change="onFileSelect"
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
            </v-dialog>
        <v-tabs grow background-color=white color=#C85250>
            <v-tab>
                 Documents
            </v-tab>
            <v-tab>
                
                    Self Signed Documents
            </v-tab>
            <v-tab-item>
                <v-data-table
                    :headers="headers"
                    :items="file"
                    sort-by="File"
                    class="elevation-1"
                >
                    <template v-slot:item.actions="{ item }">
                        <v-btn tile color="success" @click="$router.push('/document/'+item.id)" v-if="isCert">Detail</v-btn>
                        <v-btn tile color="success" @click="$router.push('/document/'+item.id)" disabled v-else>Detail</v-btn>
                    </template>
                </v-data-table>

            </v-tab-item>
            <v-tab-item>
                <v-data-table
                    :headers="headers"
                    :items="signedFile"
                    sort-by="File"
                    class="elevation-1"
                >
                    <template v-slot:item.actions="{ item }">
                        <v-btn tile color="success" @click="$router.push('/document/selfsigndoc'+item.id)">Detail</v-btn>
                        
                    </template>
                </v-data-table>

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
                    Uploading This Document
                    </v-col>
                </v-row>
            </v-container>
        </v-dialog>
        <!-- <v-btn @click="test"> just</v-btn> -->
        </div>
    
</template>

<script>
import axios from 'axios'
import { create } from 'ipfs-http-client'
import swal from 'sweetalert';

export default {
    data: () => ({
        dialog: false,
        
        isVerified:localStorage.getItem('is_verified'),
        isCert:localStorage.getItem('cert_url'),
  
        // ipfsClient:create('https://ipfs.infura.io:5001/api/v0'),

        headers: [
            {
                text: 'File Name',
                align: 'start',
                sortable: false,
                value: 'file_name',
            },
            { text: 'Size (KB)', value: 'size' },
            { text: 'Date', value: 'time' },
            { text: 'Status', value: 'status' },
            { text: 'Actions', value: 'actions', sortable: false },
        ],
        file: [],
        signedFile: [],
        
        errors:[],
        fileUpload:[],
        status:{
            buffer:''
        },
        fileDetail:{
            file_name:'',
            size:'',
            status:'',
            file_url:''
        },
        loading:false
    
        
    }),
    
    
    methods: {
        onFileSelect(event){
            this.fileUpload=event
            console.log(event)
            this.fileDetail.file_name=event.name
            this.fileDetail.size=Math.round(event.size/1000)
            console.log(this.fileDetail.size)
            this.fileDetail.status='Original Document'
            const reader= new window.FileReader()
            reader.readAsArrayBuffer(this.fileUpload)
            reader.onloadend = ()=>{
                this.buffer=Buffer(reader.result)
                // console.log('buffer', Buffer(reader.result))
            }
        },

        onUploadFile(){
            this.loading=true

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
                this.dialog=false
                console.log(response)
                this.fileDetail.file_url="https://ipfs.infura.io/ipfs/"+response.path
                axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
                axios
                .post("api/documents/",this.fileDetail)
                this.loading=false
                swal({
                    icon:"success",
                    title: "Upload File",
                    text: "File has been uploaded",
                    button: "Confirm",
                    closeOnClickOutside : false
                }).then((value)=>{
                this.$router.go()
            })
            })
            .catch(error=>{
                if (error.response){
                    for (const property in error.response.data){
                        // this.errors.push(`${property}:${error.response.data[property]}`)
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
            // this.dialog=false
        },

        test(){
            console.log(this.signedFile)
        }
        
    },
    beforeMount(){
        axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
        axios
        axios.get("http://localhost:8000/api/documents")
        .then((response) => {
                this.file = response.data
        });
        axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
        axios
        axios.get("/api/documents/selfsigndoc")
        .then((response) => {
                this.signedFile = response.data
                
        });
        
    },
}
</script>

