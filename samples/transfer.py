# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:58:40 2020

@author: Mat
"""

#################
#Transfer funds
#################
import requests

transfer_URL = "https://gateway.sirius.lightstreams.io/wallet/transfer"
#transferURL = "http://localhost:9091/wallet/transfer"

From = #<from address>
Password = #<password>
To = #<to address>
Amount = #<amout of wei>

transfer_Querystring = {"from": From,
                        "password": Password,
                        "to": To,
                        "amount_wei": Amount}

transfer_Response = requests.request("POST", 
                                  transfer_URL, 
                                  json=transfer_Querystring)

transfer_Data = transfer_Response.json()

print(transfer_Response.status_code)
