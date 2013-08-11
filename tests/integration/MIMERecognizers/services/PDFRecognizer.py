from servicelocator.lookup import service_provider
from tests.integration.MIMERecognizers.MIMERecognizerService import MIMERecognizerService


@service_provider(MIMERecognizerService)
class PDFRecognizer(MIMERecognizerService):
    def recognizes_extension(self, extension):
        return extension == ".pdf"

    def get_MIME_type(self):
        return "application/pdf"
