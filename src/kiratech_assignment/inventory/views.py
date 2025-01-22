import django_filters
from django.db import models
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import generics

from kiratech_assignment.inventory.models import Inventory
from kiratech_assignment.inventory.serializers import InventorySerializer


class InventoryFilter(filters.FilterSet):
    class Meta:
        model = Inventory
        fields = ["name", "description", "note"]
        filter_overrides = {
            models.CharField: {
                "filter_class": django_filters.CharFilter,
                "extra": lambda f: {"lookup_expr": "icontains"},
            },
            models.TextField: {
                "filter_class": django_filters.CharFilter,
                "extra": lambda f: {"lookup_expr": "icontains"},
            },
        }


class InventoryList(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = InventoryFilter


def inventory_list(request: HttpRequest) -> HttpResponse:
    serializer = InventorySerializer(Inventory.objects.all(), many=True)

    return render(request, "list.html", {"data": serializer.data})


def inventory_detail(request: HttpRequest, id: int) -> HttpResponse:
    try:
        record = Inventory.objects.get(pk=id)

    except Inventory.DoesNotExist:
        raise Http404("<h1>Page not found</h1>")

    return render(request, "detail.html", {"record": record})
