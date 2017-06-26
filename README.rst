wubi
======


Translate chinese chars to pinyin based on Mandarin.dat

Install
-------

.. code:: bash

    $ pip install wubi

Usage
-----

.. code:: python

    >>> import wubi
    >>> print wubi.get('王文超，爱自由。','cw')
    gggg yygy fhv , ep thd mh .

    >>> print wubi.get('你好', format="strip", delimiter=" ")
    王文超，爱自由。


License
-------

`wubi` is free software, under an MIT-style license. See LICENSE for details.

The data file for translations is the CC-BY-SA 3.0.

The translations are from the CC-CE-DICT project (https://cc-cedict.org/wiki/), by Denisowski, Peterson, Brelsford, and others.
