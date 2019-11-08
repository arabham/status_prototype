import os
import subprocess
import platform
import threading
from queue import Queue


activeTxt = open("activeIP.txt", 'w+')
activeTxt.close()

def ping(host):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', host]
    return subprocess.call(command)

def buildHostList():
    subnet2List = []
    subnet3List = []
    subnet4List = []
    subnet5List = []
    subnet6List = []
    subnet7List = []
    subnet8List = []
    hostlist = []
    active = []
    for i in range(1,255):
        subnet2List.append("192.168.2." + str(i))
        subnet3List.append("192.168.3." + str(i))
        subnet4List.append("192.168.4." + str(i))
        subnet5List.append("192.168.5." + str(i))
        subnet6List.append("192.168.6." + str(i))
        subnet7List.append("192.168.7." + str(i))
        subnet8List.append("192.168.8." + str(i))
    hostlist.extend(subnet2List)
    hostlist.extend(subnet3List)
    hostlist.extend(subnet4List)
    hostlist.extend(subnet5List)
    hostlist.extend(subnet6List)
    hostlist.extend(subnet7List)
    hostlist.extend(subnet8List)
    return hostlist

def active():
    hosts = buildHostList()
    active = []
    for i in hosts:
        if ping(str(i)) == 1:
            active.append(str(i))
            activeTxt = open("activeIP.txt", 'a')
            activeTxt.write(str(i + '\n'))
            activeTxt.close()
        else:
            print("no host found")
    return active

if __name__ == "__main__":
    active()
