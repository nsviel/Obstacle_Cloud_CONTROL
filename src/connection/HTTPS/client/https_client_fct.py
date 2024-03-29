#---------------------------------------------
from src.param import param_control

import http.client


def network_info(dest):
    ip = param_control.state_edge["hub"]["info"]["ip"]
    port = param_control.state_edge["hub"]["http"]["server_port"]
    connected = param_control.state_control["interface"]["edge"]["http_connected"]
    return [ip, port, connected]

def send_https_ping(ip, port):
    client = http.client.HTTPConnection(ip, port, timeout=2)
    connected = False
    try:
        client.request("GET", "/http_ping")
        connected = True
    except:
        connected = False
    client.close()
    return connected

def send_https_post(ip, port, connected, command, payload):
    if(connected):
        try:
            client = http.client.HTTPConnection(ip, port, timeout=2)
            header = {"Content-type": "application/json"}
            client.request("POST", command, payload, header)
            client.close()
        except:
            print("[\033[1;31merror\033[0m] Command \033[1;36m%s\033[0m to ip \033[1;36m%s\033[0m port \033[1;36m%d\033[0m failed [\033[1;36m%s\033[0m ]" % (command, ip, port, payload))

def send_https_get(ip, port, connected, command):
    data = None
    if(connected):
        try:
            client = http.client.HTTPConnection(ip, port, timeout=2)
            client.request("GET", command)
            response = client.getresponse()
            data = response.read()
            client.close()
        except:
            pass
    return data
