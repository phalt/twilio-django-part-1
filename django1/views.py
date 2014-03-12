# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from django_twilio.decorators import twilio_view
from twilio.twiml import Response

@twilio_view
def sms(request):
    r = Response()
    r.message('Hello world! Get in touch - paul@twilio.com')
    return r


@twilio_view
def ring(request):
    r = Response()
    r.play('http://bit.ly/phaltsw')
    return r
    
# This is a plain view that returns manually written TwiML
# Note: it's not linked to a URL in this example.
@csrf_exempt
def sms_plain(request):
    twiml = '<Response><Message>Plain old TwiML</Message></Response>'
    return HttpResponse(twiml, content_type='text/xml')

