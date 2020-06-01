# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 10:10:37 2020

@author: Mat
"""

##################
#Grant permissions
##################
import requests
#import sys

'''
ACL:  0xF15aCA55A3D8E14f59e10CAd6f93bC29Bf2710ff
Meta:  QmUhMoFt8cJDzJwXoEg34WczprtF5XJJ5ABJMcf46LjC6R
Main Acc: 0x2B6977f493463E49C23340875C10df87B34caF32
2nd Acc: 0x2ef9Cd304aAe11e9720cfD4978D155a121d17fDB
'''

Acl = #'File ACL'
Owner = #'account address of file's owner'
Password = #"password to owners account"
To = #'account address to be granted permissions'
Permissions = #'permission type' "read" "write" "admin" "noaccess"

#get token for account
grantURL = "https://gateway.sirius.lightstreams.io/acl/grant"
#signinURL = "http://localhost:9091/user/signin"

grantQuerystring = {"acl": Acl,
                    "owner": Owner,
                    "password": Password,
                    "to": To,
                    "permission": Permissions}

grant_Response = requests.request("POST", 
                                  grantURL, 
                                  json=grantQuerystring)

print ('Grant response code: ',grant_Response.status_code)

grant_Response_Data = grant_Response.json()
if grant_Response.status_code != 200:
    print(grant_Response_Data['error']['code'])
    print(grant_Response_Data['error']['message'])
else:
    print('grant response: ', grant_Response_Data['is_granted'])
