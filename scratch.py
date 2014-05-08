import tests.mockdata
import requests
from pykml import parser
import re

def cleanCoordinates(coordsRaw):

    # Clean up padding whitespace
    c = re.sub('\s*', '', str(coordsRaw))
    coords = c.split(',')

    # Remove leading zeroes from negative values, since float() fails on that format.
    coords = [re.sub('^0-', '-', c) for c in coords]
    # Convert all numbers to floats
    coords = [float(c) for c in coords]
    return coords


def extractCoordinatesFromKML(rawKML):
    root = parser.fromstring(rawKML)
    coords = list()
    for c in root.Document.Placemark.MultiGeometry.getchildren():
        c = cleanCoordinates(c.coordinates)
        coords.append(c)

    return coords

def getKML(url):
    r = requests.get(url)
    rawKML = r.content
    return rawKML
    

    
    coords = extractCoordinatesFromKML(rawKML)
    return coordsClean


if __name__ == '__main__':
    getKML(tests.mockdata.KMLURL)
