######################
#signUp
######################
import requests


signupURL = "https://gateway.sirius.lightstreams.io/user/signup"
#signupURL = "http://192.168.1.7:9091/user/signup"

Password = #<password>

signupQuerystring = {"password": Password}
signupResponse = requests.request("POST",
                                  signupURL,
                                  json=signupQuerystring)

print (signupResponse.status_code)
signupData = signupResponse.json()
print (signupData['account'])
