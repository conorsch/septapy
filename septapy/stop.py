class Stop(object):
    """Represents a single location where public transit vehicles 
    pick up and drop off passengers. Has associated attributes such as:
    .latitude
    .longitude
    .coords        # latitude and longitude as tuple
    .route
    """
    
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


