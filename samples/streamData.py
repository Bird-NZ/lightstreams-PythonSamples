# -*- coding: utf-8 -*-
"""
Created on Sat May 30 17:43:21 2020

@author: Mat
"""

##################
#Stream data
##################
import requests
import sys

Account = #"account"
Password = #'password to owners account'
Meta = #"Meta address"

#get token for account
signin_URL = "https://gateway.sirius.lightstreams.io/user/signin"
#signinURL = "http://localhost:9091/user/signin"

signin_Querystring = {"account":Account,
                     "password": Password}
signin_Response = requests.request("POST", 
                                  signin_URL, 
                                  json=signin_Querystring)

print ('Get account token status code: ',signin_Response.status_code)

getToken = signin_Response.json()

if signin_Response.status_code == 200:
    Token = getToken['token']
elif signin_Response.status_code != 200:
    print(getToken['error']['code'])
    print(getToken['error']['message'])
    sys.exit("No token able to be collected")


#use token to stream data from Meta address
streamData_URL = 'https://gateway.sirius.lightstreams.io/storage/stream'
#streamData_URL = 'http://localhost:9091/storage/stream'


streamData_Querystring = {'meta': Meta,
                          'token': Token}
streamData_Response = requests.request('GET',
                                       streamData_URL,
                                       params=streamData_Querystring)

print('Get stream status code: ', streamData_Response.status_code)
if streamData_Response.status_code != 200:
    streamData = streamData_Response.json()
    print(streamData['error']['code'])
    print(streamData['error']['message'])
else:
    streamData = streamData_Response.text
    print(streamData)



