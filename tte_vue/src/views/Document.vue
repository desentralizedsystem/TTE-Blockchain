<template>
    <v-container v-if="this.$route.params.id.search('getsentreq')==0" fluid fill-height>
        <v-row >
            <v-col cols="12" sm="6" md="8">
                <h2 class="subheading grey--text">{{document.original_file.file_name}}</h2>    
                <div v-if="thisHash">
                    <h5 class="subheading grey--text">Document Hash</h5>    
                    <h5 class="subheading grey--text">{{thisHash}}</h5>    

                </div>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12" sm="6" md="8">
                <vue-pdf-app style="height:80vh;"
                :pdf=document.signed_url
                :config="config"
                >
                </vue-pdf-app>
               
            </v-col>
            <v-col cols="6" md="4">
                <v-card class="elevation-12">
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
        </v-row>
    </v-container>
    <v-container v-else-if="this.$route.params.id.search('selfsigndoc')==0" fluid fill-height>
        <!-- <v-btn @click="test">test</v-btn> -->
        <v-row >
            <v-col cols="12" sm="6" md="8">
                <h2 class="subheading grey--text">{{document.file_name}}</h2>    
                <div v-if="thisHash">
                    <h5 class="subheading grey--text">Document Hash</h5>    
                    <h5 class="subheading grey--text">{{thisHash}}</h5>    

                </div>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12" sm="6" md="8">
                <vue-pdf-app style="height:80vh;"
                :pdf=document.signed_url
                :config="config"
                >
                </vue-pdf-app>
               
            </v-col>
            <v-col cols="6" md="4">
                <v-card class="elevation-12">
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
        </v-row>
    </v-container>
    <v-container v-else fluid fill-height>
        
        <v-row >
            <v-col cols="12" sm="6" md="8">
                <h2 v-if="(this.$route.params.id.search('getreceive')!=0)&&(this.$route.params.id.search('getsentreq')!=0)" class="subheading grey--text">{{document.file_name}}</h2>    
                <h2 v-else-if="(this.$route.params.id.search('getreceive')==0)" class="subheading grey--text">{{document.doc_url.original_file.file_name}}</h2>    
                <h2 v-else class="subheading grey--text">{{document.original_file.file_name}}</h2>    
                <div v-if="thisHash">
                    <h5 class="subheading grey--text">Document Hash</h5>    
                    <h5 class="subheading grey--text">{{thisHash}}</h5>    

                </div>
            </v-col>
            <v-col cols="6" md="4" >
                <v-btn
                    v-if="(this.$route.params.id.search('getreceive')==0)&&(document.status!='Signed')"
                    dark
                    class="mr-4"
                    color="#C85250"
                    v-bind="attrs"
                    v-on="on"
                    @click="signReq =true"
                    block
                    x-large
                >
                    <v-icon left >mdi-draw</v-icon>Sign
                </v-btn>
                <v-dialog
                        v-if="this.$route.params.id.search('getreceive')!=0"
                        v-model="dialog"
                        persistent
                        max-width="455px"
                >
                        <template v-slot:activator="{ on, attrs }">
                            <v-btn
                                v-if="(document.status!='Self Signed')&&(document.status!='Original Document (self signed)')&&(document.status!='Original Document (Sign Requested)')&&(document.status!='Signed')"
                                dark
                                class="mr-4"
                                color="#C85250"
                                v-bind="attrs"
                                v-on="on"
                                block
                                x-large
                            >
                                <v-icon left >mdi-draw</v-icon>Sign
                            </v-btn>
                        </template>
                        <v-card>
                            <v-card-title class="text-h5 red lighten-1 white--text">
                                Sign This Document
                                <v-spacer></v-spacer>
                                <v-btn
                                    icon
                                    dark
                                    @click="dialog = false"
                                >
                                    <v-icon>mdi-close</v-icon>
                                </v-btn>
                            </v-card-title>
                            <v-container  >
                                <v-row dense>
                                    <c-col >
                                        <v-card
                                            outlined
                                            @click="selfSign =true"
                                            width=440
                                        >
                                            <v-list-item three-line>
                                            <v-list-item-content>
                                            
                                                <v-list-item-title class="text-h5 mb-1">
                                                Self Sign 
                                                </v-list-item-title>
                                                <v-list-item-subtitle>Self sign your document</v-list-item-subtitle>
                                            </v-list-item-content>

                                            <v-list-item-avatar
                                                tile
                                                size="100"
                                                color="#C85250"
                                            >
                                            <v-icon dark>mdi-file-document</v-icon>
                                            </v-list-item-avatar>
                                            </v-list-item>
                                        </v-card>
                                    </c-col>
                                    <br>
                                    <c-col >
                                        <v-card
                                            outlined
                                            @click="creteSignReq"
                                            width=440
                                        >
                                            <v-list-item three-line>
                                            <v-list-item-content>
                                            
                                                <v-list-item-title class="text-h5 mb-1">
                                                Sign and Request  
                                                </v-list-item-title>
                                                <v-list-item-subtitle>Sign and request other to sign your document</v-list-item-subtitle>
                                            </v-list-item-content>

                                            <v-list-item-avatar
                                                tile
                                                size="100"
                                                color="#C85250"
                                            >
                                            <v-icon dark>mdi-account-plus</v-icon>
                                            </v-list-item-avatar>
                                            </v-list-item>
                                        </v-card>
                                    </c-col>
                                    <br>
                                    <c-col >
                                        <v-card
                                            outlined
                                            @click="creteSignReqOther"
                                            width=440
                                        >
                                            <v-list-item three-line>
                                            <v-list-item-content>
                                            
                                                <v-list-item-title class="text-h5 mb-1">
                                                Request From Other
                                                </v-list-item-title>
                                                <v-list-item-subtitle>Share your document to be signed</v-list-item-subtitle>
                                            </v-list-item-content>

                                            <v-list-item-avatar
                                                tile
                                                size="100"
                                                color="#C85250"
                                            >
                                            <v-icon dark>mdi-account-search</v-icon>
                                            </v-list-item-avatar>
                                            </v-list-item>
                                        </v-card>
                                    </c-col>  
                                </v-row>
                            </v-container>
                        </v-card>
                </v-dialog>
                <v-dialog
                        v-model="reqSign"
                        persistent
                        max-width="655px"
                >
                    <template >
                        <v-card>
                            <v-card-title class="text-h5 red lighten-1 white--text">
                                Sign and request other to sign your document
                                <v-spacer></v-spacer>
                                <v-btn
                                    icon
                                    dark
                                    @click="deleteSignReq"
                                >
                                    <v-icon>mdi-close</v-icon>
                                </v-btn>
                            </v-card-title>
                            <v-container>
                                <v-row dense>
                                    <v-col cols="5">
                                        <v-card
                                            outlined    
                                        >
                                            <v-list-item >
                                                <v-list-item-content>
                                                    <div class="text-overline mb-4">
                                                        Add Recipient
                                                    </div>
                                                </v-list-item-content>
                                            </v-list-item>
                                            <v-alert
                                            type="error"
                                            v-if="errors"
                                            dense
                                            max-height="50px"
                                            
                                            >
                                            {{errors}}
                                            </v-alert>
                                            <form @submit.prevent="addReqSigner">
                                            <v-text-field
                                                v-model="reqSignerEmail"
                                                :error-messages="email_errors"
                                                label="E-mail"
                                                required
                                               
                                            ></v-text-field>
                                            <v-card-actions>
                                                <v-spacer></v-spacer>
                                                <v-btn
                                                dark
                                                color="#C85250"
                                                type="submit"
                                                >
                                                Add
                                                </v-btn>
                                            </v-card-actions>
                                        </form>
                                        </v-card>
                                    </v-col>
                                    <v-col cols="7">
                                        <v-card
                                            outlined    
                                        >
                                            <v-list-item >
                                                <v-list-item-content>
                                                    <div class="text-overline mb-4">
                                                        Recipient List
                                                    </div>
                                                </v-list-item-content>
                                                
                                                    
                                            </v-list-item>
                                            
                                            <v-data-table
                                                hide-default-header
                                                hide-default-footer
                                                :items="reqSigner"
                                                :headers="headers"
                                            >
                                                <template v-slot:item.actions="{ item }">
                                                    <v-icon
                                                        small
                                                        class="mr-2"
                                                        @click="deleteSignerReq(item.id)"
                                                    >
                                                        mdi-cancel
                                                    </v-icon>
                                                </template>
                                            </v-data-table>
                                        </v-card>
                                    </v-col>
                                </v-row>
                                <v-row >
                                    <v-col cols="12" >
                                        <template>
                                            <v-card
                                                class="d-flex pa-2 justify-md-center"
                                                tile
                                            >
                                                
                                                <v-list-item >
                                                        <v-list-item-content>
                                                            <div class="text-overline">
                                                                Confirm Recipient and Sign this Document
                                                            </div>
                                                        </v-list-item-content>
                                                </v-list-item>
                                                <v-card-actions>
                                                    <v-btn tile color="success" @click="signAndReq=true">Confirm</v-btn>
                                                </v-card-actions>
                                            </v-card>
                                        </template>
                                    </v-col>
                                </v-row>
                            </v-container>
                        </v-card>
                    </template>
                </v-dialog>
                <v-dialog
                        v-model="otherSign"
                        persistent
                        max-width="655px"
                >
                    <template >
                        <v-card>
                            <v-card-title class="text-h5 red lighten-1 white--text">
                                request other to sign your document
                                <v-spacer></v-spacer>
                                <v-btn
                                    icon
                                    dark
                                    @click="deleteSignReqOther"
                                >
                                    <v-icon>mdi-close</v-icon>
                                </v-btn>
                            </v-card-title>
                            <v-container>
                                <v-row dense>
                                    <v-col cols="5">
                                        <v-card
                                            outlined    
                                        >
                                            <v-list-item >
                                                <v-list-item-content>
                                                    <div class="text-overline mb-4">
                                                        Add Recipient
                                                    </div>
                                                </v-list-item-content>
                                            </v-list-item>
                                            <v-alert
                                                type="error"
                                                v-if="errors"
                                                dense
                                                max-height="50px"
                                                
                                            >
                                            {{errors}}
                                            </v-alert>
                                            <form @submit.prevent="addReqSigner">
                                            <v-text-field
                                                v-model="reqSignerEmail"
                                                :error-messages="email_errors"
                                                label="E-mail"
                                                required
                                            ></v-text-field>
                                            <v-card-actions>
                                                <v-spacer></v-spacer>
                                                <v-btn
                                                dark
                                                color="#C85250"
                                                type="submit"
                                                >
                                                Add
                                                </v-btn>
                                            </v-card-actions>
                                        </form>
                                        </v-card>
                                    </v-col>
                                    <v-col cols="7">
                                        <v-card
                                            outlined    
                                        >
                                            <v-list-item >
                                                <v-list-item-content>
                                                    <div class="text-overline mb-4">
                                                        Recipient List
                                                    </div>
                                                </v-list-item-content>
                                                
                                                    
                                            </v-list-item>
                                            <v-data-table
                                                hide-default-header
                                                hide-default-footer
                                                :items="reqSigner"
                                                :headers="headers"
                                            >
                                                <template v-slot:item.actions="{ item }">
                                                    <v-icon
                                                        small
                                                        class="mr-2"
                                                       @click="deleteSignerReq(item.id)"
                                                    >
                                                        mdi-cancel
                                                    </v-icon>
                                                </template>
                                            </v-data-table>
                                        </v-card>
                                    </v-col>
                                </v-row>
                                <v-row >
                                    <v-col cols="12" >
                                        <template>
                                            <v-card
                                                class="d-flex pa-2 justify-md-center"
                                                tile
                                            >
                                                
                                                <v-list-item >
                                                        <v-list-item-content>
                                                            <div class="text-overline">
                                                                Confirm Recipient to Sign this Document
                                                            </div>
                                                        </v-list-item-content>
                                                </v-list-item>
                                                <v-card-actions>
                                                    <v-btn tile color="success" @click="createOtherSignReq">Confirm</v-btn>
                                                </v-card-actions>
                                            </v-card>
                                        </template>
                                    </v-col>
                                </v-row>
                            </v-container>
                        </v-card>
                    </template>
                </v-dialog>
                <v-dialog
                    v-model="selfSign"
                    persistent
                    max-width="600px"
                >
                    <v-card>
                        <v-card-title class="text-h5 red lighten-1 white--text">
                            Self Sign This Document
                            <v-spacer></v-spacer>
                            <v-btn
                                icon
                                dark
                                @click="selfSign = false"
                            >
                                <v-icon>mdi-close</v-icon>
                            </v-btn>
                        </v-card-title>
                            <v-form @submit.prevent="selfSignDoc" v-bind="isValid" ref="form">
                                <v-container>
                                        <v-text-field
                                            v-model="password"
                                            prepend-icon="lock"
                                            label="Certificate Password"
                                            type="password"
                                            
                                            required
                                        ></v-text-field>
                                </v-container>
                                <v-card-actions>
                                    <v-spacer></v-spacer>
                                    <v-btn                                     
                                        class="mr-4"
                                        color="#C85250"
                                        
                                        type="submit"
                                        dark
                                    >
                                    Confirm
                                    </v-btn>
                                </v-card-actions>
                            </v-form>
                    </v-card>
                </v-dialog>
                <v-dialog
                    v-model="signReq"
                    persistent
                    max-width="600px"
                >
                    <v-card>
                        <v-card-title class="text-h5 red lighten-1 white--text">
                            Sign This Document
                            <v-spacer></v-spacer>
                            <v-btn
                                icon
                                dark
                                @click="signReq = false"
                            >
                                <v-icon>mdi-close</v-icon>
                            </v-btn>
                        </v-card-title>
                            <v-form @submit.prevent="signRequestedDoc" v-bind="isValid" ref="form">
                                <v-container>
                                        <v-text-field
                                            v-model="password"
                                            prepend-icon="lock"
                                            label="Certificate Password"
                                            type="password"
                                            
                                            required
                                        ></v-text-field>
                                </v-container>
                                <v-card-actions>
                                    <v-spacer></v-spacer>
                                    <v-btn                                     
                                        class="mr-4"
                                        color="#C85250"
                                        
                                        type="submit"
                                        dark
                                    >
                                    Confirm
                                    </v-btn>
                                </v-card-actions>
                            </v-form>
                    </v-card>
                </v-dialog>
                <v-dialog
                    v-model="signAndReq"
                    persistent
                    max-width="600px"
                >
                    <v-card>
                        <v-card-title class="text-h5 red lighten-1 white--text">
                            Sign This Document
                            <v-spacer></v-spacer>
                            <v-btn
                                icon
                                dark
                                @click="signAndReq = false"
                            >
                                <v-icon>mdi-close</v-icon>
                            </v-btn>
                        </v-card-title>
                            <v-form @submit.prevent="signDocAndReq" v-bind="isValid" ref="form">
                                <v-container>
                                        <v-text-field
                                            v-model="password"
                                            prepend-icon="lock"
                                            label="Certificate Password"
                                            type="password"
                                            
                                            required
                                        ></v-text-field>
                                </v-container>
                                <v-card-actions>
                                    <v-spacer></v-spacer>
                                    <v-btn                                     
                                        class="mr-4"
                                        color="#C85250"
                                        
                                        type="submit"
                                        dark
                                    >
                                    Confirm
                                    </v-btn>
                                </v-card-actions>
                            </v-form>
                    </v-card>
                </v-dialog>
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
                
                
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12" sm="6" md="8" v-if="(document.status=='Original Document')||(document.status=='Original Document (self signed)')||(document.status=='Original Document (Sign Requested)')">
                <vue-pdf-app style="height:80vh;"
                :pdf=document.file_url
                :config="config"
                >
                </vue-pdf-app>
               
            </v-col>
            <v-col cols="12" sm="6" md="8" v-else-if="(document.status=='Self Signed')">
                <vue-pdf-app style="height:80vh;"
                :pdf=document.signed_url
                :config="config"
                >
                </vue-pdf-app>
                
            </v-col>
            <v-col cols="12" sm="6" md="8" v-else-if="(this.$route.params.id.search('getreceive')==0)&&(this.document.doc_url.signed_url!='')">
                <vue-pdf-app style="height:80vh;"
                :pdf=document.doc_url.signed_url
                :config="config"
                >
                </vue-pdf-app>
                
            </v-col>
            <v-col cols="12" sm="6" md="8" v-else-if="(this.document.doc_url.signed_url=='')">
                <vue-pdf-app style="height:80vh;"
                :pdf=document.doc_url.original_file.file_url
                :config="config"
                >
                </vue-pdf-app>
            </v-col>
            
            <v-col cols="6" md="4" v-if="(document.status!='Original Document')&&(document.status!='Original Document (self signed)')&&(document.status!='Original Document (Sign Requested)')&&(this.document.doc_url.signed_url!='')">
                <v-card class="elevation-12">
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
        </v-row>
      
    </v-container>
