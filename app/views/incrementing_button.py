from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


def incrementing_button_demo(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        "incrementing_button/demo.html",
        {"value": 0, "next_value": 1},
    )


def incrementing_button(request: WSGIRequest) -> HttpResponse:
    value = int(request.GET.get("value"))

    return render(
        request,
        "incrementing_button/button.html",
        {"value": value, "next_value": value + 1},
    )
