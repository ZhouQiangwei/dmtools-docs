dmtools bw
============

.. contents:: 
    :local:

Description
^^^^^^^^^^

The DM format is a binary file format that is suitable for use with computer programs, 
and DMtools is a powerful operating tool that can perform a range of analysis tasks on this format. 
Considering the popularity of the BigWig format for visualization purposes, we have implemented the functionality to convert dm format to bw format.

To convert the DM format to text format, we can use the "dmtools bw" command. 
We need to specify the input file as a DM file using the "-i" option. 
We can then choose to output the results to a specified file or directly to the front-end, 
Moreover, we can also select the output information content, 
such as whether to include positive and negative chains.

You can view and process dm file with dmtools:

Usage
^^^^^

.. code:: bash

    $ dmtools bw -i mutant.methratio.dm -o mutant.cg.bw --context 1


Parameters
^^^^^^^^^^

``-i`` input DM file

``-o`` output file

``-r`` region for view, can be seperated by space. chr1:1-2900 chr2:1-200

``--chr`` chromosome for view

``--bed`` bed file for view, format: chrom start end (strand).

``--strand`` [0/1/2] strand for show, 0 represent '+' positive strand, 1 '-' negative strand, 2 '.' all information

``--context`` [0/1/2/3] context for show, 0 represent 'C/ALL' context, 1 'CG' context, 2 'CHG' context, 3 'CHH' context.

``--mincover`` >= minumum coverage show, default: 0

``--maxcover`` <= maximum coverage show, default: 10000

``--zl`` The maximum number of zoom levels. [0-10]

``-h|--help``

.. tip:: For feature requests or bug reports please open an issue `on github <http://github.com/ZhouQiangwei/dmtools>`__.
