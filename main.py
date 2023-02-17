import sys
import plot
import socket
from plot import *
from getloc import *
from help import *
from tracer import traceroute


#get hostname from parse
if len(sys.argv) < 2:
    printHelp()
    exit()

hostname = sys.argv[1]

myLoc = getMyLoc()

# get target loc IP, (lon, lat), city
targetIP = socket.gethostbyname(hostname)
targetLoc = getTargetLoc(targetIP)

# traceroute process to hostname and output the ipList
ipList = traceroute(hostname)

# get geo loc of ipList and insert myLoc and IpTarget
routeLocList = getListLoc(ipList)
routeLocList.insert(0, myLoc)
routeLocList.append(targetLoc)

# prepare for and linear route in map
routeLocaLon = []
routeLocLat = []
tempLon = 0
tempLat = 0

for x in routeLocList:
    # loop until drop route with zero movement
    if x[1][0]-tempLon == 0 or x[1][1]-tempLat == 0:
        continue
    routeLocaLon.append(x[1][0])
    routeLocLat.append(x[1][1])


# init temp map
fig = go.Figure()
mapsInit(fig)

# creating route
for i in range(len(routeLocaLon)-1):
    for x in routeLocList:
        if (routeLocaLon[i], routeLocLat[i]) in x:
            route_city = x[2]
            route_ip = x[0]
    print(route_ip, '---', route_city)
    addRoute(fig, f'route{i}', ((routeLocaLon[i:i+2], routeLocLat[i:i+2]), route_city))
print(targetLoc[0],'----', targetLoc[2])


# marking myIp and ttarget Ip

mark(fig , f'My IP - {myLoc[2]}', myLoc[1])
mark(fig, f'{hostname} - {targetLoc[2]}', targetLoc[1], name=hostname)


fig.show()
