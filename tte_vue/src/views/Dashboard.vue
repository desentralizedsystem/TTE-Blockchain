<template>
  <v-container>
    
      
        <v-row>
          <v-card
            class="ma-5"
            max-width="344"
            outlined
            elevation="10"
            
          >
            <v-list-item three-line v-if="isVerified=='true'">
              <v-list-item-content>
                <div class="text-overline mb-4">
                  Account Status
                </div>
                <v-list-item-title class="text-h5 mb-1">
                  Verified
                </v-list-item-title>
              </v-list-item-content>
        
              <v-list-item-avatar tile size="80" >
                <v-sheet color="green" width="80" height="80" elevation="10">
                      <v-icon dark large>verified_user</v-icon>
                </v-sheet>
              </v-list-item-avatar>
            </v-list-item>
            <v-list-item three-line v-else-if="isVerified=='false'">
              <v-list-item-content>
                <div class="text-overline mb-4">
                  Account Status
                </div>
                <v-list-item-title class="text-h5 mb-1">
                  Unverified
                </v-list-item-title>
              </v-list-item-content>
        
              <v-list-item-avatar tile size="80" >
                <v-sheet color="red" width="80" height="80" elevation="10">
                      <v-icon dark large>mdi-close-circle</v-icon>
                </v-sheet>
              </v-list-item-avatar>
            </v-list-item>
          </v-card>
          <v-card
            class="ma-5"
            max-width="350"
            outlined
            elevation="10"
          >
            <v-list-item three-line v-if="digCert">
              <v-list-item-content>
                <div class="text-overline mb-4">
                  Digital Certificate Status
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
              <v-list-item-content>
                <div class="text-overline mb-4">
                  Digital Certificate Status
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
        </v-row>
        <v-row>
          <v-card
            class="ma-5"
            max-width="344"
            outlined
            elevation="10"
          >
            <v-list-item three-line>
              <v-list-item-content>
                <div class="text-overline mb-4">
                  Total Documents
                </div>
                <v-list-item-title class="text-h5 mb-1">
                  100
                </v-list-item-title>
              </v-list-item-content>
        
              <v-list-item-avatar tile size="80">
                <v-sheet color="blue" width="80" height="80" elevation="10">
                      <v-icon dark large>insert_drive_file</v-icon>
                </v-sheet>
              </v-list-item-avatar>
            </v-list-item>
          </v-card>
          <v-card
            class="ma-5"
            max-width="344"
            outlined
            elevation="10"
          >
            <v-list-item three-line>
              <v-list-item-content>
                <div class="text-overline mb-4">
                  Signature Request
                </div>
                <v-list-item-title class="text-h5 mb-1">
                  100
                </v-list-item-title>
              </v-list-item-content>
        
              <v-list-item-avatar tile size="80">
                <v-sheet color="blue" width="80" height="80" elevation="10">
                      <v-icon dark large>drive_file_rename_outline</v-icon>
                </v-sheet>
              </v-list-item-avatar>
            </v-list-item>
          </v-card>
          <v-card
            class="ma-5"
            max-width="344"
            outlined
            elevation="10"
          >
            <v-list-item three-line>
              <v-list-item-content>
                <div class="text-overline mb-4">
                  Signed Documents
                </div>
                <v-list-item-title class="text-h5 mb-1">
                  100
                </v-list-item-title>
              </v-list-item-content>
        
              <v-list-item-avatar tile size="80">
                <v-sheet color="blue" width="80" height="80" elevation="10">
                      <v-icon dark large>domain_verification</v-icon>
                </v-sheet>
              </v-list-item-avatar>
            </v-list-item>
          </v-card>
        </v-row> 
      
      
    
  </v-container>
</template>

<script>
export default {
  data :()=>({
    isVerified:localStorage.getItem('is_verified'),
    digCert:localStorage.getItem('cert_url')
  }),

  
  
}
</script>