from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


def slide(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        "slide.html",
    )
