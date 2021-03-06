''' for python 3 reqires for of textFSM avialable at https://github.com/jonathanslenders/textfsm


 Copyright 2016 Hewlett Packard Enterprise Development LP.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.'''
import jtextfsm as textfsm
import json




displayiproute = '''<5900>dis ip routing-table

Destinations : 42	Routes : 42

Destination/Mask    Proto  Pre  Cost         NextHop         Interface
0.0.0.0/32          Direct 0    0            127.0.0.1       InLoop0
10.3.10.0/24        OSPF   10   2            10.20.1.254     Vlan1
10.10.3.0/24        OSPF   10   2            10.20.1.254     Vlan1
10.10.10.0/24       OSPF   10   2            10.20.1.254     Vlan1
10.10.11.0/24       OSPF   10   2            10.20.1.254     Vlan1
10.10.12.0/24       OSPF   10   2            10.20.1.254     Vlan1
10.10.13.0/24       OSPF   10   2            10.20.1.254     Vlan1
10.10.50.0/24       OSPF   10   2            10.20.1.254     Vlan1
10.10.101.0/24      OSPF   10   2            10.20.1.254     Vlan1
10.10.102.0/24      OSPF   10   2            10.20.1.254     Vlan1
10.10.103.0/24      OSPF   10   2            10.20.1.254     Vlan1
10.10.105.0/24      OSPF   10   2            10.20.1.254     Vlan1
10.10.106.0/24      OSPF   10   2            10.20.1.254     Vlan1
10.10.201.0/24      OSPF   10   2            10.20.1.254     Vlan1
10.10.203.0/24      OSPF   10   2            10.20.1.254     Vlan1
10.15.1.0/24        OSPF   10   2            10.20.1.254     Vlan1
10.20.1.0/24        Direct 0    0            10.20.1.1       Vlan1
10.20.1.0/32        Direct 0    0            10.20.1.1       Vlan1
10.20.1.1/32        Direct 0    0            127.0.0.1       InLoop0
10.20.1.255/32      Direct 0    0            10.20.1.1       Vlan1
10.20.10.0/24       OSPF   10   2            10.20.1.254     Vlan1
10.101.0.0/24       OSPF   10   2            10.20.1.254     Vlan1
10.101.2.0/24       OSPF   10   2            10.20.1.254     Vlan1
10.101.15.0/24      OSPF   10   2            10.20.1.254     Vlan1
10.101.16.0/24      OSPF   10   3            10.20.1.254     Vlan1
10.102.1.0/24       OSPF   10   2            10.20.1.254     Vlan1
10.254.0.100/32     OSPF   10   3            10.20.1.254     Vlan1
127.0.0.0/8         Direct 0    0            127.0.0.1       InLoop0
127.0.0.0/32        Direct 0    0            127.0.0.1       InLoop0
127.0.0.1/32        Direct 0    0            127.0.0.1       InLoop0
127.255.255.255/32  Direct 0    0            127.0.0.1       InLoop0
172.16.2.0/24       OSPF   10   2            10.20.1.254     Vlan1
172.16.3.0/24       OSPF   10   2            10.20.1.254     Vlan1
172.16.3.10/32      OSPF   10   1            10.20.1.254     Vlan1
172.16.4.0/24       OSPF   10   2            10.20.1.254     Vlan1
172.16.5.0/24       OSPF   10   2            10.20.1.254     Vlan1
172.16.6.0/24       OSPF   10   2            10.20.1.254     Vlan1
172.16.7.0/24       OSPF   10   2            10.20.1.254     Vlan1
192.168.1.221/32    OSPF   10   1            10.20.1.254     Vlan1
224.0.0.0/4         Direct 0    0            0.0.0.0         NULL0
224.0.0.0/24        Direct 0    0            0.0.0.0         NULL0
255.255.255.255/32  Direct 0    0            127.0.0.1       InLoop0
<5900>'''


template = open("./templates/displayiproutingtable.textfsm")
re_table = textfsm.TextFSM(template)
fsm_results = re_table.ParseText(displayiproute)



print (json.dumps(fsm_results, indent=4))