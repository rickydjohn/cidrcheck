
# cidrcheck
### simple python script to check if the given IP belong to the CIDR provided.

This script will check if a given IP address belong to the subnet range provided in CIDR (classless inter-domain routing) notation. This was asked as an interview question.

How to use the script:
  This script uses two switches (-i, -c)
  1. with -i switch, the script returns the range and number of IPs in the subnet.

>    		                cidrcheck.py  -i 10.32.55.12/17
> 				FIRST IP     : 10.32.0.0
> 				LAST  IP     : 10.32.127.255
> 				NMASK IP  : 255.255.128.0
> 				TOTAL IPs  : 32768

  2. with -i and -c switch, the script checks if the given ip in -c belong to the range provided in -i
      ex:

> 				 cidrcheck.py  -i 10.32.55.12/17 -c 10.28.55.12
> 				 FIRST IP     : 10.32.0.0
> 				 LAST  IP     : 10.32.127.255
> 				 NMASK IP  : 255.255.128.0
> 				 TOTAL IPs  : 32768
> 				 IP does not belong to the subnet        IP does not belong to the subnet

				 
