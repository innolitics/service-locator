from ServiceLocator import LocateAll
from MIMERecognizers import *
from MIMERecognizers.MIMERecognizerService import MIMERecognizerService
from FileOpeners import *
from FileOpeners.FileOpenerService import FileOpenerService

file = "main.htm"
extension = ".htm"

MIMERecognizers = LocateAll(MIMERecognizerService)
mimes = [service.get_MIME_type() for service in MIMERecognizers
         if service.recognizes_extension(extension)]

FileOpeners = LocateAll(FileOpenerService)
for service in FileOpeners:
    [service.open(file) for mime in mimes
     if service.can_open_mime_type(mime)]


