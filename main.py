
# encoding = utf-8

import os
import sys
import time
import datetime

import requests
import json


def validate_input(helper, definition):
    pass

def collect_events(helper, ew):
   
   
    opt_base_url = helper.get_arg('base_url')
    opt_token = helper.get_arg('token')

    
    headers = {'Authorization': f'Bearer {opt_token}','Content-Type': 'application/x-www-form-urlencoded'}

    data = 'scope=applied-permissions/user'

    response = requests.post(opt_base_url, headers=headers, data=data,verify=False)

    #response = requests.post(opt_base_url, headers=None,data=None, verify=False)

    r_json = response.json()

    r_status = response.status_code
    if r_status != 200:
        response.raise_for_status()

    if r_json:

        res = helper.new_event(json.dumps(r_json["tokens"][0]), index=helper.get_output_index(), source=None, sourcetype=None, done=True, unbroken=True)

        ew.write_event(res)
