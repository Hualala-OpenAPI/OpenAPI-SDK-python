import requests
import time
from comm.utils import handle_requestbody, handle_signature
import uuid
from config import *
from comm.utils.logger import logger

class Req(object):
    def __init__(self,url_base):
        self.www_url_base = url_base


    def send(self,path,business_json):
        # 生成时间戳
        timestamp = int(round((time.time()) * 1000))
        # 生成签名签名需要的参数
        sig = dict()
        sig["timestamp"] = timestamp
        sig['version'] = DevConfig.version
        sig['appKey'] = DevConfig.appKey
        sig['appSecret'] = DevConfig.app_Secret
        sig["business_json"] = business_json
        # 生成签名
        signatuer =  handle_signature.handle_signature(sig)

        # 构造请求体
        datas = dict()
        datas['signature'] =signatuer
        # 生成requestBody
        requestBody = handle_requestbody.get_encrypt(business_json, DevConfig.app_Secret)
        datas['requestBody'] = ''.join(requestBody.split('\n'))
        # 当前服务器毫秒级时间戳
        datas['timestamp'] = timestamp
        # 版本号
        datas['version'] = DevConfig.version
        # appKey
        datas['appKey'] = DevConfig.appKey

        # 构造请求头
        name = 'test_name'
        namespace = uuid.NAMESPACE_URL
        traceID = str(uuid.uuid5(uuid.NAMESPACE_DNS, '{timestamp}'))
        url = self.www_url_base + path
        # 发送请求
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'groupID': DevConfig.groupID,'shopID': DevConfig.shopID,'traceID': traceID}
        response = requests.post(url, data=datas, headers=headers)
        logger.info("请求url：%s" % url)
        logger.info("请求头：%s" % headers)
        logger.info("请求体：%s" % datas)
        logger.info("接口返回结果：%s" %response.json())