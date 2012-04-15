
from twilio.twiml import Response

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django_twilio.decorators import twilio_view

from ldnrealtime.accounts.models import UserProfile
from .models import Recording

@twilio_view
def echo(request):
    response = Response()
    if request.method == 'POST':
        response.play(request.POST['RecordingUrl'])
    else:
        response.say("Echo test", voice='woman')
        response.record()
    return response

@twilio_view
def record(request):
    response = Response()
    if request.method == 'POST':
        from_number = request.POST['From']
        try:
            user = User.objects.get(userprofile__phone_number=from_number)
        except User.DoesNotExist:
            user = User.objects.create(username=from_number)
            UserProfile.objects.create(user=user, phone_number=from_number)
        record = Recording.objects.create(
            url=request.POST['RecordingUrl'],
            duration=request.POST['RecordingDuration'],
            recorded_by=user,
        )
        response.say("Thankyou and goodbye", voice='female')
    else:
        response.record()
    return response

@twilio_view
def conference(request):
    response = Response()
    response.dial().conference(                                                         
        name=request.REQUEST['room'],
        startConferenceOnEnter=True,
        endConferenceOnExit=True
    ) 
    return response
