from django.contrib import admin
from django.urls import path
from app.views.edit import contact, edit_demo, edit_contact, contacts as contacts_edit
from app.views.infinite_scroll import infinite_scroll_demo, contacts
from app.views.lazy_load import lazy_load_demo, lazy_load_graph
from app.views.incrementing_button import incrementing_button, incrementing_button_demo
from app.views.slide import slide

urlpatterns = [
    path("admin/", admin.site.urls),
    path("incrementing-button-demo/", incrementing_button_demo, name="button"),
    path("incrementing-button/", incrementing_button, name="incrementing-button"),
    path("lazy-load-demo/", lazy_load_demo, name="lazy-load-demo"),
    path("lazy-load-graph/", lazy_load_graph, name="lazy-load-graph"),
    path("infinite-scroll-demo/", infinite_scroll_demo, name="infinite-scroll-demo"),
    path("infinite-scroll-demo/contacts/", contacts, name="contacts"),
    path("edit-demo/", edit_demo, name="edit-demo"),
    path("edit-demo/contacts/", contacts_edit, name="edit-demo"),
    path("contact/<int:contact_id>/", contact, name="contact"),
    path("contact/<int:contact_id>/edit/", edit_contact, name="contact"),
    path("slide/", slide, name="slide"),
]
