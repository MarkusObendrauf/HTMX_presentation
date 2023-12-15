from time import sleep
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from random import choices


def click_to_load_demo(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        "click_to_load/demo.html",
    )


def click_to_load_list(request: WSGIRequest) -> HttpResponse:
    sleep(3)
    list_items = choices(sentences, k=4)

    return render(
        request,
        "click_to_load/list.html",
        {"list_items": list_items}
    )


sentences = [
    "Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
    "Aliquam tincidunt mauris eu risus.",
    "Vestibulum auctor dapibus neque.",
    "Nunc dignissim risus id metus.",
    "Cras ornare tristique elit.",
    "Vivamus vestibulum ntulla nec ante.",
    "Praesent placerat risus quis eros.",
    "Fusce pellentesque suscipit nibh.",
    "Integer vitae libero ac risus egestas placerat.",
    "Vestibulum commodo felis quis tortor.",
    "Ut aliquam sollicitudin leo.",
    "Cras iaculis ultricies nulla.",
    "Donec quis dui at dolor tempor interdum.",
]
