import unittest
from sqlalchemy import create_engine
from models import Base, Product
from sqlalchemy.orm import sessionmaker


class TestProduct(unittest.TestCase):

    def setUp(self) -> None:
        self.engine = create_engine('sqlite:///:memory:', echo=True)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        self.test_product = Product(name='Shibamajd', price=2345)
        self.session.add(self.test_product)
        self.session.commit()

    def tearDown(self) -> None:
        Base.metadata.drop_all(self.engine)
        self.session.close()

    def test_adding_product_to_db(self):
        test_product = Product(name='Bahaa', price=2345)
        self.session.add(test_product)
        self.session.commit()

        product_from_table = self.session.query(Product).filter_by(name=test_product.name).first()
        self.assertIsNotNone(product_from_table)

    def test_updating_products(self):
        product = self.session.query(Product).first()
        new_price = 2000
        product.price = new_price
        self.session.commit()
        self.assertEqual(product.price, new_price)
