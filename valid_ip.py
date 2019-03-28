#!/c/Python36/python
import re

# IP Validation calling through function 

def ip_address_validation(interface_output):
     regex = re.findall(r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})", interface_output)
     print(regex)
     print(len(regex))
     valid_ip = 0
     error_count = 0
     if len(regex) != 0:
         for i in regex:
             ip_valid = list(i)
             if len(ip_valid) == 4:
                 for i in ip_valid:
                     value=int(i)
                     if value <= 255:
                         valid_ip += 1
                         if valid_ip == 4:
                             ip_address = ".".join(ip_valid)
                             print ("Given {} is valid".format(ip_address))
                             valid_ip = 0
                     else:
                         ip_address = ".".join(ip_valid)
                         print ("Given {} is not valid".format(ip_address))
                         error_count =+ 1
     else:
         print ("There is no IP address found")
         error_count =+ 1
     if error_count == 0:
         print("+++PASS+++ IP address validated")
     else:
         print("+++FAIL+++ IP address is not valid")


#ip_address_validation('-192.34.56.7')

log_info = """Router# show interfaces
 Ethernet 0 is up, line protocol is up
 Hardware is MCI Ethernet, address is 0000.0c00.750c (bia 0000.0c00.750c)
 Internet address is 131.108.28.8, subnet mask is 255.255.255.0
 MTU 1500 bytes, BW 10000 Kbit, DLY 100000 usec, rely 255/255, load 1/255
 Encapsulation ARPA, loopback not set, keepalive set (10 sec)
 ARP type: ARPA, ARP Timeout 4:00:00
 Last input 0:00:00, output 0:00:00, output hang never
 Last clearing of "show interface" counters 0:00:00
 Output queue 0/40, 0 drops; input queue 0/75, 0 drops
 Five minute input rate 0 bits/sec, 0 packets/sec
 Five minute output rate 2000 bits/sec, 4 packets/sec
     1127576 packets input, 447251251 bytes, 0 no buffer
     Received 354125 broadcasts, 0 runts, 0 giants, 57186* throttles
     Internet address is 141.23.0.3, 0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     5332142 packets output, 496316039 bytes, 0 underruns
     0 output errors, 432 collisions, 0 interface resets, 0 restarts
 ...

router#show interface atm 10/1/0 
     ATM10/1/0 is up, line protocol is up 
     Hardware is cyBus ENHANCED ATM PA 
     MTU 1500 bytes, sub MTU 1500, BW  149760 Kbit, DLY 80 usec,
     Internet address is 162.20.0.255,
         reliability 249/255, txload 1/255, rxload 1/255 """


interface_output_raw = re.findall(r"Internet address.*,",log_info, re.M)
interface_output = ''.join(interface_output_raw)
print(ip_address_validation(interface_output))
