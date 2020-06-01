##################
#Balance check
##################

import requests

Account = '0x2B6977f493463E49C23340875C10df87B34caF32'
#'account'

#specify the API URL to connnect to:
balance_URL = "https://gateway.sirius.lightstreams.io/wallet/balance"
#or a localnode if running
#url = "http://localhost:9091/wallet/balance"

#add the query string -> the account number in this case:
balance_querystring = {"account": Account}

#call the API
balance_response = requests.request("GET", balance_URL, 
                                    params=balance_querystring)

#Print query status_code
print ("Status code for request is: ", balance_response.status_code)

#create a dict from the response
balance_data = balance_response.json()

#Print the value for key value pair of "balance:value" displaying the wallet balance
print ("Balance for this account is: ", balance_data['balance'])


