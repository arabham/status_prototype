import pysftp

def ftpLogs(rigIP):
	cnopts = pysftp.CnOpts()
	rusername = 'root'
	rpassword = 'arabham110@gmail.com'
	cnopts.hostkeys = None  
    try:
        with pysftp.Connection(host=rigIP, username=rusername, password=rpassword, cnopts=cnopts) as sftp:
            remoteNamePath = '/home/miner/config.json'
            remoteUptimePath = '/var/tmp/stats_sys_uptime.sent'
            remoteTempPath = '/var/tmp/stats_gpu_temp_jq.sent'
            remoteGPUCountPath = '/var/tmp/stats_gpu_count.sent'
            remote
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