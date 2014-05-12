import tests.mockdata
import requests
from pykml import parser
import re
import pylab

def cleanCoordinates(coordsRaw):

    # Clean up padding whitespace
    c = re.sub('\s*', '', str(coordsRaw))
    coords = c.split(',')

    # Remove leading zeroes from negative values, since float() fails on that format.
    coords = [re.sub('^0-', '-', c) for c in coords]
    # Convert all numbers to floats
    coords = [float(c) for c in coords]

    # Default KML structure appends '0.0' to all lines, so remove those noisy values
    coords = filter(lambda x: x != 0.0, coords)

    return coords


def extractCoordinatesFromKML(rawKML):
    root = parser.fromstring(rawKML)
    coords = list()
    for c in root.Document.Placemark.MultiGeometry.getchildren():
        c = cleanCoordinates(c.coordinates)
        for d in c:
            coords.append(d)

    return coords

def convertListOfCoordsToTuples(listOfCoords):
    l = [(x, y) for x, y in zip(*[iter(listOfCoords)]*2)]
    print l
    return l


def plotCoords(listOfCoords):
    coords = convertListOfCoordsToTuples(listOfCoords)
    x = [x[0] for x in coords]
    y = [y[0] for y in coords]
#    print "X values:"
#    print x
    color=['m','g','r','b']
    pylab.scatter(x,y, s=100, marker='o', c=color)
    pylab.show()


def getKML(url):
    print "Getting KML..."
    r = requests.get(url)
    rawKML = r.content
    
    coords = extractCoordinatesFromKML(rawKML)
    plotCoords(coords)

    return rawKML
    return coordsClean


if __name__ == '__main__':
    getKML(tests.mockdata.KMLURL)
