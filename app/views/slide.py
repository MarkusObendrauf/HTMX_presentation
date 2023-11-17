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
    "static_slides/00_start.html",
    "static_slides/02_what.html",
    "static_slides/10_back_in_time.html",
    "static_slides/20_interactivity.html",
    "static_slides/30_react.html",
    "static_slides/40_elephant.html",
    "static_slides/50_react_2.html",
    "static_slides/100_back_in_time.html",
    "static_slides/105_html_a.html",
    "static_slides/110_motivation.html",
    "static_slides/120_why_not.html",
    "static_slides/130_get_swap.html",
    "incrementing_button/demo.html",
    "static_slides/132_howl.html",
    "static_slides/133_howl_img.html",
    "static_slides/140_trigger.html",
    "lazy_load/lazy_load_demo.html",
    "infinite_scroll/demo.html",
    "static_slides/150_more_examples.html",
    "static_slides/160_put_delete.html",
    "static_slides/161_more.html",
    "edit/demo.html",
    "static_slides/162_revelation.html",
    "static_slides/170_comparison.html",
    "static_slides/200_rest.html",
    "static_slides/210_actually.html",
    "static_slides/220_hateoas.html",
    "static_slides/230_hateoas_2.html",
    "static_slides/310_migration.html",
    "static_slides/315_contexte_1.html",
    "static_slides/320_contexte_DX.html",
    "static_slides/330_contexte_UX.html",
    "static_slides/400_conclusion.html",
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
