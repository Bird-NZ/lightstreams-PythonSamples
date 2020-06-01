######################
#signin
######################
import requests


signinURL = "https://gateway.sirius.lightstreams.io/user/signin"
#signinURL = "http://localhost:9091/user/signin"

Account = #<insert account>
Password = #<password>

signinQuerystring = {"account": Account,
               "password": Password}

signinResponse = requests.request("POST",
                                  signinURL,
                                  json=signinQuerystring)
print (signinResponse.status_code)
signinData = signinResponse.json()
