import unittest
from servicelocator.lookup import Lookup


class Service(object):
    pass


class TestLookup(unittest.TestCase):
    def test_addition(self):
        lookup = Lookup()
        service = Service()
        lookup.add(Service, service)
        self.assertTrue(lookup.lookup(Service), "Lookup addition failed")

