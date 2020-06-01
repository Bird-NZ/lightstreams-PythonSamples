# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:58:40 2020

@author: OEM
"""


#################
#Transfer
#################
import requests

transferURL = "https://gateway.sirius.lightstreams.io/wallet/transfer"
#transferURL = "http://localhost:9091/wallet/transfer"

From = #<from address>
Password = #<password>
To = #<to address>
Amount = #<amout of wei>

transferQuerystring = {
    "from": From,
    "password": Password,
    "to": To,
    "amount_wei": Amount
    }

transferResponse = requests.request("POST", 
                                  transferURL, 
                                  json=transferQuerystring)

transferResponseData = transferResponse.json()

print(transferResponse.status_code)
