from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

from time import sleep


def lazy_load_demo(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        "lazy_load/lazy_load_demo.html",
    )


def lazy_load_graph(request: WSGIRequest) -> HttpResponse:
    sleep(3)
    return render(
        request,
        "lazy_load/graph.html",
    )
