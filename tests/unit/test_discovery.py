import unittest
import os
from servicelocator.lookup import global_lookup
from servicelocator.service_discoverer import discover_services
from tests.unit.services.test_service import AbstractService


class TestDiscovery(unittest.TestCase):
    def test_discovery(self):
        discover_services()
        service = global_lookup.lookup(AbstractService)
        self.assertTrue(service.i_am_a_service(), "service discovery failed")

