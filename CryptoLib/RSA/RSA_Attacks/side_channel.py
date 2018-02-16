def gen_sideChannel_payload(n,c,e):
	c1 = (c ** e)
	c2 = (2 ** e)
	return (c1*c2) % n
def reverse_sideChannel_payload(payload):
	return payload / 2


