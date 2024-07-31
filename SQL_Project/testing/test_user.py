import unittest
from sqlalchemy import create_engine
from models import Base, Users
from sqlalchemy.orm import sessionmaker


class TestUser(unittest.TestCase):

    def setUp(self) -> None:
        self.engine = create_engine('sqlite:///:memory:', echo=True)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        self.test_user = Users(name='TestUser', email='test@gmail.com')
        self.session.add(self.test_user)
        self.session.commit()

    def test_user_in_table(self):
        user_from_table = self.session.query(Users).filter_by(name=self.test_user.name).first()
        self.assertIsNotNone(user_from_table)
        self.assertEqual(user_from_table.email, self.test_user.email)
