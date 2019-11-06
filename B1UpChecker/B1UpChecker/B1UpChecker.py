import IPScanner

def main():
    numOfSubnets = 7
    activeIPs = runSubnetScan(numOfSubnets)

if __name__ == '__main__':
    main()
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

    input('Press ENTER to exit')