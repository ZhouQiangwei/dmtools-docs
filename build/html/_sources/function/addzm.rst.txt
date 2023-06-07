dmtools addzm
=============

.. contents:: 
    :local:

Description
^^^^^^^^^^

The zoom level determines the resolution of the retrieved data (DM file), with values ranging from 
1 (lowest resolution) to 9 (highest resolution). 
Higher resolutions result in smaller intervals for the DNA methylation level, and consequently, 
larger storage files. 

By default, the zoom level is set to 0 in the DM format. 
However, in some cases where the DM format needs to be viewed in the Genome Browser, 
a certain zoom level is required. And a recommended zoom level in such cases is between 2 and 6.


Usage
^^^^^

Add, remove or change zoom levels in DM file:

.. code:: bash

    $ dmtools addzm -i sample.mr.dm -o sample.mr.zm5.dm --zl 5 


Parameters
^^^^^^^^^^

``-i`` input DM file

``-o`` output dm file

``--zl`` The maximum number of zoom levels. [0-10], valid for dm out

``-r`` region for view, can be seperated by space. chr1:1-2900 chr2:1-200;

``--bed`` bed file for view, format: chrom start end (strand).

``--strand`` [0/1/2] strand for show, 0 represent '+' positive strand, 1 '-' negative strand, 2 '.' all information

``--context`` [0/1/2/3] context for show, 0 represent 'C/ALL' context, 1 'CG' context, 2 'CHG' context, 3 'CHH' context.

``--mincover`` >= minumum coverage show, default: 0

``--maxcover`` <= maximum coverage show, default: 10000

``-h|--help``

Please see 'dmtools addzm' for more details.


.. tip:: For feature requests or bug reports please open an issue `on github <http://github.com/ZhouQiangwei/dmtools>`__.
