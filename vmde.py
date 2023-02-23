import os
from operation impmort *

def main():
    print "STARTING DIAGNOSIS"
    print "\n"
    print "  Distribution : ", open("/proc/sys/kernel/ostype").read()
    print "  OS: ", open("/etc/lsb-release").read()[85:103]
    print "  Kernel Version :", open("/proc/sys/kernel/osrelease").read()
    print "  Host name: ",open("/proc/sys/kernel/hostname").read()
    
    print "  Presence of Virtual Machine: "
	presence()
	print "\n"
	
	print "Checking VM Elements"
	
	print "\t Hypervisor Flag"
	flags()
	
	print "\t Checking SCSI "
	scsi()
	
	print "\t Checking MAC Address "
	mac()
	
	print "\t Checking bi0s Vendor "
	bios_vendor()
	
	print "\t Checking Product Name "
	product_vendor()
	
	print "\t Checking System Vendor "
	sys_vendor()
	
	print "\t Checking Board Vendor "
	board_vendor()
	
	print "\t Checking Loadable Kernel Modules "
	kernel_modules()






if __name__ == "__main__":
	main()
