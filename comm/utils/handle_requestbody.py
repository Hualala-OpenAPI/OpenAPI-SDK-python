from Crypto.Cipher import AES
import base64

# 需要加密的字符串必须为16的倍数
def pad(text):
    while len(text) % 16 != 0:
        text += b' '
    return text

# 加密
def get_encrypt(request_json,secret):
    # 秘钥为8位时，需要重复
    if len(secret) < 16:
        secret += secret
    key = secret.encode('utf-8')
    iv = key
    # 进行加密算法,模式ECB模式,把叠加完16位的秘钥传进来
    aes = AES.new(key, AES.MODE_CBC, iv)
    # 加密内容,此处需要将字符串转为字节
    text = str(request_json).encode('utf-8')
    # 进行内容拼接16位字符后传入加密类中,结果为字节类型
    # print(pad(text))
    encrypt_aes = aes.encrypt(pad(text))
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')
    return encrypted_text
