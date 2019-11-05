import subprocess
import threading
import pysftp
import time
import sys
import os
from queue import Queue

active = []
cnopts = pysftp.CnOpts()
rusername = 'root'
rpassword = 'arabham110@gmail.com'
cnopts.hostkeys = None  

class Rig:

    def __init__(self, name, status, hashrate, temp, ip):
        self.name = name
        self.status = status
        self.hashrate = hashrate
        self.temp = temp
        self.ip = ip

    def setRigName(self, new_name):
        self.name = new_name

    def setRigStatus(self, new_status):
        self.status = new_status

    def setRigHashrate(self, new_hashrate):
        self.hashrate = new_hashrate

    def setRigTemp(self, new_temp):
        self.temp = new_temp

    def setRigIP(self, new_ip):
        self.ip = new_ip

    def getRigName(self):
        return(self.name)

    def getRigStatus(self):
        return(self.status)

    def getRigHashrate(self):
        return(self.hashrate)

    def getRigTemp(self):
        return(self.temp)

    def getRigIP(self):
        return(self.ip)

    def getRigAll(self):
        rigAll = [self.name,self.status,self.hashrate,self.temp,self.ip]
        return(rigAll)

def vlan2Scan():
    lock=threading.Lock()
    _start=time.time()
    def check(n):
        with open(os.devnull, "wb") as limbo:
                ip="192.168.2.{0}".format(n)
                result=subprocess.Popen(["ping", "-n", "1", "-w", "300", ip],stdout=limbo, stderr=limbo).wait()
                with lock:                    
                    if not result:
                        active.append(ip)
                        print (ip, "active")                    
                    else:
                        #print (ip, "inactive") 
                        pass                        

    def threader():
        while True:
            worker=q.get()
            check(worker)
            q.task_done()
    q=Queue()

    for x in range(255):
        t=threading.Thread(target=threader)
        t.daemon=True
        t.start()
    for worker in range(1,255):
        q.put(worker)
    q.join()
    print("Process completed in: ",time.time()-_start)

def vlan3Scan():
    lock=threading.Lock()
    _start=time.time()
    def check(n):
        with open(os.devnull, "wb") as limbo:
                ip="192.168.3.{0}".format(n)
                result=subprocess.Popen(["ping", "-n", "1", "-w", "300", ip],stdout=limbo, stderr=limbo).wait()
                with lock:                    
                    if not result:
                        active.append(ip)
                        print (ip, "active")                    
                    else:
                        #print (ip, "inactive") 
                        pass                        

    def threader():
        while True:
            worker=q.get()
            check(worker)
            q.task_done()
    q=Queue()

    for x in range(255):
        t=threading.Thread(target=threader)
        t.daemon=True
        t.start()
    for worker in range(1,255):
        q.put(worker)
    q.join()
    print("Process completed in: ",time.time()-_start)

def vlan4Scan():
    lock=threading.Lock()
    _start=time.time()
    def check(n):
        with open(os.devnull, "wb") as limbo:
                ip="192.168.4.{0}".format(n)
                result=subprocess.Popen(["ping", "-n", "1", "-w", "300", ip],stdout=limbo, stderr=limbo).wait()
                with lock:                    
                    if not result:
                        active.append(ip)
                        print (ip, "active")                    
                    else:
                        #print (ip, "inactive") 
                        pass                        

    def threader():
        while True:
            worker=q.get()
            check(worker)
            q.task_done()
    q=Queue()

    for x in range(255):
        t=threading.Thread(target=threader)
        t.daemon=True
        t.start()
    for worker in range(1,255):
        q.put(worker)
    q.join()
    print("Process completed in: ",time.time()-_start)

def vlan5Scan():
    lock=threading.Lock()
    _start=time.time()
    def check(n):
        with open(os.devnull, "wb") as limbo:
                ip="192.168.5.{0}".format(n)
                result=subprocess.Popen(["ping", "-n", "1", "-w", "300", ip],stdout=limbo, stderr=limbo).wait()
                with lock:                    
                    if not result:
                        active.append(ip)
                        print (ip, "active")                    
                    else:
                        #print (ip, "inactive") 
                        pass                        

    def threader():
        while True:
            worker=q.get()
            check(worker)
            q.task_done()
    q=Queue()

    for x in range(255):
        t=threading.Thread(target=threader)
        t.daemon=True
        t.start()
    for worker in range(1,255):
        q.put(worker)
    q.join()
    print("Process completed in: ",time.time()-_start)

