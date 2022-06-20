from comm.utils.Req import Req
from config import *


# 接口文档提供路径
path = '/doc/getBaseInfo'
# 业务参数为文档中的请求参数
business_json = {
    'groupID': "11157",
    "shopID":"76312057"
}


getBaseInfo = Req(DevConfig.www_url_root)
getBaseInfo.send(path, business_json)
