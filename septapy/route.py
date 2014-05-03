import re
import requests
import stop, trip, vehicle, utils

class Route(object):
    """Represents a path that a Vehicle can take. Can list related objects 
    such as:

    .vehicles
    .stops

    It also provides helper methods for common operations, e.g.:

    .findNearestStop

    """

    def __init__(self, identifier=None):
        # Ensure we have a string, for concatenation, rather than an integer.
        self.identifier = str(identifier)
        self.routeLineURL = 'http://www3.septa.org/transitview/kml/%s.kml' % self.identifier

    def __unicode__(self):
        return "Route " + self.identifier

    def vehicles(self):
        return vehicle.getVehiclesByRoute(self.identifier)

    def stops(self):
        return stop.getStopsByRoute(self.identifier)

    def trips(self):
        return trip.getTripsByRoute(self.identifier)

    def nearestStop(self, latitude, longitude):
        return stop.getNearestStop(latitude, longitude, route=self.identifier)

    def nearestVehicle(self, latitude, longitude):
        return vehicle.getNearestVehicle(latitude, longitude, route=self.identifier)

    def directions(self):
        vehicles = self.vehicles()
        d = None
        while d is None:
            for v in vehicles:
                try:
                    d = v.direction
                except:
                    pass

        if re.match('(east|west)bound', d, re.IGNORECASE):
            return ('EastBound', 'WestBound')
        elif re.match('(north|south)bound', d, re.IGNORECASE):
            return ('NorthBound', 'SouthBound')
        else:
            msg = "Could not find direction for vehicle %s on route %s" % (v.vehicleID, self.identifier)
            msg += "\nDirections received were:\n"
            msg += d
            raise Exception(msg)

    def guessHeading(self, latitude, longitude):
        # Determine directions for route (e.g. east/west)
        directions = self.directions()
        stops = self.stops()

        if directions == ('EastBound', 'WestBound'):
            # Find number of stops EAST of current location
            # Lower numbers for longitude (negative value in North America) mean eastward.
            stopsEastward = filter(lambda x: x.longitude < longitude, stops)
            if len(stopsEastward) > len(stops) / 2:
                return 'WestBound'
            else: 
                return 'EastBound'

        else:
            # Find number of stops NORTH of current location
            # Higher numbers for latitude (positive value in North America) mean northward.
            stopsNorthward = filter(lambda x: x.latitude > latitude, stops)
            if len(stopsNorthward) > len(stops) / 2:
                return 'SouthBound'
            else: 
                return 'NorthBound'

    def routeLine(self):
        coords = utils.getKML(self.routeLineURL)
        return coords

def guessRoute(lat, lng):
    routes = [Route(r) for r in utils.trolleyRoutes()]
    results = {}
    for r in routes:
        routeLine = r.routeLine()
        print "Route %s routeline has %s points." % (r.identifier, len(routeLine)/2 )
        shortestDistances = [utils.getDistance(lat, lng, x, y) for x, y in zip(*[iter(routeLine)]*2)]
        averageDistance = reduce(lambda x, y: float(x) + float(y), shortestDistances[:5]) / float(len(routes))
        results[r.identifier] = averageDistance

    # Invert hash of results, so max()[1] returns key, which is routeIdentifier
    inverse = [(value, key) for key, value in results.items()]
    probableRoute = max(inverse)[1]
    return probableRoute
