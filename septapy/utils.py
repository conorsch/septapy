import math
import requests
from pykml import parser
import re

def getDistance(lat1, long1, lat2, long2):
    """Returns distance between two sets of latitude and longitude"""

    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
        
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
        
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
        
    # Compute spherical distance from spherical coordinates.
        
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
    
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )

    # Remember to multiply arc by the radius of the earth 
    # in your favorite set of units to get length.
    return arc

def getKML(url):
    r = requests.get(url)
    rawKML = r.content

    root = parser.fromstring(rawKML)
    s = str(root.Document.Placemark.MultiGeometry.LineString.coordinates)

    # Clean up padding whitespace
    s = re.sub('\s*', '', s)

    coords = s.split(',')
    # Remove leading zeroes from negative values, since float() fails on that format.
    coords = [re.sub('^0-', '-', c) for c in coords]
    # Convert all numbers to floats
    coords = [float(c) for c in coords]
    return coords

def trolleyRoutes():
    """Returns list of valid trolley route identifiers, e.g. ['10', '13', '34', '36']"""
    return "10 13 34 36".split()
