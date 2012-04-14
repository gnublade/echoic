
from twilio.twiml import Response
from django_twilio.decorators import twilio_view

@twilio_view
def echo(request):
    response = Response()
    if request.method == 'POST':
        response.play(request.POST['RecordingUrl'])
    else:
        response.say("Echo test", voice='woman')
        response.record()
    return response
