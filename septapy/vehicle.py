class Vehicle(object):
    """Represents a single physical vehicle traveling along a Route."""

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
