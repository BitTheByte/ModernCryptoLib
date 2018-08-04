class utilities:
	@staticmethod
	def egcd(a,b):
		from RSA_Attacks.utilities import egcd
		return egcd(a,b)
	@staticmethod
	def modinv(a,m):
		from RSA_Attacks.utilities import modinv
		return modinv(a,m)
	@staticmethod
	def mulinv(a,b):
		from RSA_Attacks.utilities import mulinv
		return  mulinv(a,b)
	@staticmethod
	def powinv(x,n):
		from RSA_Attacks.utilities import powinv
		return powinv(x,n)
	@staticmethod
	def rational_to_contfrac (x, y):
		from RSA_Attacks.utilities import rational_to_contfrac
		return rational_to_contfrac (x, y)
	@staticmethod
	def convergents_from_contfrac(frac):    
		from RSA_Attacks.utilities import convergents_from_contfrac
		return convergents_from_contfrac
	@staticmethod
	def contfrac_to_rational (frac):
		from RSA_Attacks.utilities import contfrac_to_rational
		return contfrac_to_rational (frac)
	@staticmethod
	def is_perfect_square(n):
		from RSA_Attacks.utilities import is_perfect_square
		return is_perfect_square(n)
	@staticmethod
	def isqrt(n):
		from RSA_Attacks.utilities import isqrt
		return isqrt(n)
class attacks:
    @staticmethod
    def Fermat(n,limit=9999):
        from RSA_Attacks.fermet import fermat
        return fermat(n,limit)
    @staticmethod
    def multiPrime(primes_array,n,e,c):
        from RSA_Attacks.multiPrime import multiPrime
        return multiPrime(primes_array,n,e,c)
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
    def Hasted(n1,n2,n3,chipher_text_1,chipher_text_2,chipher_text_3,e):
        from RSA_Attacks.hasted import hasted
        return hasted(n1,n2,n3,chipher_text_1,chipher_text_2,chipher_text_3,e)

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
        from RSA_Attacks.utilities import modinv
        return modinv(e,calculate.phi(p,q))

class convert:
    @staticmethod
    def hex_to_decimal(data_bytes):
        return long(data_bytes,16)
    @staticmethod
    def base64_to_decimal(b64_string):
        from base64 import b64decode
        return convert.hex_to_decimal( b64decode(b64_string) )
    @staticmethod
    def decimal_to_text(number):
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




        
