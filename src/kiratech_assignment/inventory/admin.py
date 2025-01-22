from django.contrib import admin

from kiratech_assignment.inventory.models import Inventory, Supplier


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass
