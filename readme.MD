
# Twilio & Django part 1

This is a simple Django application demonstrating how to integrate [django-twilio][1]
into your Django projects.

## How to use

1. Download this repository

2. Install the requirements with pip:

```
    $ pip install -r requirements.txt
```

This will install:

* Django
* django-twilio

3. Open the urls.py to see how the URL configuration has been done


4. Open the views.py to see how the views are set up.

5. Get the server running with:

```
    $ python manage.py runserver
```

You can use cURL to test the server, this will output the [TWiML][2] response:

```
    curl -X POST 127.0.0.1:8000/sms/
```

```
    <?xml version="1.0" encoding="UTF-8"?>
        <Response>
            <Message>
                <Body>Hello world! Get in touch - paul@twilio.com</Body>
            </Message>
        </Response>
```




[1]: https://github.com/rdegges/django-twilio
[2]: https://www.twilio.com/docs/api/twiml
