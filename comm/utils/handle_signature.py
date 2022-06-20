from hashlib import sha1
from comm.utils.logger import logger


# 构造签名
def handle_signature(sig):
    # 构造加密前字符串
    # 1.处理业务参数
    middle_list = [sig]  # 列表中存字典
    new_dict = {}  # 新字典存数据
    while middle_list:
        for key, value in middle_list.pop(0).items():
            if isinstance(value, dict):
                # 将这个字典保存到列表a中
                middle_list.append(value)
            elif isinstance(value, list) and isinstance(value[0], dict):
                middle_list.append(value[0])
            elif isinstance(value, int) or isinstance(value, str) or isinstance(value, float):
                # 将key和value保存到新字典中
                new_dict[key] = value
    # 排序
    sort_list = sorted(new_dict.items(), key=lambda item: item[0].upper(), reverse=False)
    # 2.拼接字符串
    ret = ''
    for tuple in sort_list:
        for k in tuple:
            ret += str(k)
    # 拼接前后缀
    sig_string = "key" + ret + "secret"
    logger.info("签名加密前字符串：%s" % sig_string)
    # 构造签名
    # 创建sha1对象
    s1 = sha1()
    # 对s1进行更新
    s1.update(sig_string.encode())
    # 签名加密处理
    result = s1.hexdigest()
    new_result = result.upper()
    logger.info("签名结果：%s" %new_result)
    return new_result