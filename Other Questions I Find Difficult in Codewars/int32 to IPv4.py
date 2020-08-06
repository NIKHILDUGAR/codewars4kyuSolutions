#BIT MANIPULATION SOLUTION
def int32_to_ip(int32):
    return str(int32 >> 24 & 0xFF)+'.'+str(int32 >> 16 & 0xFF)+'.'+str(int32 >>  8 & 0xFF)+'.'+str(int32& 0xFF)
    
#ANOTHER SOLUTION

from ipaddress import IPv4Address

def int32_to_ip(int32):
    return str(IPv4Address(int32))
