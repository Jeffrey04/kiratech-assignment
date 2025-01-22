from django.test import Client, TestCase

from inventory.models import Inventory, Supplier


# Create your tests here.
class InventoryTestCase(TestCase):
    def test_inventory_list(self) -> None:
        client = Client()

        response = client.get("/inventory/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Inventory List" in response.content.decode("utf-8"))

    def test_inventory_detail(self) -> None:
        client = Client()

        inventory = Inventory.objects.create(
            name="Foo",
            description="Some description",
            note="Some note",
            stock=100,
            availability=True,
            supplier=Supplier.objects.create(name="Some supplier"),
        )

        response = client.get(f"/inventory/{inventory.pk + 1}/")
        self.assertEqual(response.status_code, 404)

        response = client.get(f"/inventory/{inventory.pk}/")
        content = response.content.decode("utf-8")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(inventory.name in content)
        self.assertTrue(inventory.description in content)
        self.assertTrue(inventory.note in content)
        self.assertTrue(str(inventory.stock) in content)
        self.assertTrue(inventory.supplier.name in content)

    def test_inventory_api(self) -> None:
        client = Client()

        inventory1 = Inventory.objects.create(
            name="Foo",
            description="Some description",
            note="Some note",
            stock=100,
            availability=True,
            supplier=Supplier.objects.create(name="Some supplier"),
        )

        inventory2 = Inventory.objects.create(
            name="Bar",
            description="New description",
            note="New note",
            stock=100,
            availability=True,
            supplier=Supplier.objects.create(name="New supplier"),
        )

        response = client.get("/api/inventory/")

        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) == 2)

        response = client.get(f"/api/inventory/?name={inventory1.name.lower()}")
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(result) == 1)

        # check only necessary fields are in
        self.assertTrue("description" not in result[0])
        self.assertTrue("note" not in result[0])
        self.assertTrue("stock" not in result[0])

        # check relevant record is returned properly
        self.assertEqual(result[0]["id"], inventory1.pk)
        self.assertEqual(result[0]["name"], inventory1.name)
        self.assertEqual(result[0]["availability"], inventory1.availability)
        self.assertEqual(result[0]["supplier"], inventory1.supplier.name)

        response = client.get("/api/inventory/?description=new")
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(result) == 1)

        self.assertEqual(result[0]["id"], inventory2.pk)
        self.assertEqual(result[0]["name"], inventory2.name)
        self.assertEqual(result[0]["availability"], inventory2.availability)
        self.assertEqual(result[0]["supplier"], inventory2.supplier.name)

        response = client.get("/api/inventory/?note=some")
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(result) == 1)

        self.assertEqual(result[0]["id"], inventory1.pk)
        self.assertEqual(result[0]["name"], inventory1.name)
        self.assertEqual(result[0]["availability"], inventory1.availability)
        self.assertEqual(result[0]["supplier"], inventory1.supplier.name)
