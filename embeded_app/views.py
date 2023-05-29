from django.shortcuts import render
from django.http import HttpResponse

import requests
import json


# Create your views here.
def homepage(request):
    url = "https://dev.vdocipher.com/api/videos/e7cc59d26da7440090daf9918d6d3b26/otp"
    payload = json.dumps({
        "annotate": json.dumps([
            {'type': 'rtext', 'text': 'name', 'alpha': '0.60', 'color': '0xFF0000', 'size': '15', 'interval': '5000'}
        ])
    })
    headers = {
        'Authorization': "Apisecret v68GeMNvpAxjwqaqZOMmF01g5TN2bupmjFge6SlindBqIXtw4quP6srUh5Y4M2Wy",
        'Content-Type': "application/json",
        'Accept': "application/json"

    }
    response = requests.request("POST", url, data=payload, headers=headers)
    json_object = json.loads(response.text)
    print(type(json_object))
    print(response)
    print(response.text)
    url_pb_01 = 'https://player.vdocipher.com/v2/?otp={}&playbackInfo={}'.format(json_object['otp'],
                                                                                 json_object['playbackInfo'])

    #return HttpResponse(response)
    return render(request, 'landing_page.html', {"url": url_pb_01})
    # src="https://player.vdocipher.com/v2/?otp=[[REPLACE_WITH_OTP]]&playbackInfo=
    # print(response.text)
