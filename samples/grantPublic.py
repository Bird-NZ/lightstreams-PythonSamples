# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 16:11:12 2020

@author: Mat
"""

##################
#grantPublic
##################
import requests

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



