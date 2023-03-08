# import panos
# from panos.firewall import Firewall
# from panos.panorama import Panorama

# Grab API KEY using GET or POST method
# curl -k -X GET 'https://<firewall>/api/?type=keygen&user=<username>&password=<password>'
# or
# curl -k -X POST 'https://<firewall>/api/?type=keygen&user=<username>&password=<password>'

# First API Call
# curl -k 'https://<firewall>//api/?type=op&cmd=<show><system><info></info></system></show>&key=<apikey>'

# TODOS
#    - Fix self signed cert auth
#    - verify=True

import requests
import xmltodict

# FW_IP = "aaa.bbb.ccc.ddd"
FW_IP = ""
API_ACTION = "/api/?type=op"
API_PATH = "&cmd=<show><system><info></info></system></show>"
API_KEY = ""

sys_info_api = requests.get(f"https://{FW_IP}{API_ACTION}{API_PATH}&key={API_KEY}", verify=True)

sys_info_dict = xmltodict.parse(sys_info_api.text)

sys_info_system = sys_info_dict['response']['result']['system']

hostname = sys_info_system['hostname']
ip_address = sys_info_system['ip-address']
serial = sys_info_system['serial']
panos_version = sys_info_system['sw-version']

print(f"Hostname: {hostname}, \
    IP Address: {ip_address}, \
    Serial: {serial}, \
    PANOS Version: {panos_version}")
