from Crypto.Cipher import AES
from cryptography.fernet import Fernet
from Crypto import Random

class AESChipher:
    def __init__(self):
        self.CBC = self.CBC()
        self.ECB = self.ECB()
        self.fernet = self.fernet()
    class ECB:
        def encrypt(self,key,text):
            return AES.new(key,AES.MODE_ECB).encrypt(text)
        def decrypt(self,key,chipher_text):
            return AES.new(key,AES.MODE_ECB).decrypt(chipher_text)
    class CBC:
        def __init__(self):
            self.calculate = self.calculate()
        def encrypt(self,plain_text,key,iv):
            pad = lambda s: s + (16 - len(s) %16) * chr(16 - len(s) % 16)
            return AES.new(key, AES.MODE_CBC, iv).encrypt(pad(plain_text))
        def decrypt(self, chipher_text,key,iv):
            unpad = lambda s: s[:-ord(s[-1:])]
            cipher = AES.new(key, AES.MODE_CBC, iv)
            return unpad(cipher.decrypt(chipher_text)).decode('utf8')
        def gen_iv(self):
            return Random.new().read(16)
        class calculate:
            def iv(self,plain_text,chipher_text,key):
                plain_text = plain_text[:16]
                chipher_text = chipher_text[:16]
                iv = AES.new(key ,AES.MODE_ECB).decrypt(chipher_text)
                return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(plain_text , iv)).encode("hex")
    class fernet:
        def encrypt(self,key,text):
            return Fernet(key).encrypt(text)
        def decrypt(self,key,chipher_text):
            return Fernet(key).decrypt(chipher_text)
        def gen_key(self):
            return Fernet.generate_key()