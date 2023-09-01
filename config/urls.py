from django.contrib import admin
from django.urls import path
from app.views.views import create_contact, ContactList, delete_contact
from app.views.button import button, increment_button

urlpatterns = [
    path("admin/", admin.site.urls),
    path("create-contact/", create_contact, name="create-contact"),
    path("contacts/", ContactList.as_view(), name="contact-list"),
    path("delete-contact/<int:pk>/", delete_contact, name="delete-contact"),
    path("button/", button, name="button"),
    path("increment-button/", increment_button, name="increment-button"),
]
