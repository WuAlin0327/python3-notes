import configparser


def socket_conf(addr):
	co = configparser.ConfigParser()
	print(co.sections())
	co.read(addr)
	return co['socket']

def userinfo(addr):
	config = configparser.ConfigParser()
	config.read(addr)
	return config
