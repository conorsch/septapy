import tests.mockdata
import requests
from pykml import parser
import re

def getCoordinatesNamespaces(rawKML):
    root = parser.fromstring(rawKML)
    results = []
    dp = root.descendantpaths()
    regex = re.compile('{http://www.opengis.net/kml/2.2}kml.')
    for d in dp:
        if re.match(r'.*coordinates$', d):
            ns = re.sub(regex, '', d)
            results.append(ns)

    return results

def getKML(url):
    r = requests.get(url)
    rawKML = r.content

    coordinatesNamespaces = getCoordinatesNamespaces(rawKML)
    print coordinatesNamespaces
    s = ','.join(coordinatesNamespaces)
    print s

    # Clean up padding whitespace
    s = re.sub('\s*', '', s)

    coords = s.split(',')
    # Remove leading zeroes from negative values, since float() fails on that format.
    coords = [re.sub('^0-', '-', c) for c in coords]
    # Convert all numbers to floats
    coords = [float(c) for c in coords]
    return coords

if __name__ == '__main__':
    getKML(tests.mockdata.KMLURL)
