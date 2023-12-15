from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


def tabs_demo(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        "tabs/demo.html",
        {"tab": 1}
    )


def tab(request: WSGIRequest) -> HttpResponse:
    tab_id = request.GET.get("tab") or "1"
    return render(
        request,
        "tabs/tab.html",
        {"tab": tab_id}
    )
