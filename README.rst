===============================
 Python Service Locator v 0.1.3
===============================

- The service locator pattern is a very simple but useful pattern that helps you remove glue code from application code.
- Decoupling the wiring of dependencies (glue code) can reduce your lines of code significantly and encourages loose coupling.
- This allows you to depend on abstractions rather than on concretions, it makes adding additional
  functionality to your application much easier.
- Configuration xml files are not pythonic and are often overcomplicated, class decorators are used instead.
- Concrete service implementations should be placed in a services folder. All services subfolders will be discovered using
  discover_services function and all containing modules will be auto-loaded.
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

    @service_provider(MIMERecognizerService)
    class PDFRecognizer(MIMERecognizerService):
        def recognizes_extension(self, extension):
            return extension == ".pdf"

        def get_MIME_type(self):
            return "application/pdf"


You can register as many services and service providers as you like. To retrieve service providers for a service, use the
locate function like this:

.. code-block:: python
    from servicelocator.lookup import global_lookup

    MIMERecognizers = global_lookup.lookup_all(MIMERecognizerService)

This will get all concrete implementations of the MIMERecognizerService but the dependent module need not know about the
existence of any of these concrete implementations. This makes adding new service providers very easy.

And if you know there is only one implementation of the service:

.. code-block:: python

    from servicelocator.lookup import global_lookup

    MIMERecognizer = global_lookup.lookup(MIMERecognizerService)


