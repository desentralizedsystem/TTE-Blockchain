<template>
    <div>
        <h1 class="subheading grey--text">Signature Request</h1>
        <br>
        <!-- <v-row align="left">
            <v-btn dark color="#C85250">Sent</v-btn>
            <v-divider class="mx-1" vertical></v-divider>
            <v-btn dark color="#C85250">Received</v-btn>
        </v-row> -->
        <v-toolbar>
            <v-tabs
                dark
                background-color=#C85250
                grow
            >
                <v-tab  href="#sent">Sent</v-tab>
                <v-tab-item value="sent">
                    <v-data-table
                    :headers="header1"
                    :items="sentDoc"
                    sort-by="File"
                    class="elevation-1"
                    >
                        <template v-slot:item.actions="{ item }" >
                            <v-btn tile color="success" v-if="(item.status=='Pending')" disabled>Detail</v-btn>
                            <v-btn tile color="success" v-else-if="(item.status!='Pending')&&(isCert)" @click="$router.push('/document/getsentreq'+item.id)">Detail</v-btn>
                            <v-btn tile color="success" v-else disabled @click="$router.push('/document/getsentreq'+item.id)">Detail</v-btn>
                        </template>
                    </v-data-table>
                </v-tab-item>
                <v-tab href="#received">Received</v-tab>
                <v-tab-item value="received">
                    <v-data-table
                    :headers="header2"
                    :items="receiveDoc"
                    sort-by="File"
                    class="elevation-1"
                    >
                        <template v-slot:item.actions="{ item }">
                            <v-btn tile color="success" @click="$router.push('/document/getreceive'+item.id)" v-if="isCert">Detail</v-btn>
                            <v-btn tile color="success" @click="$router.push('/document/getreceive'+item.id)" v-else disabled>Detail</v-btn>
                        </template>
                    </v-data-table>
                </v-tab-item>
            </v-tabs>
            
        </v-toolbar>
        <br>
        
    </div>
</template>

<script>
import axios from 'axios'


export default {
    data: () => ({
    dialog: false,
    tmpDATA:[],
    len:null,
    sentDoc:[],
    receiveDoc:[],
    isCert:localStorage.getItem('cert_url'),
    header1: [
      {
        text: 'File Name',
        align: 'start',
        sortable: false,
        value: 'file_name',
      },
      // { text: 'Recipient', value: 'Recipient' },
      { text: 'Date', value: 'time' },
      { text: 'Status', value: 'status' },
      { text: 'Actions', value: 'actions', sortable: false },
    ],
    sent: [],
    header2: [
      {
        text: 'File Name',
        align: 'start',
        sortable: false,
        value: 'file_name',
      },
      { text: 'Sender', value: 'sender' },
      { text: 'Date', value: 'time' },
      { text: 'Status', value: 'status' },
      { text: 'Actions', value: 'actions', sortable: false },
    ],
    received: [],
  }),

  created () {
    this.initialize()
  },

  methods: {
    initialize () {
      this.sent = [
        {
          File: 'Proposal Donor Darah',
          Recipient: 'Jono',
          Date: '10-10-2019',
          Status: 'Pending',
        },
      ]
      this.received = [
        {
          File: 'Proposal Donor Darah',
          Sender: 'Jono',
          Date: '10-10-2019',
          Status: 'Pending',
        },
      ]
    },
  },
  async beforeMount(){
        axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
        await axios
        .get(`/api/documents/getsentreq/`)
        .then((response) => {
                this.tmpDATA = response.data
                this.len = this.tmpDATA.length
                // console.log(response.data)
        });
        
        for(let i=0;i<this.len;i++){
                const data = {
                    id:this.tmpDATA[i].id,
                    file_name:this.tmpDATA[i].original_file.file_name,
                    status:this.tmpDATA[i].status,
                    time:this.tmpDATA[i].original_file.time,
                    file_url:this.tmpDATA[i].signed_url
                }
                // console.log(data)
                this.sentDoc.push(data)
            }
        axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
        await axios
        .get(`/api/documents/getreceive/`)
        .then((response) => {
                this.tmpDATA = response.data
                this.len = this.tmpDATA.length
                // console.log(response.data)
        });
        let tmpUrl=''
        for(let i=0;i<this.len;i++){
                if(this.tmpDATA[i].doc_url.signed_url==null){
                  tmpUrl=this.tmpDATA[i].doc_url.original_file.file_url
                }else{
                  tmpUrl=this.tmpDATA[i].doc_url.signed_url
                }
                const data = {
                    id:this.tmpDATA[i].id,
                    file_name:this.tmpDATA[i].doc_url.original_file.file_name,
                    sender:this.tmpDATA[i].doc_url.author.first_name+" "+this.tmpDATA[i].doc_url.author.last_name,
                    status:this.tmpDATA[i].doc_url.status,
                    time:this.tmpDATA[i].doc_url.original_file.time,
                    file_url:this.tmpDATA[i].signed_url
                }
                // console.log(data)
                this.receiveDoc.push(data)
            }
    },
}
</script>