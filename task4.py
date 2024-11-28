# tests/test_models.py
import unittest
from models import Product  # Assuming your Product model is in the models.py file
from faker import Faker

fake = Faker()

class TestProductModel(unittest.TestCase):
    
    def test_delete_product(self):
        # Create a fake product (simulating a database or an in-memory object)
        product = Product(name=fake.company(),
                          description=fake.text(max_nb_chars=200),
                          price=99.99,
                          sku=fake.uuid4(),
                          category=fake.word())
        
        # Simulate saving the product to a "database"
        product.save()  # Assuming the 'save' method persists the product
        
        # Ensure product exists in the "database"
        saved_product = Product.read(product.sku)  # Assuming 'read' method fetches by SKU
        self.assertIsNotNone(saved_product)

        # Simulate the "delete" operation
        product.delete()  # Assuming 'delete' method removes the product
        
        # Try to retrieve the deleted product
        deleted_product = Product.read(product.sku)
        
        # Ensure that the product is deleted (should return None or equivalent)
        self.assertIsNone(deleted_product)

if __name__ == '__main__':
    unittest.main()
