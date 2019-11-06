
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