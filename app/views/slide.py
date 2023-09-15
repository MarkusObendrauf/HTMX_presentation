from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from enum import Enum


class TransitionClass(Enum):
    NEXT = "next-slide"
    PREVIOUS = "previous-slide"


slides = ["slide.html"]


def next_slide(request: WSGIRequest, slide_number: int = 0) -> HttpResponse:
    return render_slide(request, slide_number + 1, TransitionClass.NEXT)


def previous_slide(request: WSGIRequest, slide_number: int = 0) -> HttpResponse:
    return render_slide(request, slide_number - 1, TransitionClass.PREVIOUS)


def slide(request: WSGIRequest, slide_number: int = 0) -> HttpResponse:
    return render_slide(request, slide_number)


def render_slide(
    request: WSGIRequest,
    slide_number: int,
    transition_class: TransitionClass = TransitionClass.NEXT,
) -> HttpResponse:
    return render(
        request,
        "slide.html",
        {
            "transition_class": transition_class.value,
            "page": "incrementing_button/button.html",
        },
    )
