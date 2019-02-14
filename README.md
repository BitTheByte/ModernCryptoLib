# ModernCryptoLib
Cryptography library to automate cryptographic attacks main purpose to help CTF players and advanced users 

# Current version
0.0.12
# How to install
```bash
$ sudo python setup.py install
```
# Initialization
```python
from CryptoLib.RSA import RSA
```
# Example
```python
n = 3233
e = 17
c = 855 #(123 ** e) % n
factordb = RSA.attacks.Factordb(n)
q = factordb[0]
p = factordb[1]
d = RSA.utilities.modinv(e,780)
print "Decrypted Message : {}".format(pow(c,d,n))
```

# API
```
[-] N = Rsa modulus
[-] E = Rsa exponent
[-] C = Cipher text

RSA.utilities.egcd(a,b)
RSA.utilities.modinv(a,m)
RSA.utilities.mulinv(a,b)
RSA.utilities.powinv(x,n)
RSA.utilities.is_perfect_square(n)
RSA.utilities.isqrt(n)
RSA.utilities.rational_to_contfrac (x, y)
RSA.utilities.convergents_from_contfrac(frac)    
RSA.utilities.contfrac_to_rational (frac)

RSA.attacks.Hasted(n1,n2,n3,chipher_text_1,chipher_text_2,chipher_text_3,e)
RSA.attacks.Wiener(n,e)
RSA.attacks.Fermat(n,limit)
RSA.attacks.Chinese_remainder_theorem(p,q,dp,dq,chipher_text)
RSA.attacks.MultiPrime(primes_array,n,e,c)
RSA.attacks.Factordb(n)
     |_ https://factordb.com/
RSA.attacks.Gen_sideChannel_payload(n,c,e)
RSA.attacks.Reverse_sideChannel_payload(payload)
RSA.attacks.Common_modulus(chipher_text_1, chipher_text_2, e1, e2, n)

RSA.convert.hex_to_decimal(data_bytes)
RSA.convert.base64_to_decimal(b64_string)
RSA.convert.decimal_to_text(number)

RSA.KeyParser(path)
   |_ https://www.dlitz.net/software/pycrypto/api/current/Crypto.PublicKey.RSA-module.html

RSA.export.public_key(n,e)
RSA.export.private_key(n,e,d,p,q)

RSA.calculate.d(p,q,e)
RSA.calculate.phi(p,q)
```
# TO-DO
- Full documentation
- Finish aes attacks module
- Set standard return value for all functions instand of dictionaries, str and arrays
- Add Broadcast Attack
- ~~Add Multi-prime RSA attacks~~
- Clean the code
