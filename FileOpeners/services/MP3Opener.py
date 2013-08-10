from ..FileOpenerService import FileOpenerService
from ServiceLocator import ServiceProvider


@ServiceProvider(FileOpenerService)
class MP3Opener(FileOpenerService):

    def can_open_mime_type(self, mime):
        return mime == "audio/mp3"

    def open(self, file):
        print("opening with music player")
