# -*- coding: utf-8 -*-
"""
Created on Fri May 29 07:36:29 2020

@author: Mat
"""

#######################
#Display Meta
#######################

import requests

Meta = #<meta address>

#set URL
fetchMeta_URL = "https://gateway.sirius.lightstreams.io/storage/meta"
#fetchMeta_URL = "http://localhost:9091/storage/meta"

#set querystring
fetchMeta_Querystring = {"meta": Meta}

#Post 
fetchMeta_Response = requests.request("GET",
                                    fetchMeta_URL,
                                    params=fetchMeta_Querystring)
#check status of POST
print(fetchMeta_Response.status_code)

#format with Json() into dict
fetchMeta_Data = fetchMeta_Response.json()

