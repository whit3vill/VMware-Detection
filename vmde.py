import os
import uuid

def printVal(val):
	if (val == 0):
		print '\t\t \033[1;31mDetected!\033[1;m'
	else:
		print '\t\t \033[1;32mPASS\033[1;m'
		
def VMDirCheck():
	list_dir = os.listdir("/usr/bin/")
	vmdir = "vmware-"
	if (any(vmdir in s for s in list_dir) == True):
		print '\t\t \033[1;31m'+vmdir+' Detected!\033[1;m'
	else:
		printVal(1)
		
def flagCheck():
	if 'hypervisor' in open("/proc/cpuinfo").read():
		printVal(0)
	else:
		printVal(1)
		
def scsiCheck():
	list_dir = open("/proc/scsi/scsi").read().split(" ")
	vmdir = "VMware"
	if (any(vmdir in s for s in list_dir) == True):
		print '\t\t \033[1;31m'+vmdir+' Detected!\033[1;m'
	else:
		printVal(1)
		
def macCheck():
	VMmac=['00:05:69','00:0c:29','00:0C:29','00:1C:14','00:1c:14','00:50:56']
	flag = 0
    
	mac = ':'.join(("%012X" % uuid.getnode())[i:i+2] for i in range(0, 12, 2))
	macc = mac[0:8]
        
	for i in VMmac:
		if (i == macc):
			print '\t\t \033[1;31mVMWare Detected! MAC Address : '+mac+'\033[1;m'
			flag = 1
    
	if (flag == 0):
		printVal(1)
		
def biosvendorCheck():
    bios_vendor = open("/sys/class/dmi/id/bios_vendor").read()
    lists = {"vmware", "Phoenix", "innotek"}
    flag = 0
    
    for i in lists:
        if (bios_vendor.find(i) != -1):
            print '\t\t \033[1;31m'+i+' Detected!\033[1;m'
            flag = 1
    if (flag == 0):
        printVal(1)

def boardvendorCheck():
    board_vendor = open("/sys/class/dmi/id/board_vendor").read()
    lists = {"VMware", "Phoenix", "innotek", "Oracle"}
    flag = 0
    
    for i in lists:
        if (board_vendor.find(i) != -1):
            print '\t\t \033[1;31m'+i+' Detected!\033[1;m'
            flag = 1
    if (flag == 0):
        printVal(1)         
        
def productnameCheck():
    product_name = open("/sys/class/dmi/id/product_name").read()
    lists = {"VMware", "Phoenix", "innotek"}
    flag = 0
    
    for i in lists:
        if (product_name.find(i) != -1):
            print '\t\t \033[1;31m'+i+' Detected!\033[1;m'
            flag = 1
    if (flag == 0):
        printVal(1)   
        
def sysvendorCheck():
    sys_vendor = open("/sys/class/dmi/id/sys_vendor").read()
    lists = {"VMware", "Phoenix", "innotek"}
    flag = 0
    
    for i in lists:
        if (sys_vendor.find(i) != -1):
            print '\t\t \033[1;31m'+i+' Detected!\033[1;m'
            flag = 1
    if (flag == 0):
        printVal(1)

def kernelModulesCheck():
    modules = open("/proc/modules").read()
    lists = {"vmw_balloon", "vmwfgx"}
    flag = 0
    
    for i in lists:
        if (modules.find(i) != -1):
            print '\t\t \033[1;31m'+i+' Detected!\033[1;m'
            flag = 1
    if (flag == 0):
        printVal(1)       
        
def main():
    print "STARTING DIAGNOSIS"
    print "\n"
    print "  Distribution : ", open("/proc/sys/kernel/ostype").read()
    print "  OS: ", open("/etc/lsb-release").read()[85:103]
    print "  Kernel Version :", open("/proc/sys/kernel/osrelease").read()
    print "  Host name: ",open("/proc/sys/kernel/hostname").read()
    
    print "  Presence of Virtual Machine: "
	VMDirCheck()
	print "\n"
	
	print "Checking VM Elements"
	
	print "\t Hypervisor Flag"
	flagCheck()
	
	print "\t SCSI "
	scsiCheck()
	
	print "\t MAC Address "
	macCheck()
	
	print "\t Bios Vendor "
	biosvendorCheck()

	print "\t Board Vendor "
	boardvendorCheck()
    
	print "\t Product Name "
	productnameCheck()
	
	print "\t System Vendor "
	sysvendorCheck()
	
	print "\t Loadable Kernel Modules "
	kernelModulesCheck()

if __name__ == "__main__":
	main()
