import tests.mockdata
import requests
from pykml import parser
import re

def getCoordinatesNamespaces(root):
    coordinatesNamespaces = []
    dp = root.descendantpaths()
    for d in dp:
        if re.match(r'.*coordinates$', d):
            print d
            ns = re.sub('{http://www.opengis.net/kml/2.2}', '', d)
            print ns
            print type(ns)
            coordinatesNamespaces.append(ns)

    return coordinatesNamespaces

def getKML(url):
    r = requests.get(url)
    rawKML = r.content
    root = parser.fromstring(rawKML)

    tree = objectify.fromstring(rawKML)
    coordinatesNamespaces = getCoordinatesNamespaces(root)
    print "Found %s coordinate namespaces, and they are:" % len(coordinatesNamespaces)

    for c in coordinatesNamespaces:
        try:
            coords = getattr(root, c) 

            # Clean up padding whitespace
            c = re.sub('\s*', '', c)

            coords = c.split(',')
            # Remove leading zeroes from negative values, since float() fails on that format.
            coords = [re.sub('^0-', '-', c) for c in coords]
            # Convert all numbers to floats
            coords = [float(c) for c in coords]

            return coords

        except AttributeError, e:
            print e

if __name__ == '__main__':
    getKML(tests.mockdata.KMLURL)
