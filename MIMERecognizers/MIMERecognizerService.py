

class MIMERecognizerService(object):
    """
    This class only contains the software contract that must be fulfilled by all decoders.
    """
    def recognizes_extension(self, extension):
        pass

    def get_MIME_type(self):
        pass
