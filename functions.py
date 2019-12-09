import requests
import json
from datetime import datetime


def check_status(json_file):
    for current_json_object in json_file:
        check_container_status(current_json_object)


def check_container_status(json_object):
    response = requests.get(json_object['url'], verify=False)
    if response:
        # print('Success!')
        update_status_fields(json_object, response.status_code)
    else:
        # print('An error has occurred.')
        update_status_fields(json_object, response.status_code)


def update_status_fields(object, status_code):
    object['status']['statusCode'] = status_code
    object['status']['lastChecked'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

