import IPScanner
import Rig
import LogFetcher
import FileReader
import MakeTable

def main():
    #rig = Rig()
    #activeIPs = IPScanner.active()
    #print(activeIPs)

    #for i in activeIPs():
    # testing loop
    # TODO:remove
    for i in range(1):
        LogFetcher.ftpLogs(str(activeIPs[i]))
        name = FileReader.parseName()
        uptime = FileReader.parseUptime()
        temp = FileReader.parseTemp()
        gpuCount = FileReader.parseGPUCount()
        hashrate = FileReader.parseHashrate()
        rig = Rig(name,uptime,hashrate,tempactiveIPs[i])
        table = MakeTable.makeCSV(name,uptime,temp,gpuCount,hashrate,activeIPs[i])



if __name__ == '__main__':
    main()
    #global rig


    input('Press ENTER to exit')