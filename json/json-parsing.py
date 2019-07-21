import json
from urllib.request import urlopen

def getCountry(ipAdress):
    response = urlopen('http://api.ipstack.com/'+ipAdress+'?access_key=9beb00225a90e7fffb5fafc91571113d').read().decode('utf-8')
    responseJson= json.loads(response)
    return responseJson
    # return responseJson.get("country_code")

print(getCountry("83.86.78.89"))