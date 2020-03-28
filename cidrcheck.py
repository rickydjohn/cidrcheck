#!/usr/bin/python

import argparse


class ipconvert:
    
    def __init__(self, cidr):
        self.cidr = cidr
        self.ip = None
        self.notation = None
        self.mask = None
        self.fip = None
        self.lip = None

    def f_lastip(self, msk, fip):
        lip = []
        for i,v in enumerate(msk):
            lip.append(255 - (msk[i] - fip[i]))
        return lip
    
    def f_firstip(self, nmsk):
        fip = []
        for i,v in enumerate(nmsk):
            fip.append(nmsk[i] & self.ip[i])
        return fip
    
    def netmask(self):
        nmsk = [0,0,0,0]
        used = self.notation // 8
        remain = self.notation % 8
        for i in range(used):
            nmsk[i] = 255
        if used < 4:
            nmsk[used] = 256 - (256 >> remain)
        return nmsk

    def compare(self, ip):
        i = map(int, ip.split("."))
        f = self.fip
        l = self.lip
        for i, v in enumerate(i):
            if v >= f[i] and v <= l[i]:
                continue
            else:
                return False
        return True

    def getdata(self):
        ips = self.cidr.split("/")
        self.ip = map(int, ips[0].split("."))
        self.notation = int(ips[1])
        nmsk = self.netmask()
        self.mask = nmsk
        fip = self.f_firstip(nmsk)
        self.fip = fip
        lip = self.f_lastip(nmsk, fip)
        self.lip = lip
        return {
                "fip": ".".join(map(str, fip)),
                "lip": ".".join(map(str, lip)),
                "nmsk": ".".join(map(str, nmsk)),
                "total": 2**(32 - self.notation)
                }
    

if __name__ == "__main__":
    args = argparse.ArgumentParser("A Program to calculate IP range")
    args.add_argument("-i", help="supply IP address in CIDR notation. eg:10.0.0.0/8")
    args.add_argument("-c", help="supply IP address to be checked. eg:10.0.0.0/8")
    arg = args.parse_args()
    ipm = ipconvert(arg.i)
    if arg.i and not arg.c:
        d = ipm.getdata()
        print
        print "FIRST IP  :", d["fip"]
        print "LAST  IP  :", d["lip"]
        print "NMASK IP  :", d["nmsk"]
        print "TOTAL IPs :", d["total"]
        print
    elif arg.i and arg.c:
        d = ipm.getdata()
        print
        print "FIRST IP  :", d["fip"]
        print "LAST  IP  :", d["lip"]
        print "NMASK IP  :", d["nmsk"]
        print "TOTAL IPs :", d["total"]
        print
        if ipm.compare(arg.c):
            print "IP belongs to the subnet"
            print 
        else:
            print "IP does not belong to the subnet"
            print 


