from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context_processors import csrf

from urlshort.core.models import Link

import random
import string
import json


def index(request):
    context = {}
    context.update(csrf(request))

    return render_to_response('index.html', context)


def redirect_original(request, slug_key):
    url = get_object_or_404(Link, pk=slug_key)
    url.count += 1
    url.save()

    return HttpResponseRedirect(url.my_url)


def shorten_url(request):
    url = request.POST.get("url", '')
    current_url = request.get_host()

    if not (url == ''):
        slug_key = get_short_code()
        b = Link(my_url=url, slug_key=slug_key)
        b.save()

        response_data = {}
        response_data['url'] = current_url + "/" + slug_key

        return HttpResponse(json.dumps(response_data),
                            content_type="application/json")

    return HttpResponse(json.dumps({"error": "error occurs"}),
                        content_type="application/json")


def get_short_code():
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase

    while True:
        slug_key = ''.join(random.choice(char) for x in range(length))
        try:
            temp = Link.objects.get(pk=slug_key)
        except:
            return slug_key
