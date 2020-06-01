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
Password = #'password to owners account'

#get token for account
revokePublicURL = "https://gateway.sirius.lightstreams.io/acl/revoke-public"

revokePublic_Querystring = {"acl": Acl,
                    "owner": Owner,
                    "password": Password}

revokePublic_Response = requests.request("POST", 
                                  revokePublicURL, 
                                  json=revokePublic_Querystring)

print ('Get account token status code: ', revokePublic_Response.status_code)

streamData = revokePublic_Response.json()

if revokePublic_Response.status_code != 200:
    print(streamData['error']['code'])
    print(streamData['error']['message'])
else:
    print('Is public access revoked? :', streamData['is_revoked'])



