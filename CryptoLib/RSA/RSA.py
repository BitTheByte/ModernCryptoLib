class attacks:
    @staticmethod
    def Fermat(n,limit=9999):
        from RSA_Attacks.fermet import fermat
        return fermat(n,limit)

    @staticmethod
    def Common_modulus(chipher_text_1, chipher_text_2, e1, e2, n):
        from RSA_Attacks.common_modulus import common_modulus
        return common_modulus(chipher_text_1, chipher_text_2, e1, e2, n)

    @staticmethod
    def Chinese_remainder_theorem(p,q,dp,dq,chipher_text):
        from RSA_Attacks.chinese_remainder_theorem import chinese_remainder_theorem
        return chinese_remainder_theorem(p,q,dp,dq,chipher_text)

    @staticmethod
    def Wiener(n,e):
        from RSA_Attacks.wiener import wiener
        return wiener(n,e)

    @staticmethod
    def Hasted(n1,n2,n3,chipher_text_1,chipher_text_2,chipher_text_3):
        from RSA_Attacks.hasted import hasted
        return hasted(n1,n2,n3,chipher_text_1,chipher_text_2,chipher_text_3)

    @staticmethod
    def Gen_sideChannel_payload(n,c,e):
        from RSA_Attacks.side_channel import gen_sideChannel_payload
        return gen_sideChannel_payload(n,c,e)
        
    @staticmethod
    def Reverse_sideChannel_payload(payload):
        from RSA_Attacks.side_channel import reverse_sideChannel_payload
        return reverse_sideChannel_payload(payload)
    @staticmethod
    def factordb(n):
        from RSA_Attacks.factordb import FactorDB
        f =  FactorDB(n)
        f.connect()
        return f.get_factor_list()

class calculate:
    @staticmethod
    def phi(p,q):
        return (p - 1) * (q -1)
    @staticmethod
    def d(p,q,e):
        from RSA_Attacks.utilities import egcd
        return egcd(e,calculate.phi(p,q))[1]

class convert:
    @staticmethod
    def bytes_to_number(data_bytes):
        return long(data_bytes,16)
    @staticmethod
    def base64_to_number(b64_string):
        from base64 import b64decode
        return convert.bytes_to_number( b64decode(b64_string) )
    @staticmethod
    def number_to_text(number):
        number = format(int(number), 'x')
        return str(number).decode("hex")

def KeyParser(path):
        from Crypto.PublicKey import RSA
        return RSA.importKey(open(path, "r").read())
class export:
    @staticmethod
    def public_key(n,e):
        from Crypto.PublicKey import RSA
        print RSA.construct((long(n), long(e))).exportKey()
    @staticmethod
    def private_key(n,e,d,p=None,q=None):
        from Crypto.PublicKey import RSA
        if q != None and p != None:
            return RSA.construct((long(n), long(e) ,long(d) ,long(p),long(q))).exportKey()
        else:
            return RSA.construct((long(n), long(e) ,long(d))).exportKey()




        
