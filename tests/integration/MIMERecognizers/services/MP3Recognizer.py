from servicelocator.lookup import service_provider
from tests.integration.MIMERecognizers.MIMERecognizerService import MIMERecognizerService


@service_provider(MIMERecognizerService)
class MP3Recognizer(MIMERecognizerService):
    def recognizes_extension(self, extension):
        return extension == ".mp3"

    def get_MIME_type(self):
        return "audio/x-mp3"