def vlan6Scan():
    lock=threading.Lock()
    _start=time.time()
    def check(n):
        with open(os.devnull, "wb") as limbo:
                ip="192.168.6.{0}".format(n)
                result=subprocess.Popen(["ping", "-n", "1", "-w", "300", ip],stdout=limbo, stderr=limbo).wait()
                with lock:                    
                    if not result:
                        active.append(ip)
                        print (ip, "active")                    
                    else:
                        #print (ip, "inactive") 
                        pass                        

    def threader():
        while True:
            worker=q.get()
            check(worker)
            q.task_done()
    q=Queue()

    for x in range(255):
        t=threading.Thread(target=threader)
        t.daemon=True
        t.start()
    for worker in range(1,255):
        q.put(worker)
    q.join()
    print("Process completed in: ",time.time()-_start)

def vlan7Scan():
    lock=threading.Lock()
    _start=time.time()
    def check(n):
        with open(os.devnull, "wb") as limbo:
                ip="192.168.7.{0}".format(n)
                result=subprocess.Popen(["ping", "-n", "1", "-w", "300", ip],stdout=limbo, stderr=limbo).wait()
                with lock:                    
                    if not result:
                        active.append(ip)
                        print (ip, "active")                    
                    else:
                        #print (ip, "inactive") 
                        pass                        

    def threader():
        while True:
            worker=q.get()
            check(worker)
            q.task_done()
    q=Queue()

    for x in range(255):
        t=threading.Thread(target=threader)
        t.daemon=True
        t.start()
    for worker in range(1,255):
        q.put(worker)
    q.join()
    print("Process completed in: ",time.time()-_start)

def vlan8Scan():
    lock=threading.Lock()
    _start=time.time()
    def check(n):
        with open(os.devnull, "wb") as limbo:
                ip="192.168.8.{0}".format(n)
                result=subprocess.Popen(["ping", "-n", "1", "-w", "300", ip],stdout=limbo, stderr=limbo).wait()
                with lock:                    
                    if not result:
                        active.append(ip)
                        print (ip, "active")                    
                    else:
                        #print (ip, "inactive") 
                        pass                        

    def threader():
        while True:
            worker=q.get()
            check(worker)
            q.task_done()
    q=Queue()

    for x in range(255):
        t=threading.Thread(target=threader)
        t.daemon=True
        t.start()
    for worker in range(1,255):
        q.put(worker)
    q.join()
    print("Process completed in: ",time.time()-_start)

def runVlanScans():
    global active
    vlan2Scan(),vlan3Scan(),vlan4Scan(),vlan5Scan(),vlan6Scan(),vlan7Scan(),vlan8Scan()
    return active

def parseRigName():
    rigName = ''
    data = []
    with open("name.miner.log", "r") as f:
        for line in f:
            for word in line.split('"'):
                data.append(word)

    for i, x in enumerate(data):
       if(x.startswith('AAB1')):
           rigName = x
    print(rigName)
    return rigName

def parseRigStatus():
    loglines = []
    rigStatus = 'Online'
    with open ('screen.miner.log', 'r') as screenminerlog:
        for logline in screenminerlog:
            loglines.append(logline)

    loglines.reverse()

    for num, lines in enumerate(loglines):
        if(loglines[num][0] != 'G'):
            rigStatus = 'Troubleshoot'
            break

    return rigStatus

def parseRigHashRate():
    return "Needs work"

def parseRigTemp():
    return "Needs work"

def ftpLogs(rigIP):
    try:
        with pysftp.Connection(host=rigIP, username=rusername, password=rpassword, cnopts=cnopts) as sftp:
            remoteNameFilePath = '/home/miner/config.json'
            remoteFilePath = '/var/tmp/screen.miner.log'
            localNameFilePath = './name.miner.log'
            localFilePath = './screen.miner.log'

            if exists(remoteNameFilePath):
                if exists(localNameFilePath):
                    sftp.get(remoteNameFilePath, localNameFilePath)
                else:
                    print("local file path does not exist!")
            else:
                print("remote file path does not exist!")

            if exists(remoteFilePath):
                if exists(localFilePath):
                    sftp.get(remoteFilePath, localFilePath)
                else:
                    print("local file path does not exist!")
            else:
                print("remote file path does not exist!")
    except:
        print("failed to connect to server!")


if __name__ == '__main__':
    # active ip scan
    runVlanScans();
    global rig
    # TODO remove
    print(len(active))
    for i, x in enumerate(active):
        rigIP = x
        ftpLogs(rigIP)
        rigName = parseRigName()
        rigStatus = parseRigStatus()
        rigHashrate = parseRigHashRate()
        rigTemp = parseRigTemp()
        rig = Rig(rigName,rigStatus,rigHashrate,rigTemp,rigIP)

    f = open("activeips.txt", "w+")
    for x in range(len(active)):
        # TODO remove
        print(active[x])
        f.write(str(active[x]))
        f.write('\n')
    f.close()
    print(rig.getRigAll())

    #parseLog()

    # set status
