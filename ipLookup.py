import urllib.request 
from urllib.request import urlopen
import json
import re
import socket

# check if the ip address is valid
def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True

# check each key has value
def getEachInfo(info, keyValue, keyStr):
    try: 
        info[keyValue]
    except KeyError:
        return
    else:
        print (keyStr + ": " + str(info[keyValue]))
        
# get response from page: "http://ipinfo.io/ip_address/json"
# and print out all info
def getInfo(ip_address):
    url = 'http://ipinfo.io/' + ip_address + '/json'
    response = urlopen(url)
    info = json.load(response)
    getEachInfo(info, 'ip','IP')
    getEachInfo(info, 'city','City')
    getEachInfo(info, 'region','Region')
    getEachInfo(info, 'country','Country')
    getEachInfo(info, 'location','Location')
    getEachInfo(info, 'org','Org')
    getEachInfo(info, 'postal','Postal')
    getEachInfo(info, 'bogon','Bogon IP address')

def main():
    # get the ip address from user
    ip_address = input('Please enter a valid IP address:')
    if is_valid_ipv4_address(ip_address):
        getInfo(ip_address)
    else:
        main()
    
if __name__ == '__main__':
    main()