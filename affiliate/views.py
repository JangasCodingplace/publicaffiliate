from django.shortcuts import render
from .models import Link
from django.http import Http404, HttpResponse


def index(request):
    return render(request, 'index/index.html')


def redirect_fallback_url(request, key):
    try:
        link = Link.objects.get(key=key)
    except Link.DoesNotExist:
        raise Http404("Page not Found.")

    response = HttpResponse("", status=302)
    response['Location'] = link.android_link
    return response


def redirect_ios_countdown(request, key):
    try:
        link = Link.objects.get(key=key)
    except Link.DoesNotExist:
        raise Http404("Page not Found.")

    data = {'link': link}
    return render(request, 'affiliates/iOS_Countdown.html', data)


def ios_urlgenius(request, key):
    try:
        link = Link.objects.get(key=key)
    except Link.DoesNotExist:
        raise Http404("Page not Found.")

    data = {'link': link}
    return render(request, 'affiliates/iOS_URLGenius_modified.html', data)
