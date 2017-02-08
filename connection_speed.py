#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests
import speedtest

requests.packages.urllib3.disable_warnings()

speedtester = speedtest.Speedtest()
best_server = speedtester.get_best_server()

DL = speedtester.download()
UL = speedtester.upload()

dl_rate = "DL {:.2f}".format(DL / 1000 / 1000)
dl_icon = "i402"
ul_rate = "UL {:.2f}".format(UL / 1000 / 1000)
ul_icon = "i120"

access_token = "YOUR ACCESS TOKEN"
url = "ENDPOINT_URL"

headers = {'Accept': 'application/json', 'Cache-Control': 'no-cache', 'X-Access-Token': access_token}

data = {
    'frames': [
        {
            'index': 0,
            'text': dl_rate,
            'icon': dl_icon
        },
        {
            'index': 1,
            'text': ul_rate,
            'icon': ul_icon
        }
    ]
}

r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
