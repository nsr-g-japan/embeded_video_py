from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
def homepage(request):


    url = "https://dev.vdocipher.com/api/videos/e7cc59d26da7440090daf9918d6d3b26/otp"

    payloadStr = json.dumps({'ttl': 300})
    headers = {
        'Authorization': "Apisecret v68GeMNvpAxjwqaqZOMmF01g5TN2bupmjFge6SlindBqIXtw4quP6srUh5Y4M2Wy",
        'Content-Type': "application/json",
        'Accept': "application/json"
    }

    response = requests.request("POST", url, data=payloadStr, headers=headers)
    json_object = json.loads(response.text)
    print(type(json_object))
    print(response.text)
    return render(request, 'landing_page.html', json_object)

    #print(response.text)