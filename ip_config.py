#!/c/Python36/python


import re
config = """service timestamps log datetime msec localtime show-timezone
 service timestamps interface debug datetime msec localtime show-timezone
 !
 interface FastEthernet0/1
  switchport mode access
  no ip address
  switchport access vlan 532
  storm-control broadcast level 0.4 0.3
  storm-control action trap
  no shutdown
 !
 interface FastEthernet0/2
  ip address 10.0.12.1 255.255.255.0
  switchport mode trunk
  switchport trunk allowed 300,532
  switchport nonegotiate
  shutdown
 !
 interface FastEthernet0/3
  ip address 10.0.16.1 255.255.255.0
  switchport mode access
  switchport access vlan 300
  storm-control broadcast level 0.4 0.3
  storm-control action trap
  shutdown
 !
 interface FastEthernet0/4
  no ip address
  switchport
  switchport mode access
  storm-control broadcast level 0.4 0.3
  storm-control action trap
  shutdown
 !
 end
 """

int_config = []
config_split = config.split("!")
#print(config_split)
for interface in config_split:
    #print(interface)
    if re.search(r"interface.*\d\/\d",interface):
        int_config.append(interface)
        #print("INT CONF",int_config)
for int_detail in int_config:
    int_name = re.search(r"interface.*\n",int_detail)
    value1=(int_name.group().strip("\n"))
    #print(value1)
    int_ip = re.search(r"ip address.*\n|no ip.*\n",int_detail)
    value2=(int_ip.group().strip("\n"))
    #print(value2)
    int_state = re.search(r"shutdown\n|no shutdown\n",int_detail)
    value3=(int_state.group().strip("\n"))
    #print(value3)
    int_details = " ".join([value1,value2,value3])
    print(int_details)
