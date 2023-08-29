#---------------------------------------------
# Possible GET command:
# - /http_ping
# - /get_state_xxx
# - /get_image
#---------------------------------------------

from src.param import param_control
from src.connection.HTTPS.client import https_client_fct
from src.utils import parser_json

import json


def get_state(dest):
    [ip, port, connected] = https_client_fct.network_info(dest)
    command = "/get_state_" + dest
    data = https_client_fct.send_https_get(ip, port, connected, command)
    if(data != None and data != b''):
        try:
            if(dest == "edge"):
                parser_json.update_state_file(param_control.path_state_current + "state_edge.json", data)
                param_control.state_edge = json.loads(data)
            elif(dest == "ground"):
                parser_json.update_state_file(param_control.path_state_current + "state_ground.json", data)
                param_control.state_ground = json.loads(data)
            elif(dest == "network"):
                parser_json.update_state_file(param_control.path_state_current + "state_network.json", data)
                param_control.state_network = json.loads(data)
        except:
            print("[error] GET working problem dest [%s]"% dest)

def get_image(dest):
    [ip, port, connected] = https_client_fct.network_info(dest)
    command = "/get_image"
    data = https_client_fct.send_https_get(ip, port, connected, command)
    if(data != None):
        if(len(data) != 0):
            img = open(param_control.path_state_current + "image", "wb")
            img.write(data)
            img.close()
            return True
    return False