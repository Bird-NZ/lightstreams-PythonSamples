######################
#signUp
######################
import requests


signup_URL = "https://gateway.sirius.lightstreams.io/user/signup"
#signupURL = "http://localhost:9091/user/signup"

Password = #<password>

signup_Querystring = {"password": Password}
signup_Response = requests.request("POST",
                                  signup_URL,
                                  json=signup_Querystring)

print (signup_Response.status_code)
signup_Data = signup_Response.json()
print (signup_Data['account'])
