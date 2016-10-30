#!/usr/bin/env python3
import time
import requests
import horetu

url = 'https://wifigw.cis.vutbr.cz/login.php'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

def status():
    '''
    Check whether you are connected to the internet.
    '''
    r = requests.get(url, headers=headers)
    connected = 'input type="password"' not in r.text
    return {True:'connected', False:'not connected'}[connected]

def connect(user=None, password=None):
    '''
    Connect to the internet.
    '''
    if not user:
        user = input('Username: ')
    if not password:
        password = input('Password: ')
    requests.post(url, headers=headers,
                  data='user=%s&auth=any&password=%s' % (user, password))

def disconnect():
    '''
    Disconnect from the internet.
    '''
    requests.post(url, headers=headers, data='logout=1')

def watch(user=None, password=None, n=60, verbose=False):
    '''
    Poll the internet connection periodically, and reconnect if the
    connection is down.

    :param n: Seconds to sleep
    '''
    if not user:
        user = input('Username: ')
    if not password:
        password = input('Password: ')
    while True:
        try:
            s = status()
            if verbose:
                print(s)
            if s == 'not connected':
                connect(user=user, password=password)
            time.sleep(n)
        except KeyboardInterrupt:
            break

def main():
    horetu.cli([connect, disconnect, status, watch],
               config=os.path.expand('~/.vutwifi.conf'))

if __name__ == '__main__':
    main()
