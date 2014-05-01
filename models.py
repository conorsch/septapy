from django.db import models
import math
import requests

class Route(models.Model):

    route = models.SlugField()
    identifier = models.SlugField()

    def __init__(self, identifier=None):
        self.identifier = str(identifier)

    def __unicode__(self):
        return "Route " + self.identifier

    def vehicles(self):
        vehicleURL = 'http://www3.septa.org/transitview/bus_route_data/' + self.identifier
        try:
            r = requests.get(vehicleURL)
        except:
            raise Exception("FAILED GET ON VEHICLES FOR ROUTE '%s'" % self.identifier)

        j = r.json()
        vehicles = j[j.keys()[0]]
        return [Vehicle(v, route=self.identifier) for v in vehicles]

    def stops(self):
        stopsURL = 'http://www3.septa.org/hackathon/Stops/' + self.identifier
        r = requests.get(stopsURL)
        j = r.json()
        return [Stop(s, route=self.identifier) for s in j]

    def findNearestStop(self, latitude, longitude):
        stops = self.stops()
        stops.sort(key=lambda s: self.getDistance(s.latitude, s.longitude, latitude, longitude))
        return stops[0]

    def findNearestVehicle(self, latitude, longitude):
        vehicles = self.vehicles()
        vehicles.sort(key=lambda v: self.getDistance(v.latitude, v.longitude, latitude, longitude))
        return vehicles[0]

    def getDistance(self, lat1, long1, lat2, long2):
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

class Stop(object):
    def __init__(self, jsonArgs, route=None):

        self.latitude = jsonArgs['lat']
        self.longitude = jsonArgs['lng']
        self.coords = (self.latitude, self.longitude)
        self.stopID = jsonArgs['stopid']
        self.name = jsonArgs['stopname']
        self.title = self.name
        self.route = route

    def __str__(self):
        representation = """\
Route: %(route)s
Stop Name: %(stopName)s
Stop ID: %(stopID)s
Location: %(lat)s, %(long)s
""" % {
                'route': self.route,
                'stopName': self.name,
                'stopID': self.stopID, 
                'lat': self.latitude,
                'long': self.longitude,
                }

        return representation

class Vehicle(object):
    def __init__(self, jsonArgs, route=None):

        self.latitude = float(jsonArgs['lat'])
        self.longitude = float(jsonArgs['lng'])
        self.coords = (self.latitude, self.longitude)
        self.vehicleID = jsonArgs['VehicleID']
        self.blockID = jsonArgs['BlockID']
        self.direction = jsonArgs['Direction']
        self.label = jsonArgs['label']
        self.title = self.label
        self.offset = jsonArgs['Offset']
        self.destination = jsonArgs['destination']
        self.route = route

    def __unicode__(self):
        representation = """\
Route: %(route)s
Current location: %(lat)s, %(long)s
Heading: %(heading)s
Next stop: %(destination)s
""" % {
                'route': self.route,
                'lat': self.latitude,
                'long': self.longitude, 
                'heading': self.direction,
                'destination': self.destination,
                }

        return representation
