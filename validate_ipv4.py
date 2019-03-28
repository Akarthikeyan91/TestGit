#!/c/Python36/python

import re 
ip_address = "IP address is need to be validated and segreagated with the IP subnetting 200.34.23.1/23, ip address of interface is 192.168.1.3/28 and 192.178.2.1/31 this should be derived for network planning"
regex = re.findall(r"(\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b)\/(\b[0-9]{1,2}\b)",ip_address)
print("REGEXP", regex)
for i in regex:
    valid_ip_address = i 
    print (valid_ip_address)
    if len(valid_ip_address) == 2:
        subnet_mask = valid_ip_address[1]
        ip_address = valid_ip_address[0]
        host = 2**(32-int(subnet_mask))
        network = 2**(8-(32-int(subnet_mask)))
        print ("No of Hosts {}".format(host-2))
        print ("No of Networks {}".format(network))
        ip_class = re.findall(r"(\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b))",ip_address)
        if int(ip_class[0]) <= 126:
            print ("Class A network")
#Code need to write for Class A network            
        elif int(ip_class[0]) >=128 and int(ip_class[0]) <=191:
            print ("Class B Network")
#Code need to write for Class B network 
        elif int(ip_class[0]) >=192 and int(ip_class[0]) <=223:
            print (ip_class)
            print ("Class C Network")
            ip_class[3]= "0"
            network_ip_address = ".".join(ip_class)
            ip_class[3] = str(host-1)
            broadcast_ip_address = ".".join(ip_class)
            print ("Network IP address is {}".format(network_ip_address))
            print ("Network Broadcast IP address is {}".format(broadcast_ip_address))
        else:
            print ("Given IP address cant be subnetted")
