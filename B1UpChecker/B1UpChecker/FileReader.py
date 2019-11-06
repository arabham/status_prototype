import re

def main():
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
    def fileReader(file):
          with open(file, 'r') as reader:
              fileToStr = reader

          print(fileToStr)

    #loglines = []
    #rigStatus = 'Online'
    #with open ('screen.miner.log', 'r') as screenminerlog:
    #    for logline in screenminerlog:
    #        loglines.append(logline)   
    #loglines.reverse()
    #for num, lines in enumerate(loglines):
    #    if 'time:' in loglines[num]:
    #        print(loglines[num])
            
    #        statusString = loglines[num]
    #        break
    #print(re.findall('\d+', statusString))

if __name__ == "__main__":
    main()