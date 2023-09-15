from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


def transition_demo(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        "transition/transition_demo.html",
    )


def transition(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        "transition/transition.html",
    )
