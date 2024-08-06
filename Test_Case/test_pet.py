#-*- coding:utf-8 -*-
# @Time    : 2024/8/6
# @Author  : Wu Xiaowei
# @File    : test_pet.py
# ****************************
from Common.Check_Result import check_result
from Common.Config import Base_url
from Web_api.Rest_api import post, put

headers = {'Content-Type':'application/json','accept':'application/json'}

class TestCase:
    def test_pet_update(self):
        test_data = {
            "id": 0,
            "category": {
                "id": 0,
                "name": "Pomeranian"
            },
            "name": "kurikur",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "Super Cute"
                }
            ],
            "status": "available"
        }
        api = Base_url + '/pet'
        code,result = put(headers= headers,data= test_data, address= api)
        expected_result = {'id': '@ignored',
                           'category': {'id': 0, 'name': 'Pomeranian'},
                           'name': 'kurikur',
                           'photoUrls': ['string'],
                           'tags': [{'id': 0, 'name': 'Super Cute'}],
                           'status': 'available'}

        check_result(expected_result, code, result)

    def test_store(self):
        test_data =  {
            "id": 0,
            "petId": 9223372036854743000,
            "quantity": 0,
            "shipDate": "2024-08-06T14:00:48.983Z",
            "status": "placed",
            "complete": True
        }
        api = Base_url + '/store/order'
        print(api)
        code, result = post(headers=headers, address=api, data=test_data)
        expected_result = {
            "id": '@ignored',
            "petId": 9223372036854743000,
            "quantity": 0,
            "shipDate": "@ignored",
            "status": "placed",
            "complete": True
        }
        check_result(expected_result,code, result)