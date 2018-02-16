from utilities import modinv
def chinese_remainder_theorem(p,q,dp,dq,chipher_text):
    q_inv = modinv(p , q)
    m1 = pow(chipher_text,dp,p)
    m2 = pow(chipher_text,dq,q)
    h = (q_inv*(m1-m2)) % p
    return m2 + h * q