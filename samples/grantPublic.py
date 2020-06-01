# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 16:11:12 2020

@author: Mat
"""

##################
#grantPublic
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
Password =  #'password to owners account'

#get token for account
grantPublicURL = "https://gateway.sirius.lightstreams.io/acl/grant-public"

grantPublic_Querystring = {"acl": Acl,
                    "owner": Owner,
                    "password": Password}

grantPublic_Response = requests.request("POST", 
                                  grantPublicURL, 
                                  json=grantPublic_Querystring)

print ('Get account token status code: ', grantPublic_Response.status_code)

streamData = grantPublic_Response.json()

if grantPublic_Response.status_code != 200:
    print(streamData['error']['code'])
    print(streamData['error']['message'])
else:
    print('Is public access granted? :', streamData['is_granted'])



