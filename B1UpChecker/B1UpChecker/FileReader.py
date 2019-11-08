#working
def parseName():
    rigName = ''
    data = []
    with open("name.miner.log", "r") as f:
        for line in f:
            for word in line.split('"'):
                data.append(word)

    for i, x in enumerate(data):
       if(x.startswith('AAB1')):
           rigName = x
    print("Rig Name: " + rigName)
    return rigName

def parseUptime():
    uptime = ''
    with open("stats_sys_uptime.sent", "r") as f:
        for line in f:
            uptime = line
    print("Rig Uptime:" + uptime)
    return uptime

# TODO:improve formatting for temp
def parseTemp():
    temp = []
    with open("stats_gpu_temp_jq.sent", "r") as f:
        for lines in f:
            temp.append(lines)
    print(temp)
    return temp

def parseGPUCount():
    count = ''
    with open("stats_gpu_count.sent", "r") as f:
        for lines in f:
            count = lines
    print("Rig GPU Count:" + count)
    return count

def parseHashrate():
    loglines = []
    hashrate = ''
    with open("screen.miner.log", 'r') as f:
        for lines in f:
            loglines.append(lines)
        loglines.reverse()

        for i in range(1, 15):
            if("Eth speed: " in loglines[i]):
                hashrate = loglines[i][10:17]
    print("Rig Hash Rate:" + hashrate)
    return hashrate