# -*- coding:utf-8 -*-
# @Time    : 2024/8/6
# @Author  : wu xiaowei
# @File    : apiMethod.py
# *************************

import json
import logging
import requests

def post(headers, address,  data=None):
    response = requests.post(url=address,json=data,headers=headers)
    try:
        if response.status_code != 200:
            return response.status_code, response.text
        else:
            return response.status_code, response.json()
    except json.decoder.JSONDecodeError:
        return response.status_code, None
    except Exception as e:
        logging.exception('ERROR')
        logging.error(e)
        raise

def put(headers, address, data):
    response = requests.put(url=address,
                            json=data,
                            headers=headers)
    try:
        return response.status_code, response.json()
    except json.decoder.JSONDecodeError:
        return response.status_code, None
    except Exception as e:
        logging.exception('ERROR')
        logging.error(e)
        raise