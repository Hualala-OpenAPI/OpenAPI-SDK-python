'''
提供requestBody解密工具
'''

from Crypto.Cipher import AES
import base64

# 解密算法
def decrypt_aes(cryptedStr,secret):
    if len(secret) < 16:
        secret += secret
    key = secret.encode('utf-8')
    iv = key
    generator = AES.new(key, AES.MODE_CBC, iv)
    cryptedStr = base64.b64decode(cryptedStr)
    plain_text = generator.decrypt(cryptedStr)
    decryptedStr = plain_text.decode('utf-8').rstrip('\0')
    return decryptedStr


if __name__ == '__main__':
    # appSecret
    app_secret = "12345678"
    # 需要解密的内容，requestBody
    cryptedStr = '''
3DjoV9Pw4XAEL655NHFgLFIb/EfHnOJgGNqsD1++lx20qjxtZNjqo2Ydsg71MGqPV9B7h/M3JcEj
UO1BCzE6QcHmKcoeT/ShKsO8n6zOu0fr1JEkubCvUb+SeKQ0c2CMmUYIbS8ku72R5VALO886rs+P
7lLd6NE77GgJw7TabXfKxcQUJ/K99FSNhItQQ0w3qvf/ORBsY1dWyWGMkeI2sZeIXX+griiRV3ms
/FB6p59RWBrw+6O13aVVBS9eLWpAJYURkzK4zd1Ah0QE2BL1g+g29kNCsd5fQD5vIOMzbPOoM+VX
tJKkHFCIKOddu4gDBinmEkuqoboFfzgmcw5i05RnCdtk3yyStmMxkwCA7gNG3t4CqnzqQoZBtXBv
E1TqRSfL8UaTl4tRox6yZCDk3Jx2TfjFL2q4pnmOq06TpuhyxvGmBPgF0YkscCxqVoCGVeAdN2Vm
4TQw+dhTf6M1ZiGhX3TBM6+4EhzvGuWT2XbFiO0Y1Mu3xjv4Rxxg9E0moMNLszNpu+2/mJaofZo5
w/VqVkzMuNXkMl3CZY9J2cYHdkspZ+Db2I2NOD+QLgqq77303u93uZJvDzKRofWCkiFruJWL00jz
gOI0BqqbpjZdYP1hR6iI5+QJYmlWB4RueSNDgkjNFC7AELYYQFKJTVeZSsnQqf3W7CKH5uc3ieHN
m5vRr+28w/ZE2geFRaLwu08e6j3IBHCmc8ONvaGry7mmMY3M2uWyVHJYTvfFFGVFD8oMTR8wduQ8
mw+dGMVoYuEFVgKO9PL70uw6Q49Uc/Ax09S249FK90rMMZ5PRjgQ6/bb0Z8fMz7cEN0tKaJwKWhe
/wWNj+V7z7LgkqaGN4mKne7DBZ6/SUwcsOjYQ2unamX91PigBDa5L9nXic2SDExEcd+G2BoJ2Sm7
VEidcSuI9r3xtj7OufQENSv1qiWylT3OUNwLsHuXeHe5x0+VN+rY0zAicuYeNm6vMiQRvHMk0F47
BWk+LtnHtRxyas6bkYLaJ8MBCqhQJuALBWoPw3fqS6mMrTwG9nnR3UveK+TIdtt3XvaIyU7J0T1Y
DUJ4u6lLbG6qePYAOHGb5A17etp9Yylb+qfyZuOIb8wJfomQbuj6IfCOKzB98W3pilwE/9BmLcHy
4R1p32ZYLjHWryQ/F4X5oO3NJMHrkpwzFbqJd11Nuzjlx+HDrH2TpLnvYxEdSkRG+zHrTjL6AJQW
zHvZDq9g474DJVFrg7Z8TjM+bjLbqFcbdvCPGN+Sg0njz6QclHmspwn5p2VEkSNecS+HZ3nDLajz
Y51vx6irAhUa2m8TUiPKbxCBMlP99arJjnj9kAQf9pcGCNOeRCoCIXWy2tShS/jdO6zTAHU8qPZz
uxpQltOle6g7r8+KPlhny25ObcYD1kMuAypACy6EwToXwGAsg/2p/9WP7FBEnA==
'''
    print("解密结果为：",decrypt_aes(cryptedStr,app_secret))

