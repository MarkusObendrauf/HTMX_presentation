from typing import Iterable
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

from app import models


def edit_demo(request: WSGIRequest) -> HttpResponse:
    contacts = _get_contacts(page=0)
    return render(
        request,
        "infinite_scroll/infinite_scroll_demo.html",
        {"contacts": contacts, "next_page": 1},
    )


def contacts(request: WSGIRequest) -> HttpResponse:
    page = int(request.GET.get("page"))
    contacts = _get_contacts(page=page)
    return render(
        request,
        "infinite_scroll/infinite_scroll_rows.html",
        {"contacts": contacts, "next_page": page + 1},
    )


def _get_contacts(page: int) -> Iterable[models.Contact2]:
    contacts_per_page = 30
    page_start = page * contacts_per_page
    page_end = page_start + contacts_per_page
    return models.Contact2.objects.all()[page_start:page_end]
