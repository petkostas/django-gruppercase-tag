=====
django-gruppercase-tag
=====

django-gruppercase-tag_ is a django template tag to properly convert
Greek words to uppercase.
Most languages fail to properly uppercase Greek lowercase words as they contain
accents, Greek uppercase words do not contain accents.

Quick start
-----------

1. Create a ``templatetags`` folder inside your application folder that you want to use the tag
2. Copy ``grupppercase.py`` to your ``templatetags`` folder
3. Inside your template: ``{% load gruppercase %}``
4. Uppercase your words (within your template) ``{{ somevar|gruppercase }}``

You can use it with no problems with any other language strings, as it will replace only
Greek characters in your string.


Authors
=======

* Author: `Kostas Petrakis`_

.. _Kostas Petrakis: https://github.com/petkostas
.. _django-gruppercase-tag: https://github/com/petkostas/django-gruppercase-tag
