#---------------------------------------------
from src.param import param_control
from src.utils import terminal

from datetime import datetime

import psutil
import os


def test_ssd_con():
    path = param_control.path_ssd
    if(os.path.exists(path) and path.find("lidar_ssd") != -1):
        hdd = psutil.disk_usage(param_control.path_ssd)
        param_control.state_control["interface"]["ssd_connected"] = True
        param_control.state_control["ssd"]["space_used"] = int(hdd.used / (2**30))
        param_control.state_control["ssd"]["space_total"] = int(hdd.total / (2**30))
    else:
        param_control.state_control["interface"]["ssd_connected"] = False
        param_control.state_control["ssd"]["space_used"] = 0
        param_control.state_control["ssd"]["space_total"] = 0

def determine_path():
    date = get_formatedge_2_time()
    param_control.state_control["ssd"]["path"]["dir_capture"] = os.path.join(param_control.path_ssd, "capture")
    param_control.state_control["ssd"]["path"]["file_name"] = param_control.state_control["ssd"]["path"]["file_name_add"] + "_" + date + ".pcap"
    param_control.state_control["ssd"]["path"]["dir_l1"] = os.path.join(param_control.state_control["ssd"]["path"]["dir_capture"], "lidar_1")
    param_control.state_control["ssd"]["path"]["dir_l2"] = os.path.join(param_control.state_control["ssd"]["path"]["dir_capture"], "lidar_2")
    param_control.state_control["ssd"]["path"]["path_l1_file"] = os.path.join(param_control.state_control["ssd"]["path"]["dir_l1"], param_control.state_control["ssd"]["path"]["file_name"])
    param_control.state_control["ssd"]["path"]["path_l2_file"] = os.path.join(param_control.state_control["ssd"]["path"]["dir_l2"], param_control.state_control["ssd"]["path"]["file_name"])
    new_path = param_control.state_control["ssd"]["path"]["dir_capture"] + "/lidar_x/" + param_control.state_control["ssd"]["path"]["file_name"]

def get_formatedge_2_time():
    date = datetime.now().strftime('%d-%m-%Y_%Hh%M')
    return str(date)

def check_directories():
    connected = param_control.state_control["interface"]["ssd_connected"]
    if(connected):
        # Capture directory
        path = param_control.state_control["ssd"]["path"]["dir_capture"]
        if(os.path.exists(path) == False):
            create_directory(path)
        # Lidar 1 directory
        path = param_control.state_control["ssd"]["path"]["dir_l1"]
        if(os.path.exists(path) == False):
            create_directory(path)
        # Lidar 2 directory
        path = param_control.state_control["ssd"]["path"]["dir_l2"]
        if(os.path.exists(path) == False):
            create_directory(path)

def create_directory(path):
    os.mkdir(path)
    terminal.addLog("#", "Directory %s created" % path)

def clear_directory(path):
    for file in os.scandir(path):
        os.remove(file.path)
