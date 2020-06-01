# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 10:10:37 2020

@author: Mat
"""

##################
#Grant permissions
##################
import requests


Acl = #'File ACL'
Owner = #'account address of file's owner'
Password = #"password to owners account"
To = #'account address to be granted permissions'
Permissions = #'permission type' "read" "write" "admin" "noaccess"

#get token for account
grant_URL = "https://gateway.sirius.lightstreams.io/acl/grant"
#signinURL = "http://localhost:9091/user/signin"

grant_Querystring = {"acl": Acl,
                    "owner": Owner,
                    "password": Password,
                    "to": To,
                    "permission": Permissions}

grant_Response = requests.request("POST", 
                                  grant_URL, 
                                  json=grant_Querystring)

print ('Grant response code: ',grant_Response.status_code)

grant_Response_Data = grant_Response.json()
if grant_Response.status_code != 200:
    print(grant_Response_Data['error']['code'])
    print(grant_Response_Data['error']['message'])
else:
    print('grant response: ', grant_Response_Data['is_granted'])
