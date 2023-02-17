import ipaddress
import json
import requests

def getMyLoc():
    """
    this return: IP , lon , lat , city
    """
    url = 'http://ip-api.com/json/'
    response = requests.get(url)
    data = response.json()
    try:
        myIP = data['query']
        lon = data['lon']
        lat = data['lat']
        city = data['city']
    except KeyError as e:
        print(f'Error: {e} Not Found man')
        exit()
    
    return (myIP , (lon, lat) , city)

def getTargetLoc(IP):
    """
    IP = obviusly target IP
    return = lon , lat, city
    """
    url = f'https://ipapi.co/{IP}/json'
    response = requests.get(url)
    data = response.json()
    try:
        lon = data['lon']
        lat = data['lat']
        city = data['city']
    except KeyError as e:
        print(f'Error: {e} Not Found man')
        exit()
    
    return (IP , (lon, lat), city)

def getListLoc(ipList):
    """
    As the name this is 4 search a list of ip
    ipList = (tuple/list) of ip
    return = (list) (ipAddress, lon, lat, city)
    """
    List = []

    for ipAddress in ipList:
        url = f'https://ipapi.co/{ipAddress}/json'
        response = requests.get(url)
        data = response.json()

        # if IP is private
        try:
            if ['error'] == True:
                continue
        except KeyError:
            pass

        lon = data['lon']
        lat = data['lat']
        if lon == None or lat == None:
            continue
        city = data['city']

        List.append((ipAddress, (lon, lat), city))

    return List
