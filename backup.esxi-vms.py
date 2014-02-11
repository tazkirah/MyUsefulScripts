#!/usr/bin/python

# author: Paulino Padial
# software-base (dependencies)
#       bazaarvcb:      http://www.magiksys.net/bazaarvcb/index.html

import subprocess
import shutil

#<!--// VARS
# Path to bazaarvcb script
bazaarvcb='/root/bazaarvcb-0.9.7b-linux-x86_64/bazaarvcb'
# Path to Folder where you want to store backups
backupRoot='/mnt/backup/virtual-machines/'
esxiCredentials=['esxi-user','esxi-password']
# Number of backups to store before do rollUp
rollOut=1

data = dict()                   # ESXI_SERVER   VM1,VM2,VM3
data['esxi-server-1'] = []
data['esxi-serer-1'].append('yourvirtualmachinetobackup')
#data['esxi-server-2'] = []
#data['esxi-serer-2'].append('yourvirtualmachinetobackup')
#data['esxi-serer-2'].append('yourvirtualmachinetobackup2')

#<!--// SCRIPT

# Copy script because bug that binary is corrupted...
# Info: When i use sometimes bazaarvcb binary, this fails with segmentation fault, when i copy from original again
#   all works... this is a workaround
shutil.copy2(bazaarvcb, '/bin/bazaarvcb')

# Do backups
for esxi in data:
        for vm in data[esxi]:
                print "Backing up " + vm + " of " + esxi + "..."
                p = subprocess.Popen([
                                        'bazaarvcb',
                                        'backup',
                                        '-H',
                                        esxi,
                                        '-l','/tmp/esxi-backup-using-script.log','--shutdown','--poweron-after',
                                        '-u',
                                        esxiCredentials[0],
                                        '-p',
                                        esxiCredentials[1],
                                        '--roll-out',
                                        str(rollOut),
                                        '--consolidate',
                                        vm,
                                        backupRoot
                                      ],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT)

                # Real-time command output printing
                for line in iter(p.stdout.readline,''):
                        print line
# //--!>
