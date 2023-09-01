from typing import Iterable
from django.core.handlers.wsgi import WSGIRequest, QueryDict
from django.http import HttpResponse
from django.shortcuts import render

from app import models


def edit_demo(request: WSGIRequest) -> HttpResponse:
    contacts = _get_contacts(page=0)
    return render(
        request,
        "edit/demo.html",
        {"contacts": contacts, "next_page": 1},
    )


def edit_contact(request: WSGIRequest, contact_id: int) -> HttpResponse:
    contact = models.Contact2.objects.get(id=contact_id)
    return render(
        request,
        "edit/edit_row.html",
        {"contact": contact},
    )


def contact(request: WSGIRequest, contact_id: int) -> HttpResponse:
    contact = models.Contact2.objects.get(id=contact_id)
    if request.method == "DELETE":
        contact.delete()
        return contacts(request)
    elif request.method == "PUT":
        put = QueryDict(request.body)
        contact.first_name = put.get("first_name")
        contact.last_name = put.get("last_name")
        contact.email = put.get("email")
        contact.save()
    return render(
        request,
        "edit/row.html",
        {"contact": contact},
    )


def contacts(request: WSGIRequest) -> HttpResponse:
    page = int(request.GET.get("page") or 0)
    contacts = _get_contacts(page=page)
    return render(
        request,
        "edit/row_page.html",
        {"contacts": contacts, "next_page": page + 1},
    )


def _get_contacts(page: int) -> Iterable[models.Contact2]:
    contacts_per_page = 30
    page_start = page * contacts_per_page
    page_end = page_start + contacts_per_page
    return models.Contact2.objects.all()[page_start:page_end]
