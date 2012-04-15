import time
import json
                                                                                 
from django.core.cache import cache
from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import render

from django_pusher.push import pusher
from twilio.util import TwilioCapability

pusher.register('presence-world')

def home(request):
    capability = TwilioCapability(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    capability.allow_client_outgoing(settings.TWILIO_APP_ID)
    return render(request, 'index.html', {
        'token': capability.generate()
    })


@require_POST
@csrf_exempt
def pusher_auth(request):
    channel = request.POST["channel_name"]
    socket_id = request.POST["socket_id"]
    latlon = request.session.get('location')
    info = {'lat': latlon[0], 'lon': latlon[1]} if latlon else None
    r = pusher._real_getitem(channel).authenticate(socket_id, {
        'user_id': socket_id,
        'user_info': info,
    })
    return HttpResponse(json.dumps(r), mimetype="application/json")

@require_POST
@csrf_exempt
def pusher_location(request):
    lat = request.POST["lat"]
    lon = request.POST["lon"]
    request.session['location'] = (lat, lon)
    return HttpResponse()
