import requests
import json
from datetime import datetime


def check_status(json_file):
    for current_json_object in json_file:
        check_container_status(current_json_object)


def check_container_status(json_object):
    try:
        # successful request
        response = requests.get(json_object['url'], verify=False)
        update_status_fields(json_object, response.status_code)
    except requests.exceptions.ConnectionError as error:
        # failed request
        update_status_fields(json_object, "999")


def update_status_fields(object, status_code):
    object['status']['statusCode'] = status_code
    object['status']['lastChecked'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

