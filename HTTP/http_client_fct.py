#! /usr/bin/python
#---------------------------------------------

from param import param_co
from HTTP import http_client
from src import connection
from src import parser_json

import http.client as client
import json
import time


def send_conn_request(command):
    ip = param_co.state_co["hubium"]["ip"]
    port = param_co.state_co["hubium"]["http_server_port"]
    connected = False
    sock = client.HTTPConnection(ip, port, timeout=0.1)
    try:
        sock.request("GET", command)
        connected = True
    except:
        connected = False
    sock.close()
    return connected

def send_state_request(name):
    connected = param_co.state_co["hubium"]["http_connected"]
    ip = param_co.state_co["hubium"]["ip"]
    port = param_co.state_co["hubium"]["http_server_port"]
    if(connected):
        try:
            sock = client.HTTPConnection(ip, port, timeout=1)
            sock.request("GET", name)
            response = sock.getresponse()
            state = response.read()
            sock.close()
            return state
        except:
            pass

def send_command_request(command, sucess):
    connected = param_co.state_co["hubium"]["http_connected"]
    ip = param_co.state_co["hubium"]["ip"]
    port = param_co.state_co["hubium"]["http_server_port"]
    if(connected):
        try:
            sock = client.HTTPConnection(ip, port, timeout=1)
            sock.request("GET", command)
        except:
            connection.connection_closed()

def send_image_request(path):
    connected = param_co.state_co["hubium"]["http_connected"]
    ip = param_co.state_co["hubium"]["ip"]
    port = param_co.state_co["hubium"]["http_server_port"]
    if(connected):
        try:
            sock = client.HTTPConnection(ip, port, timeout=1)
            sock.request("GET", "/image")
            response = sock.getresponse()
            data_binary = response.read()

            # Save image
            if(len(data_binary) != 0):
                img = open(path, "wb")
                img.write(data_binary)
                img.close()

            sock.close()
        except:
            connection.connection_closed()

def send_param_request(command, lvl1, lvl2, value):
    connected = param_co.state_co["hubium"]["http_connected"]
    ip = param_co.state_co["hubium"]["ip"]
    port = param_co.state_co["hubium"]["http_server_port"]

    header = {"Content-type": "application/json"}
    payload = {lvl1: {lvl2: value}}
    file = json.dumps(payload)

    if(connected):
        try:
            sock = client.HTTPConnection(ip, port, timeout=1)
            sock.request("POST", command, file, header)
            sock.close()
        except:
            print("[\033[1;31merror\033[0m] Command \033[1;36m%s\033[0m to ip \033[1;36m%s\033[0m port \033[1;36m%d\033[0m failed" % (command, ip, port))
