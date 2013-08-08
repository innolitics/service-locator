===============================
 Python Service Locator v 0.0.2
===============================

- The service locator pattern is a very simple but useful pattern that can help you manage dependencies.
- Helps decouple the wiring of dependencies (glue code) from the actual application logic itself.
- Rather than instantiating a library service yourself, you ask the ecosystem to locate them for you.
- This allows you to depend on abstractions rather than on concretions, it makes adding additional
  functionality to your application much easier.
- Configuration xml files are not pythonic and are often overcomplicated, class decorators are used instead.
- All services will be instantiated by the service locator as a singleton.


Usage
-----

Please see main.py for a sample project. Suppose you have an abstract service class that looks like this:

.. code-block:: python

    class MIMERecognizerService(object):
        def recognizes_extension(self, extension):
            pass

        def get_MIME_type(self):
            pass

Register a service like this:

.. code-block:: python

    @ServiceProvider(MIMERecognizerService)
    class PDFRecognizer(MIMERecognizerService):
        def recognizes_extension(self, extension):
            return extension == ".pdf"

        def get_MIME_type(self):
            return "application/pdf"


You can register as many services and service providers as you like. To retrieve service providers for a service, use the
locate function like this:

.. code-block:: python

    MIMERecognizers = LocateAll(MIMERecognizerService)

This will get all concrete implementations of the MIMERecognizerService but the dependent module need not know about the
existence of any of these concrete implementations. This makes adding new service providers very easy.


TODO
====

- Think about thread safety. Singletons are currently instantiated in a thread unsafe way.
- Think about a non-global singleton registry. There may be some use having local service provider registries instead of
  one global one?
