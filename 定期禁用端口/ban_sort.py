# encoding: utf-8
import os

socks = [824,2078,6667,10086]
def ban(socks):
    for sock in socks:
        print(os.system("sudo iptables -A INPUT -p tcp --dport {0} -j DROP".format(sock)))

if __name__ == '__main__':
    ban(socks)