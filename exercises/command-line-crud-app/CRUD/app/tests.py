from django.test import TestCase
from app import models


class TestShopping(TestCase):
    def test_create_item(self):
        shopping = models.create_item(
            "Kayle",
            "1"
        )

        self.assertEqual(shopping.id, 1)
        self.assertEqual(shopping.item, "Kayle")
        self.assertEqual(shopping.quantity, "1")

    def test_view_all(self):
        items_data = [
            {
                "item": "Pizza",
                "quantity": "5",
            },
            {
                "item": "Toilet Paper",
                "quantity": "2",
            },
            {
               "item": "Car",
                "quantity": "1",
            },
        ]

        for item_data in items_data:
            models.create_item(
                item_data["item"],
                item_data["quantity"],
            )

        items = models.view_all()

        self.assertEqual(len(items), len(items_data))

        items_data = sorted(items_data, key=lambda c: c["item"])
        items = sorted(items, key=lambda c: c.item)

        for data, shopping in zip(items_data, items):
            self.assertEqual(data["item"], shopping.item)
            self.assertEqual(data["quantity"], shopping.quantity)
           

    def test_search_item_name(self):
        items_data = [
            {
                "item": "Kayle",
                "quantity": "1"
            },
            {
               "item": "McAlister's Mac & Cheese",
               "quantity": "2"
            },
            {
                "item": "Monster",
                "quantity": "20"
            },
        ]

        for item_data in items_data:
            models.create_item(
                item_data["item"],
                item_data["quantity"]
            )

        self.assertIsNone(models.search_item_name("Blair"))

        shopping = models.search_item_name("Kayle")

        self.assertIsNotNone(shopping)
        self.assertEqual(shopping.quantity, "1")

    def test_search_quantity(self):
        items_data = [
            {
                "item": "Fruit",
                "quantity": "40"
            },
            {
               "item": "Water",
               "quantity": "5"
            },
            {
                "item": "Pencil",
                "quantity": "5"
            },
        ]

        for item_data in items_data:
            models.create_item(
                item_data["item"],
                item_data["quantity"]
            )

        self.assertEqual(len(models.search_quantity(5)), 2)

    def test_update_item(self):
        items_data = [
            {
                "item": "Fruit",
                "quantity": "40"
            },
            {
               "item": "Water",
               "quantity": "5"
            },
            {
                "item": "Pencil",
                "quantity": "5"
            },
        ]

        for item_data in items_data:
            models.create_item(
                item_data["item"],
                item_data["quantity"]
            )

        models.update_item("Fruit", "5")

        self.assertEqual(
            models.search_item_name("Fruit").quantity, "5"
        )

    def test_delete_item(self):
        items_data = [
            {
                "item": "Fruit",
                "quantity": "40"
            },
            {
               "item": "Water",
               "quantity": "5"
            },
            {
                "item": "Pencil",
                "quantity": "5"
            },
        ]

        for item_data in items_data:
            models.create_item(
                item_data["item"],
                item_data["quantity"]
            )

        models.delete_item("Water")

        self.assertEqual(len(models.view_all()), 2)

