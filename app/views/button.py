from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


def button(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        "incrementing_button_demo.html",
        {"value": 0, "next_value": 1},
    )


def increment_button(request: WSGIRequest) -> HttpResponse:
    value = int(request.GET.get("value"))

    return render(
        request,
        "incrementing_button.html",
        {"value": value, "next_value": value + 1},
    )
