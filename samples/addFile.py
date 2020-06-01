# -*- coding: utf-8 -*-
"""
Created on Fri May 29 07:24:40 2020

@author: Mat
"""

###########################
#add File
###########################

import requests

Account = #'account'
Password = #'password'
FileLocation = #'file location'

addFile_URL = "https://gateway.sirius.lightstreams.io/storage/add"
#ACLUpdate_URL = 'http://localhost:9091/storage/add'

#create data payload
addFile_payload = {'owner':Account,
                   'password':Password
                   }
#create file payload
addFile_file = {'file': open(FileLocation,'rb')}

#run request
addFile_response = requests.request('POST', addFile_URL,
                            data=addFile_payload,
                            files=addFile_file
                            )
#Return json
addFile_Data = addFile_response.json()


if addFile_response.status_code == 200:
    print("ACL: ",addFile_Data['acl'])
    print("Meta: ",addFile_Data['meta'])
else:
    print (addFile_Data['error']['code'])
    print (addFile_Data['error']['message']) 




