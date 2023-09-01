from django.contrib import admin
from django.urls import path
from app.views.lazy_load import lazy_load_demo, lazy_load_graph
from app.views.views import create_contact, ContactList, delete_contact
from app.views.incrementing_button import incrementing_button, incrementing_button_demo

urlpatterns = [
    path("admin/", admin.site.urls),
    path("create-contact/", create_contact, name="create-contact"),
    path("contacts/", ContactList.as_view(), name="contact-list"),
    path("delete-contact/<int:pk>/", delete_contact, name="delete-contact"),
    path("incrementing-button-demo/", incrementing_button_demo, name="button"),
    path("incrementing-button/", incrementing_button, name="incrementing-button"),
    path("lazy-load-demo/", lazy_load_demo, name="lazy-load-demo"),
    path("lazy-load-graph/", lazy_load_graph, name="lazy-load-graph"),
]
