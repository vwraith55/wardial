'''
This is a lab for CSCI040.
Complete the lab by fixing the FIXME annotations below.
'''

import requests

def is_server_at_hostname(hostname):
    '''
    >>> is_server_at_hostname('google.com')
    True
    >>> is_server_at_hostname('www.google.com')
    True
    >>> is_server_at_hostname('GoOgLe.CoM')
    True
    >>> is_server_at_hostname('142.250.68.110')
    True
    >>> is_server_at_hostname('facebook.com')
    True
    >>> is_server_at_hostname('www.facebook.com')
    True
    >>> is_server_at_hostname('FACEBOOK.com')
    True
    >>> is_server_at_hostname('google.commmm')
    False
    >>> is_server_at_hostname('aslkdjlaksjdlaksjdlakj')
    False
    >>> is_server_at_hostname('142.250.68.110.1.3.4.5')
    False
    >>> is_server_at_hostname('8.8.8.8')
    False
    '''
    try:
        r = requests.get('http://' + hostname, timeout=5)
        return True
    except Exception:
        return False


def increment_ip(ip):
    '''
    >>> increment_ip('1.2.3.4')
    '1.2.3.5'
    >>> increment_ip('1.2.3.255')
    '1.2.4.0'
    >>> increment_ip('0.0.0.0')
    '0.0.0.1'
    >>> increment_ip('0.0.0.255')
    '0.0.1.0'
    >>> increment_ip('0.0.255.255')
    '0.1.0.0'
    >>> increment_ip('0.255.255.255')
    '1.0.0.0'
    >>> increment_ip('0.255.5.255')
    '0.255.6.0'
    >>> increment_ip('255.255.255.255')
    '0.0.0.0'
    '''
    parts = [int(x) for x in ip.split('.')]
    parts[3] += 1
    for i in range(3, 0, -1):
        if parts[i] == 256:
            parts[i] = 0
            parts[i-1] += 1
    parts[0] = parts[0] % 256
    return '.'.join(str(p) for p in parts)


def enumerate_ips(start_ip, n):
    '''
    >>> list(enumerate_ips('192.168.1.0', 2))
    ['192.168.1.0', '192.168.1.1']
    >>> list(enumerate_ips('8.8.8.8', 10))
    ['8.8.8.8', '8.8.8.9', '8.8.8.10', '8.8.8.11', '8.8.8.12', '8.8.8.13', '8.8.8.14', '8.8.8.15', '8.8.8.16', '8.8.8.17']
    >>> list(enumerate_ips('192.168.0.255', 2))
    ['192.168.0.255', '192.168.1.0']
    >>> len(list(enumerate_ips('8.8.8.8', 10)))
    10
    >>> len(list(enumerate_ips('8.8.8.8', 1000)))
    1000
    >>> len(list(enumerate_ips('8.8.8.8', 100000)))
    100000
    '''
    ip = start_ip
    for _ in range(n):
        yield ip
        ip = increment_ip(ip)


if __name__ == '__main__':

    # FIXME 1: Generate all DPRK IPs
    dprk_ips = list(enumerate_ips('175.45.176.0', 1024))

    # FIXME 2: Filter to only IPs with web servers
    dprk_ips_with_servers = []
    for ip in dprk_ips:
        print('scanning:', ip)
        if is_server_at_hostname(ip):
            dprk_ips_with_servers.append(ip)

    print('dprk_ips_with_servers=', dprk_ips_with_servers)