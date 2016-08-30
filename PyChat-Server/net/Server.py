class Server(object):
	'The Server object'

	_addr = ""
	_port = ""

	def __init__(self, addr="localhost", port="5400"):
		_addr = addr
		_port = port