</template>

<script>
import VuePdfApp from "vue-pdf-app";
// import this to use default icons for buttons
import "vue-pdf-app/dist/icons/main.css";
import axios from 'axios'
import Web3 from 'web3'
import sign from '/build/contracts/sign.json'
import swal from 'sweetalert';

export default {  
    data :()=>({
        links:[
            {icon: 'drive_file_rename_outline', text:'Request Sign', route: ''},
            {icon: 'download', text:'Download', route: ''},
        ],
        testURL:"https://ipfs.infura.io/ipfs/QmbFy4kqWYz9kKJS5CtiqnRoQGk16GDA3bo5KajnGKPHLe",
        dialog: false,
        reqSign: false,
        otherSign: false,
        selfSign:false,
        signAndReq:false,
        loading:false,
        url:'',
        slug:'',
        hash:'',
        thisHash:'',
        reqSignerEmail:'',
        document:[],
        selfSignDocument:[],
        documentVal:null,
        errors:"",
        signer:[],
        selfSigner:[],
        reqSigner:[],
        tmpDATA:null,
        len :null,
        signReq:false,
        tmpId:'',
        userId:'',
        config : {
            sidebar: false,
            secondaryToolbar: false,
            toolbar : {
                toolbarViewerRight: {
                    
                    openFile: false,
                    print: false,
                    viewBookmark: false,
                },
            }
        },
        headers: [
           
            {value: 'first_name'},
            {value: 'last_name'},
            {value: 'email' },
            {value: 'actions'},
        ],
        recipients:[
            {
                first_name:'ashimos',
                email:'ashtsaqofi@gmail.com'
            }
        ],
        
    }),
    components: {
        VuePdfApp
    },
    
    methods: {
        suksesAlert() {
            swal({
            icon: "success",
            title: "Succesfully",
            text: "Document was Signed",
            button: "Confirm",
            })
         },
        errorAlert() {
            swal({
            icon: "error",
            title: "Erros",
            text: "an error occurred while signing the document",
            button: "Confirm",
            })
            this.loading=false
         },
        selfSignDoc(){
            this.loading = true
            const data = {
                "password":this.password,
                "file_url":this.document.file_url,
                "key_url":"https://ipfs.infura.io/ipfs/"+localStorage.getItem('key_url'),
                "pem_url":"https://ipfs.infura.io/ipfs/"+localStorage.getItem('cert_url'),
            }
            axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
            axios
                .post("http://localhost:8000/api/documents/selfsign", data)
                .then(response => {
                    this.dialog= false
                    this.selfSign= false
                    this.url = response.data.url
                    this.hash = response.data.hash
                    this.updateDoc()
                    this.addSigner()   
                    this.selfSign = false
                    // console.log(response)   
                })
                .catch(error => {
                    this.errorAlert()
                    // this.errors=error.response.data.detail
                })
        },

        signDocAndReq(){
            this.loading = true
            const data = {
                "password":this.password,
                "file_url":this.document.file_url,
                "key_url":"https://ipfs.infura.io/ipfs/"+localStorage.getItem('key_url'),
                "pem_url":"https://ipfs.infura.io/ipfs/"+localStorage.getItem('cert_url'),
            }
            axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')

            axios
                .post("http://localhost:8000/api/documents/selfsign", data)
                .then(response => {
                    this.dialog= false
                    this.reqSign= false
                    this.signAndReq= false
                    this.url = response.data.url
                    this.hash = response.data.hash
                    this.updateSingAndReqDoc()
                    this.addSigner()   
                    // console.log(response)   
                })
        },
        
        signRequestedDoc(){
            this.loading = true
            let data = {
                "password":this.password,
                "file_url":this.document.doc_url.signed_url,
                "key_url":"https://ipfs.infura.io/ipfs/"+localStorage.getItem('key_url'),
                "pem_url":"https://ipfs.infura.io/ipfs/"+localStorage.getItem('cert_url'),
                "id":this.document.id,
            }
            if(this.document.doc_url.signed_url==''){
                data = {
                    "password":this.password,
                    "file_url":this.document.doc_url.original_file.file_url,
                    "key_url":"https://ipfs.infura.io/ipfs/"+localStorage.getItem('key_url'),
                    "pem_url":"https://ipfs.infura.io/ipfs/"+localStorage.getItem('cert_url'),
                    "id":this.document.id,
                }
            }
       
            axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')

            axios
                .post("http://localhost:8000/api/documents/signdoc", data)
                .then(response => {
                    
                    this.signReq= false
                    
                    this.url = response.data.url
                    this.hash = response.data.hash
                    this.updateRequestedDoc()
                    this.addSignRequested()   
                    // console.log(response)   
                })
        },

        async addSigner(){
            web3 = window.web3
            const accounts = await web3.eth.getAccounts()
            const networkId = await web3.eth.net.getId()
            const networkData = sign.networks[networkId]
            // console.log(networkData)
            if(networkData) {
                const abi = sign.abi
                const address = networkData.address
                const contract = new web3.eth.Contract(abi,address)
                // console.log(contract)
                const addSigner = await contract.methods.addSigner(this.document.id,localStorage.getItem('email'),localStorage.getItem('first_name'),localStorage.getItem('last_name'),this.url,this.hash).send({from : accounts.toString()}).then((r)=>{
                    this.loading=false
                    this.suksesAlert()
                })
                // const addSigner = await contract.methods.addSigner(10,'email','first_name','last_name',"www.com","dasasfgasd").send({from : accounts.toString()}).then((r)=>{
                //     console.log(r)
                // })
                console.log(addSigner)
            } else {
            window.alert('Smart contract not deployed to detected network.')
            }
        },
        async addSignRequested(){
            web3 = window.web3
            const accounts = await web3.eth.getAccounts()
            const networkId = await web3.eth.net.getId()
            const networkData = sign.networks[networkId]
            // console.log(networkData)
            if(networkData) {
                const abi = sign.abi
                const address = networkData.address
                const contract = new web3.eth.Contract(abi,address)
                // console.log(contract)
                const addSigner = await contract.methods.addSigner(this.document.doc_url.original_file.id,localStorage.getItem('email'),localStorage.getItem('first_name'),localStorage.getItem('last_name'),this.url,this.hash).send({from : accounts.toString()}).then((r)=>{
                    this.loading=false
                    this.suksesAlert()
                })
                // const addSigner = await contract.methods.addSigner(10,'email','first_name','last_name',"www.com","dasasfgasd").send({from : accounts.toString()}).then((r)=>{
                //     console.log(r)
                // })
                console.log(addSigner)
            } else {
            window.alert('Smart contract not deployed to detected network.')
            }
        },
        updateDoc(){
            let data = {
                "file_name": this.document.file_name,
                "size": this.document.size,
                "status": "Self Signed",
                "file_url": this.document.file_url,
                "signed_url": "https://ipfs.infura.io/ipfs/"+this.url,
                "ori_id": this.document.id,
            }
            axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
            axios
                .post("http://localhost:8000/api/documents/selfsigndoc", data)
                .then(response=>{
                    // console.log(response)
                })
            data = {
                "file_name": this.document.file_name,
                "size": this.document.size,
                "status": "Original Document (self signed)",
                "file_url": this.document.file_url,
            }
            // console.log (data)
            axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
            axios
                .put(`http://localhost:8000/api/documents/${this.document.id}`, data)
                .then(response=>{
                    // console.log(response)
                })

            data = {
                "doc_id": this.document.id,
                "hash": this.hash
            }
            axios
                .post("http://localhost:8000/api/documents/hashlist/", data)
                .then(response=>{
                    // console.log(response)
                })
            
        },
        updateSingAndReqDoc(){
            let data = {
                "signed_url": "https://ipfs.infura.io/ipfs/"+this.url,

            }
            axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
            axios
                .put(`http://localhost:8000/api/documents/getsentreq/${this.tmpId}/`, data)
                .then(response=>{
                    // console.log(response)
                })
            data = {
                "file_name": this.document.file_name,
                "size": this.document.size,
                "status": "Original Document (Sign Requested)",
                "file_url": this.document.file_url,
            }
            // console.log (data)
            axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
            axios
                .put(`http://localhost:8000/api/documents/${this.document.id}`, data)
                .then(response=>{
                    // console.log(response)
                })

             data = {
                "doc_id": this.document.id,
                "hash": this.hash
            }
            axios
                .post("http://localhost:8000/api/documents/hashlist/", data)
                .then(response=>{
                    // console.log(response)
                })
            
        },
        async updateRequestedDoc(){
            let data = {
                "signed_url": "https://ipfs.infura.io/ipfs/"+this.url,

            }
            
            axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
            await axios
                .put(`http://localhost:8000/api/documents/reqsign/${this.document.doc_url.id}/`, data)
                .then(response=>{
                    // console.log(response)
                })
            data = {
                "status": "Signed",
            }
            await axios
                .put(`http://localhost:8000/api/documents/getreceive/${this.document.id}/`, data)
                .then(response=>{
                    // console.log(response)
                })
            axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
            await axios
                .get(`/api/documents/getreceive/${this.slug}/`)
                .then(response => {
                    this.document = response.data
                    // console.log(document)
                })
                .catch(error => {
                    console.log(error)
                })

            const len = this.document.doc_url.signer.length
            let isDone= true
            for(let i=0;i<len;i++){
                if(this.document.doc_url.signer[i].status=="Pending"){
                    isDone = false
                }
            }
            if (isDone==true){
                data = {
                    "status": "Signed",
                }
               await axios
                    .put(`http://localhost:8000/api/documents/reqsign/${this.document.doc_url.id}/`, data)
                    .then(response=>{
                        // console.log(response)
                    })
            }

            const pHash = {
                "doc_id": this.document.doc_url.original_file.id,
                "hash": this.hash
            }
            await axios
                .post("http://localhost:8000/api/documents/hashlist/", pHash)
                .then(response=>{
                    // console.log(response)
                })

            
        },
        createOtherSignReq(){
            const  data = {
                "file_name": this.document.file_name,
                "size": this.document.size,
                "status": "Original Document (Sign Requested)",
                "file_url": this.document.file_url,
            }
            axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
            axios
                .put(`http://localhost:8000/api/documents/${this.document.id}`, data)
                .then(response=>{
                    // console.log(response)
                    this.dialog=false
                    this.otherSign=false
                    this.$router.go()
                })
            
        },
        async creteSignReq(){
            axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
            const iduser = localStorage.getItem('id')
            const data = {
                "author":iduser,
                "original_file":this.$route.params.id,
                "signer":[]
            }
            console.log(data)
           await axios
                .post('api/documents/postreqsign/',data)
                .then(response => {
                    this.tmpId=response.data.id
                    this.reqSign =true
                    
                })
                .catch(error => {
                    // console.log(error.response.data.detail)
                    this.errors=error.response.data.detail
                })
        },
        async creteSignReqOther(){
            axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
            const iduser = localStorage.getItem('id')
            const data = {
                "author":iduser,
                "original_file":this.$route.params.id,
                "signer":[]
            }
            console.log(data)
           await axios
                .post('api/documents/postreqsign/',data)
                .then(response => {
                    this.tmpId=response.data.id
                    this.otherSign =true
                    
                })
                .catch(error => {
                    // console.log(error.response.data.detail)
                    this.errors=error.response.data.detail
                })
        },
        deleteSignReq(){
            this.reqSigner=[]
            axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
            axios
                .delete(`api/documents/reqsign/${this.tmpId}/`)
                .then(response => {
                    this.reqSign = false
                    
                })
                .catch(error => {
                    
                })
        },
        deleteSignReqOther(){
            this.reqSigner=[]
            axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
            axios
                .delete(`api/documents/reqsign/${this.tmpId}/`)
                .then(response => {
                    this.otherSign = false
                    
                })
                .catch(error => {
                    
                })
        },
        async deleteSignerReq(id){
            this.reqSigner=[]
            axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
            await axios
                .delete(`api/documents/signreq/${id}/`)
                .then(response => {
                    
                    
                })
                .catch(error => {
                    
                })
            await axios
               .get(`api/documents/reqsign/${this.tmpId}/`)
               .then(response => {
                   
                   this.tmpDATA = response.data
                   this.len = response.data.signer.length
               })
            // console.log(this.tmpDATA.signer)
            for(let i=0;i<this.len;i++){
                const data = {
                    id:this.tmpDATA.signer[i].id,
                    first_name:this.tmpDATA.signer[i].signer.first_name,
                    last_name:this.tmpDATA.signer[i].signer.last_name,
                    email:this.tmpDATA.signer[i].signer.email
                }
                // console.log(data)
                this.reqSigner.push(data)
            }
        },
        async addReqSigner(){
            this.reqSigner=[]
            this.userId=null
            
            axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
            const data = {
                "email":this.reqSignerEmail
            }
            await axios
                .post('api/getid',data)
                .then(response => {
                    this.userId=response.data.id
                    // console.log(this.userId)
                })
                .catch(error => {
                    // console.log(error.response.data.detail)
                    this.errors=error.response.data.detail
                })
            if(this.userId!=null){
                axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
                const data = {
                    "signer":this.userId,
                    "doc_url":this.tmpId,
                    "status":"Pending",
                    
                }
                await axios
                    .post('api/documents/postsignreq/',data)
                    .then(response => {
                        this.reqSignerEmail=''
                        })
                    .catch(error => {
                        
                        this.errors=error.response.data
                    })
                
            }
            await axios
               .get(`api/documents/reqsign/${this.tmpId}/`)
               .then(response => {
                   
                   this.tmpDATA = response.data
                   this.len = response.data.signer.length
               })
            // console.log(this.tmpDATA.signer)
            for(let i=0;i<this.len;i++){
                const data = {
                    id:this.tmpDATA.signer[i].id,
                    first_name:this.tmpDATA.signer[i].signer.first_name,
                    last_name:this.tmpDATA.signer[i].signer.last_name,
                    email:this.tmpDATA.signer[i].signer.email
                }
                // console.log(data)
                this.reqSigner.push(data)
            }

        },
        
        async test(){
            
           console.log(this.signer)
        }
        
    },
    async beforeMount(){
       
        //initializing web3
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

        //get doc data
        let documentID = this.$route.params.id
        
        
        axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
        await axios
            .get(`http://localhost:8000/api/documents/${documentID}`)
            .then(response => {
                   this.document = response.data
                    console.log(this.document)
                   
               })
               .catch(error => {
                   console.log(error)
               })
        
        if((this.document.status!="Original Document")&&(this.document.status!=null)){

            const data = {
                    "file_url":this.document.signed_url
                }
            
            await axios
                .post('api/documents/getdochash',data)
                .then(response => {
                       this.thisHash = response.data.hash
                       console.log(this.thisHash)
                   })
                   .catch(error => {
                       console.log(error)
                   })
        }
        
        //get doc validation
       
        if(this.$route.params.id.search('selfsigndoc')==0){
            this.slug = this.$route.params.id.slice(11)
            axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
            axios.get(`/api/documents/selfsigndoc${this.slug}`)
            .then((response) => {
                    this.document = response.data
                    // console.log("aaaaaaaa",this.document)
            });
            const data = {
                "file_url":this.document.signed_url
            }
            axios.post("api/documents/signvalidation",data)
                .then(response=>{
                    this.documentVal=response.data
                    // console.log(this.documentVal)
                })
        
            
            web3 = window.web3
            // const accounts = await web3.eth.getAccounts()
            const networkId = await web3.eth.net.getId()
            const networkData = sign.networks[networkId]
            if(networkData) {
                const abi = sign.abi
                const address = networkData.address
                
                // console.log(address)
                const contract = new web3.eth.Contract(abi,address)
                const getSigner = await contract.methods.document(this.document.ori_id,0).call()
                
                this.signer.push(getSigner)
                
            } else {
                window.alert('Smart contract not deployed to detected network.')
            }
        }
        
        else if (this.$route.params.id.search('getreceive')==0){
            this.slug = this.$route.params.id.slice(10)
    
            axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
            await axios
                .get(`/api/documents/getreceive/${this.slug}/`)
                .then(response => {
                    this.document = response.data
                    // console.log(document)
                })
                .catch(error => {
                    console.log(error)
                })
            
            let data = {
                    "file_url":this.document.doc_url.signed_url
                }

            if (this.document.doc_url.signed_url==''){
                data = {
                    "file_url":this.document.doc_url.original_file.file_url
                }
            }
            
            await axios
                .post('api/documents/getdochash',data)
                .then(response => {
                       this.thisHash = response.data.hash
                    //    console.log(this.thisHash)
                   })
                   .catch(error => {
                       console.log(error)
                   })
            if (this.document.doc_url.signed_url!=''){
                await axios
                    .post("http://localhost:8000/api/documents/signvalidation",data)
                    .then(response=>{
                        this.documentVal=response.data
                    })

            }

            web3 = window.web3
            // const accounts = await web3.eth.getAccounts()
            const networkId = await web3.eth.net.getId()
            const networkData = sign.networks[networkId]
            if(networkData) {
                const abi = sign.abi
                const address = networkData.address
                
                // console.log(accounts.toString())
                const contract = new web3.eth.Contract(abi,address)
                const countSigner = await contract.methods.countSigner(this.document.doc_url.original_file.id).call()
                for(let i=0;i<countSigner;i++){
                    const getSigner = await contract.methods.document(this.document.doc_url.original_file.id,i).call()
                    this.signer.push(getSigner)
                }
                
                
                
            } else {
                window.alert('Smart contract not deployed to detected network.')
            }
        
        }
        else if (this.$route.params.id.search('getsentreq')==0){
            this.slug = this.$route.params.id.slice(10)
    
            axios.defaults.headers.common['Authorization'] = 'Bearer '+localStorage.getItem('simple_token')
            await axios
                .get(`/api/documents/getsentreq/${this.slug}/`)
                .then(response => {
                    this.document = response.data
                    // console.log(this.slug,response)
                })
                .catch(error => {
                    console.log(error)
                })
            
            let data = {
                    "file_url":this.document.signed_url
                }
            await axios
                .post('api/documents/getdochash',data)
                .then(response => {
                       this.thisHash = response.data.hash
                    //    console.log(this.thisHash)
                   })
                   .catch(error => {
                       console.log(error)
                   })
            
            await axios
                .post("http://localhost:8000/api/documents/signvalidation",data)
                .then(response=>{
                    this.documentVal=response.data
                })

            web3 = window.web3
            // const accounts = await web3.eth.getAccounts()
            const networkId = await web3.eth.net.getId()
            const networkData = sign.networks[networkId]
            if(networkData) {
                const abi = sign.abi
                const address = networkData.address
                
                // console.log(accounts.toString())
                const contract = new web3.eth.Contract(abi,address)
                const countSigner = await contract.methods.countSigner(this.document.original_file.id).call()
                for(let i=0;i<countSigner;i++){
                    const getSigner = await contract.methods.document(this.document.original_file.id,i).call()
                    this.signer.push(getSigner)
                }
                
                
                
            } else {
                window.alert('Smart contract not deployed to detected network.')
            }
            // console.log(this.signer)
        }

        
       
    }
};
</script>