import os
# from urllib.request import urlopen
# import re as r
import public_ip as ip


from django.shortcuts import render
from django.http import HttpResponse

import requests
import json
import socket
from ipware import get_client_ip

# Create your views here.
def homepage(request):
    system_ip = ip.get()
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)


    print("Your Computer Name is:" + hostname)
    print("Your Computer IP Address is:" + IPAddr)
    url = "https://dev.vdocipher.com/api/videos/e7cc59d26da7440090daf9918d6d3b26/otp"
    water_mark = '\u00A9'
    water_mark += 'copyright by Firmbond K.K'
    print(water_mark)
    payload = json.dumps({
        "annotate": json.dumps([
            {'type': 'rtext', 'text': water_mark, 'alpha': '0.60', 'color': '0xFF0000', 'size': '15', 'interval': '5000'},
            {'type': 'rtext', 'text': 'Private-IP:'+IPAddr , 'alpha': '0.60', 'color': '0xFF0000', 'size': '15', 'interval': '5000'},
            {'type': 'rtext', 'text': 'Public-IP:'+system_ip , 'alpha': '0.60', 'color': '0xFF0000', 'size': '15', 'interval': '5000'},
            {'type': 'rtext', 'text': 'User Name:' + hostname, 'alpha': '0.60', 'color': '0xFF0000', 'size': '15', 'interval': '5000'}
        ])
    })
    headers = {
        'Authorization': "Apisecret v68GeMNvpAxjwqaqZOMmF01g5TN2bupmjFge6SlindBqIXtw4quP6srUh5Y4M2Wy",
        'Content-Type': "application/json",
        'Accept': "application/json"

    }
    response = requests.request("POST", url, data=payload, headers=headers)
    json_object = json.loads(response.text)

    url_pb_01 = 'https://player.vdocipher.com/v2/?otp={}&playbackInfo={}'.format(json_object['otp'],
                                                                                 json_object['playbackInfo'])

    #return HttpResponse(response)
    print(os.system('ipconfig'))

    return render(request, 'landing_page.html', {"url": url_pb_01})
    # src="https://player.vdocipher.com/v2/?otp=[[REPLACE_WITH_OTP]]&playbackInfo=
    # print(response.text)

