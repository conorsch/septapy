# Create your views here.
from django.http import HttpResponse
from septajawn.septapy.models import Route
import json
import requests


def showRoute(request, route=None):

    r = Route(route)

    message = """
    %s 
    Vehicles are:
    """ % r

    for v in r.vehicles():
        message += unicode(v)
        message += '\n' 

    return HttpResponse(message)

def getNearestStop(request, route=None, lat=None, lng=None):

    r = Route(route)

    # form data comes in as unicode via GET, so convert to float
    lat = float(request.GET.get('lat'))
    lng = float(request.GET.get('lng'))
    #print "LAT LONG ARE: %s %s" % (lat, lng)

    n = r.findNearestStop(lat, lng)
    d = dict(title=n.title, lat=n.latitude, lng=n.longitude)
    j = json.dumps(d)

    return HttpResponse(j, mimetype='application/json')

def getNearestTrolley(request, route=None, lat=None, lng=None):

    r = Route(route)

    # form data comes in as unicode via GET, so convert to float
    lat = float(request.GET.get('lat'))
    lng = float(request.GET.get('lng'))

    n = r.findNearestVehicle(lat, lng)

    # poor man's object serialization right here. 
    d = dict(direction=n.direction, title=n.title, lat=n.latitude, lng=n.longitude)
    j = json.dumps(d)

    return HttpResponse(j, mimetype='application/json')
