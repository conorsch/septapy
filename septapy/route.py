import requests


class Route(models.Model):
    """Represents a path that a Vehicle can take. Can list related objects 
    such as:

    .vehicles
    .stops

    It also provides helper methods for common operations, e.g.:

    .findNearestStop

    """

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

