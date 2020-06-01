# -*- coding: utf-8 -*-
"""
Created on Fri May 29 07:32:26 2020

@author: Mat
"""

###########################
#Update File
###########################

import requests

Meta = #<mata address>
Owner = #<owner address>
FileLocation = #<file location>


updateFile_URL = "https://gateway.sirius.lightstreams.io/storage/update"
#updateFile_URL = 'http://localhost:9091/storage/update'

updateFile_payload = {'owner':Owner,
                      'meta':Meta
                      }
updateFile_file = {'file': open(FileLocation,'rb')}

updateFile_response = requests.request('POST', updateFile_URL,
                            data=updateFile_payload,
                            files=updateFile_file
                            )

print(updateFile_response.status_code)
updateFileData = updateFile_response.json()