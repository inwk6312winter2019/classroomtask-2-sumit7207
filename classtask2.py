class ipaddress(object):
	def __init__ (self, ipadd, mask):
		self.ipadd =  ipadd.split(".")
		self.mask =  mask.split(".")

	def print_add(self):
		print("Address: ",end="")
		for str1 in self.ipadd:
			print(str1,".",end="")
		print("\t")
		for item in self.ipadd:
			print(bin(int(item))[2:],".",end= "")
		print()
		print("Netmask: ", end = "")
		for mask1 in self.mask:
			print(mask1,".",end="")
		print("\t")
		for item in self.mask:
			print(bin(int(item))[2:],".",end = "")


ipaddress1 = ipaddress("192.168.1.0","255.255.255.0")

ipaddress1.print_add()
