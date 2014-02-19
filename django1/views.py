# -*- coding: utf-8 -*-
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
    r.play('http://movie.10yan.com/2009cjzt/mp3/xw3.mp3')
    return r
