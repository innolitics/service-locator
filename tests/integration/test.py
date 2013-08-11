from servicelocator.lookup import global_lookup
from servicelocator.service_discoverer import discover_services
from tests.integration.FileOpeners.FileOpenerService import FileOpenerService
from tests.integration.MIMERecognizers.MIMERecognizerService import MIMERecognizerService
import unittest

discover_services()


class Test(unittest.TestCase):
    def test_MIME_lookup(self):
        MIMERecognizers = global_lookup.lookup_all(MIMERecognizerService)
        self.assertTrue(len(MIMERecognizers) == 4)

    def test_Opener_lookup(self):
        FileOpeners = global_lookup.lookup_all(FileOpenerService)
        self.assertTrue(len(FileOpeners) == 4)

