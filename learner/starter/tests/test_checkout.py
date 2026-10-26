import unittest

from src.checkout import calculate_total


class CheckoutTests(unittest.TestCase):
    def test_single_line_item(self):
        self.assertEqual(calculate_total([{"name": "Notebook", "price": 4.5, "quantity": 2}]), 9.0)

    def test_multiple_items(self):
        items = [
            {"name": "Notebook", "price": 4.5, "quantity": 2},
            {"name": "Pen", "price": 1.25, "quantity": 4},
        ]
        self.assertEqual(calculate_total(items), 14.0)

    def test_empty_cart(self):
        self.assertEqual(calculate_total([]), 0.0)

    def test_return_type_is_float(self):
        self.assertIsInstance(calculate_total([]), float)


if __name__ == "__main__":
    unittest.main()
