import ipaddress
import json
import requests

def getMyLoc():
    """
    this return: IP , lon , lat , city
    """
    url = 'https://ipapi.co/json'
    response = requests.get(url)
    data = response.json()
    try:
        myIP = data['ip']
        lat = data.get('latitude')
        lon = data.get('longitude')
        city = str(data.get('city'))
    except KeyError as e:
        print(f'Error on my: {e} Not Found man')
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
        lon = data['longitude']
        lat = data.get('latitude')
        city = str(data.get('city'))
    except KeyError as e:
        print(f'Error on target: {e} Not Found man')
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


        lat = data.get('latitude')
        lon = data.get('longitude')
        if lon == None or lat == None:
            continue
        city = str(data.get('city'))

        List.append((ipAddress, (lon, lat), city))

    return List
