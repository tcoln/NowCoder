import sys
line = sys.stdin.readline().strip().split(':')
cmd = int(line[0])
content = line[1]
rings = [0]*1000
for i in range(20):
    rings[i*50] = 1

def hashServer(content):
    if content[-2] == '0':
        redis = int(content[-1])
    else:
        redis = int(content[-2:])
    return 50*(redis-1)

def findServer(deads, content):
    asc = 0
    for c in content:
        asc += ord(c)
    asc %= 1000
    print deads
    for d in deads:
        rings[d] = 0
    for i in range(1000): 
	if rings[i] != 0: 
		print i
    while rings[asc] != 1:
        asc += 1
        if asc >= 1000:
            asc = 0
    return asc

def hashServer(content):
    if content[-2] == '0':
        redis = int(content[-1])
    else:
        redis = int(content[-2:])
    return 50*(redis/2) + (25 if redis%2==1 else 525)

if cmd == 1:    
    print hashServer(content)
elif cmd == 2:
    print findServer('', content)
elif cmd == 3:
    print content
    dtoken = content.split(';')
    deads = [hashServer(d) for d in dtoken[0].split(',')]
    token = dtoken[1]
    asc = findServer(deads, token)
    print asc
