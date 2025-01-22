from django.urls import path

from inventory.views import inventory_detail, inventory_list

urlpatterns = [
    path("", inventory_list),
    path("<int:id>/", inventory_detail),
]
