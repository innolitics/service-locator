from servicelocator.lookup import service_provider
from tests.integration.MIMERecognizers.MIMERecognizerService import MIMERecognizerService


@service_provider(MIMERecognizerService)
class HTMLRecognizer(MIMERecognizerService):
    def recognizes_extension(self, extension):
        return extension == ".html" or extension == ".htm"

    def get_MIME_type(self):
        return "text/html"
