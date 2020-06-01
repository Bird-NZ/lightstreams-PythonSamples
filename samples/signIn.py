# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 16:11:12 2020

@author: Mat
"""

######################
#signin
######################
import requests


signin_URL = "https://gateway.sirius.lightstreams.io/user/signin"
#signinURL = "http://localhost:9091/user/signin"

Account = #'insert account'
Password = #'password'

signin_Querystring = {"account": Account,
               "password": Password}

signin_Response = requests.request("POST",
                                  signin_URL,
                                  json=signin_Querystring)
print (signin_Response.status_code)
signin_Data = signin_Response.json()
