from django.contrib.auth.models import User
from django.db.models import Q
from django.test import TestCase

# Create your tests here.


class TestUser(TestCase):
    def setUp(self) -> None:
        self.user: User = User(
            **{
                "username": "RomanPierce",
                "password": "FastFilm@13",
                "first_name": "Roman",
                "last_name": "Pierce",
                "email": "romanpierce123@filmproductions.edu",
            }
        )
        self.user.save()
        return super(TestUser, self).setUp()

    def testUserContact(self):
        assert (
            self.user.email
            == User.objects.get(
                email="romanpierce123@filmproductions.edu"
            ).email
        )

    def testString(self):
        assert "MJ".lower() == "mj"

    def testInteger(self):
        assert 2 + 6 == 8

    def testFloat(self):
        assert 0.6 + 0.7 != 1.3

    def testType(self):
        assert type(self.user) == User
        assert isinstance(self.user, User)

    def tearDown(self) -> None:
        self.user.delete()
        return super().tearDown()
