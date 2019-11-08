import pysftp

def ftpLogs(rigIP):
    cnopts = pysftp.CnOpts()
    rusername = 'root'
    rpassword = 'kingaliamer@gmail.com'
    cnopts.hostkeys = None  
    try:
        with pysftp.Connection(host=rigIP, username=rusername, password=rpassword, cnopts=cnopts) as sftp:
            remoteNamePath = '/home/miner/config.json'
            remoteUptimePath = '/var/tmp/stats_sys_uptime.sent'
            remoteTempPath = '/var/tmp/stats_gpu_temp_jq.sent'
            remoteGPUCountPath = '/var/tmp/stats_gpu_count.sent'
            remoteHashRatePath = '/var/tmp/screen.miner.log'
            localNamePath = './name.miner.log'
            localUptimePath = './stats_sys_uptime.sent'
            localTempPath = './stats_gpu_temp_jq.sent'
            localGPUCountPath = './stats_gpu_count.sent'
            localHashRatePath = './screen.miner.log'

            # check name file paths
            if exists(remoteNamePath):
                if exists(localNamePath):
                    sftp.get(remoteNamePath, localNamePath)
                else:
                    print("local name file path does not exist!")
            else:
                print("remote name file path does not exist!")

            # check uptime file paths
            if exists(remoteUptimePath):
                if exists(localUptimePath):
                    sftp.get(remoteUptimePath, localUptimePath)
                else:
                    print("local uptime file path does not exist!")
            else:
                print("remote uptime file path does not exist!")

            # check temp file path
            if exists(remoteTempPath):
                if exists(localTempPath):
                    sftp.get(remoteTempPath, localTempPath)
                else:
                    print("local temp file path does not exist!")
            else:
                print("remote temp file path does not exist!")

            # check gpu count file path
            if exists(remoteGPUCountPath):
                if exists(localGPUCountPath):
                    sftp.get(remoteGPUCountPath, localGPUCountPath)
                else:
                    print("local gpu count file path does not exist!")
            else:
                print("remote gpu count file path does not exist!")

            # check hash rate file path
            if exists(remoteHashRatePath):
                if exists(localHashRatePath):
                    sftp.get(remoteHashRatePath, localHashRatePath)
                else:
                    print("local hash rate path does not exist!")
            else:
                print("remote hash rate path does not exist!")

    except:
        print("failed to connect to server!")