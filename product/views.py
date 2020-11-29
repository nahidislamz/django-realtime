from django.shortcuts import render
from .models import Product
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import StreamingHttpResponse, HttpResponseRedirect
from django.urls import reverse
import time


def productView(request):
    product = Product.objects.all()
    return render(request, 'index.html', {'product': product})


def event_stream():

    initial_data = ""
    while True:
        data = json.dumps(list(Product.objects.order_by("-id").values("item", "desc", "price")),
                          cls=DjangoJSONEncoder
                          )

        if not initial_data == data:
            yield "\ndata: {}\n\n".format(data)
            initial_data = data
        time.sleep(1)


def getProduct(request):
    response = StreamingHttpResponse(event_stream())
    response['Content-Type'] = 'text/event-stream'
    return response
