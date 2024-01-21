class cidr:
    def __init__(self, cidr, ip=None):
        self.cidr = cidr
        self.validate = ip

    def iptoint(self, ip: list):
        if len(ip) != 4:
            raise("incorrect ip")
        return ip[0] << 24 | ip[1] << 16 | ip[2] << 8 | ip[3]

    def intToIp(self, ip:int):
        ip_address = ""
        for i in [24, 16, 8, 0 ]:
            if i != 0:
                ip_address+=str((ip >> i) & 255) + "."
            else:
                ip_address+=str((ip >> i) & 255)
        return ip_address

    def netmask(self, cidr_notation: int):
        cidr = [0,0,0,0]
        used = cidr_notation // 8
        remain = cidr_notation % 8
        for i  in range(used):
            cidr[i] = 255
        for j in range(1, remain+1):
            cidr[used] += 1 << (8 - j)
        return self.iptoint(cidr)

    def build_cidr(self):
        ip, cidr_notation = self.cidr.split("/")
        if ip == "" or cidr_notation == "":
            raise("Invalid format provided")
        netmask = self.netmask(int(cidr_notation))
        network_id = netmask & self.iptoint(list(map(int, ip.split("."))))

        #https://stackoverflow.com/questions/32940991/how-to-find-first-and-last-ip-address-from-a-given-subnet
        broadcast = network_id | ~netmask

        print(f"NetID: %s\nNMask: %s\nBcast: %s" %(
            self.intToIp(network_id), 
            self.intToIp(netmask),
            self.intToIp(broadcast)
            ))
        
        if self.validate:
            check_ip = self.iptoint(list(map(int, self.validate.split("."))))
            if (check_ip & netmask) == (network_id & netmask):
                print(f"%s ip belongs to above subnet" %(self.intToIp(check_ip)))
            else:
                print(f"ERROR: %s does not belongs to above subnet" %(self.intToIp(check_ip)))

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        cidr(sys.argv[1]).build_cidr()
    elif len(sys.argv) == 3:
        cidr(sys.argv[1], sys.argv[2]).build_cidr()
