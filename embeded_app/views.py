# import public_ip as ip
from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import socket
import getpass



# Create your views here.
def homepage(request):
    # system_ip = ip.get()
    #{'type': 'rtext', 'text': 'Public-IP:' + system_ip, 'alpha': '0.60', 'color': '0xFF0000', 'size': '15','interval': '5000'},
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print(socket.gethostbyaddr(IPAddr))
    #{'type': 'rtext', 'text': 'User Name:' + hostname, 'alpha': '0.60', 'color': '0xFF0000', 'size': '15', 'interval': '5000'}
    #{'type': 'rtext', 'text': 'Private-IP:' + IPAddr, 'alpha': '0.60', 'color': '0xFF0000', 'size': '15','interval': '5000'},
    username = getpass.getuser()
    print(username)
    url = "https://dev.vdocipher.com/api/videos/e7cc59d26da7440090daf9918d6d3b26/otp"
    water_mark = '\u00A9'
    water_mark += 'copyright by Firmbond K.K'
    print(water_mark, hostname)
    payload = json.dumps({
        "annotate": json.dumps([
            {'type': 'rtext', 'text': water_mark, 'alpha': '0.60', 'color': '0xFF0000', 'size': '15',
             'interval': '5000'},
            {'type': 'text', 'text': 'Private-IP:' + IPAddr, 'alpha': '0.30', 'x': '40', 'y': '130',
             'color': '0xFF0000', 'size': '13'}



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

    return render(request, 'landing_page.html', {"url": url_pb_01})
