# -*- coding: utf-8 -*-
import urllib2
import requests
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')  # 提示编码不匹配警告

class DingTalk(object):
    def __init__(self, corp_id, corp_secret):
        self.corp_id = corp_id
        self.crop_secret = corp_secret
        self.token = '13e4b78f00d3baa66564624a2ff4e3ade723b790921d21f4446bed0a4e94cff6'
        self.headers = {'Content-Type': 'application/json;charset=utf-8'}
        self.api_url = "https://oapi.dingtalk.com/robot/send?access_token=%s" % self.token

    def get_access_token(self):
        """
        corp_id和corp_secret是企业的id和secret
        :return: access_token
        """
        url = 'https://oapi.dingtalk.com/gettoken?corpid=%s&corpsecret=%s' % (self.corp_id, self.corp_secret)
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        response_str = response.read()
        response_dict = json.loads(response_str)
        error_code_key = "errcode"
        access_token_key = "access_token"
        if response_dict.has_key(error_code_key) and response_dict[error_code_key] == 0 and response_dict.has_key(access_token_key):
            self.token = response_dict[access_token_key]
        else:
            self.token = ''

    def send_text(self,text):
        json_text = {
            "msgtype": "text",
            "at": {
                "atMobiles": [
                    "13161396617",
                    '13603518488'
                ],
                "isAtAll": False
            },
            "text": {
                "content": text
            }
        }
        print(requests.post(self.api_url, json.dumps(json_text), headers=self.headers).content)

    def send_link(self):
        json_text = {
            "msgtype": "link",
            "link": {"text": "较长河为疏落，变大地为黄金！",
                     "title": "黑猫警长请出动！",
                     "picUrl": "",
                     "messageUrl": "http://10.238.163.131:8889/lab"
                    }
                }
        print(requests.post(self.api_url, json.dumps(json_text), headers=self.headers).content)


if __name__ == '__main__':
    ding = DingTalk(123,123)
    # ding.send_text('流浪地球一号舰队呼叫小焦！！')
    ding.send_link()






