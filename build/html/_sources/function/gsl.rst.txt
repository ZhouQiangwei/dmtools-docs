GSL Library
===========

gsl library
-----------

The GSL library may need to be installed when the following problems occur during the installation process.

..

You can download here:

* fatal error: gsl/gsl_matrix_double.h : No such file or directory

:download:`gsl-2.4.tar.gz <https://www.dna-asmdb.com/tools/gsl-2.4.tar.gz>`

.. code:: bash

    ./configure --prefix=/disk1/glli/tools/gsl-2.4/
    make
    make install

Add environment variables to ~/.bashrc

.. code:: bash

    export C_INCLUDE_PATH=$C_INCLUDE_PATH:~/software/gsl-2.4/include
    export CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:~/software/gsl-2.4/include
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH::~/software/gsl-2.4/lib
    export LIBRARY_PATH=$LIBRARY_PATH::~/software/gsl-2.4/lib

And then:

.. code:: bash

    $ source ~/.bash

.. tip:: For feature requests or bug reports please open an issue `on github <http://github.com/ZhouQiangwei/BMtools>`__.
