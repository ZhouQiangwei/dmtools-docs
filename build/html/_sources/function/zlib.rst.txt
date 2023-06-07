Zlib library
============

zlib library
------------

The GSL library may need to be installed when the following problems occur during the installation process.

* unfound zlib.h

:download:`zlib-1.2.11.zip <https://www.dna-asmdb.com/tools/zlib-1.2.11.zip>`

.. code:: bash

    ./configure --prefix=/disk1/glli/tools/zlib-1.2.11/
    make
    make install

Add environment variables to ~/.bashrc

.. code:: bash

    export C_INCLUDE_PATH=$C_INCLUDE_PATH:/disk1/glli/tools/zlib-1.2.11/include
    export CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:/disk1/glli/tools/zlib-1.2.11/include
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH::/disk1/glli/tools/zlib-1.2.11/lib
    export LIBRARY_PATH=$LIBRARY_PATH::/disk1/glli/tools/zlib-1.2.11/lib

And then:

.. code:: bash

    $ source ~/.bash

.. tip:: For feature requests or bug reports please open an issue `on github <http://github.com/ZhouQiangwei/BatMeth2>`__.
