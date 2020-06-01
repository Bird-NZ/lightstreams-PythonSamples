##################
#Balance check
##################

import requests

Account = #'account'
#specify the API URL to connnect to:
url = "https://gateway.sirius.lightstreams.io/wallet/balance"

#or a localnode if running
#url = "http://localhost:9091/wallet/balance"

#add the query string -> the account number in this case:
querystring = {"account": Account}

#call the API
response = requests.request("GET", url, params=querystring)

#Print query status_code
print ("Status code for request is: ", response.status_code)

#create a dict from the response
data = response.json()

#Print the value for key value pair of "balance:value" displaying the wallet balance
print ("Balance for this account is: ",data['balance'])

#create balance as a int
balance = data['balance']
