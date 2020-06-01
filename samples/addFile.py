# -*- coding: utf-8 -*-
"""
Created on Fri May 29 07:24:40 2020

@author: Mat
"""
#Account = "0x2B6977f493463E49C23340875C10df87B34caF32"
#FileLocation = "C:/temp/fileToUpload2.txt"

###########################
#add File
###########################

import requests
# main acc 0x2B6977f493463E49C23340875C10df87B34caF32
# 
Account = #'account'
Password = #'password'
FileLocation = #'file location'

addFile_URL = "https://gateway.sirius.lightstreams.io/storage/add"
#ACLUpdate_URL = 'http://localhost:9091/storage/add'


addFile_payload = {'owner':Account,
                   'password':Password
                   }

addFile_file = {'file': open(FileLocation,'rb')}

addFile_response = requests.request('POST', addFile_URL,
                            data=addFile_payload,
                            files=addFile_file
                            )

addFile_Data = addFile_response.json()
if addFile_response.status_code == 200:
    print("ACL: ",addFile_Data['acl'])
    print("Meta: ",addFile_Data['meta'])
else:
    print (addFile_Data['error']['code'])
    print (addFile_Data['error']['message']) 




