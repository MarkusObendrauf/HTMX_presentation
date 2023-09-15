from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from enum import Enum


class TransitionClass(Enum):
    NEXT = "next-slide"
    PREVIOUS = "previous-slide"


def slide_base(request: WSGIRequest, slide_number: int = 0) -> HttpResponse:
    return render(
        request,
        "slide_base.html",
        {
            "transition_class": TransitionClass.NEXT.value,
            "slide_number": slide_number,
        },
    )


slides = [
    "slide_1.html",
    "incrementing_button/demo.html",
    "lazy_load/lazy_load_demo.html",
    "infinite_scroll/demo.html",
    "edit/demo.html",
]


def slide(request: WSGIRequest, slide_number: int = 0) -> HttpResponse:
    previous = request.GET.get("previous") == "true"
    transition_class = TransitionClass.PREVIOUS if previous else TransitionClass.NEXT
    slide = slides[slide_number]
    return render(
        request,
        slide,
        {
            "transition_class": transition_class.value,
            "slide_number": slide_number,
        },
    )
