from django.conf import settings
from django.shortcuts import render

from twilio.util import TwilioCapability

def home(request):
    capability = TwilioCapability(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    capability.allow_client_outgoing(settings.TWILIO_APP_ID)
    return render(request, 'index.html', {
        'token': capability.generate()
    })
