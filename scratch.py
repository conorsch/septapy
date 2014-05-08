import tests.mockdata
import requests
from pykml import parser
import re

def getCoordsFromRoot(root):
    coords = list()
    for c in root.Document.Placemark.MultiGeometry.getchildren():
        coords.append(c.coordinates)
    return coords

def getKML(url):
    r = requests.get(url)
    rawKML = r.content
    root = parser.fromstring(rawKML)
    coordsRaw = getCoordsFromRoot(root)
    coordsClean = list()

    for c in coordsRaw:

        # Clean up padding whitespace
        c = re.sub('\s*', '', str(c))
        coords = c.split(',')

        # Remove leading zeroes from negative values, since float() fails on that format.
        coords = [re.sub('^0-', '-', c) for c in coords]
        # Convert all numbers to floats
        coords = [float(c) for c in coords]

        coordsClean.append(coords)

    return coordsClean


if __name__ == '__main__':
    getKML(tests.mockdata.KMLURL)
