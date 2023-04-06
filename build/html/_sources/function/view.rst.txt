dmtools view
============

.. contents:: 
    :local:

Description
^^^^^^^^^^

The DM format is a binary file format that is suitable for use with computer programs, 
and DMtools is a powerful operating tool that can perform a range of analysis tasks on this format. 
However, since the DM format is difficult for humans to read, we may need to convert it 
into a more user-friendly text format.

To convert the DM format to text format, we can use the "dmtools view" command. 
We need to specify the input file as a DM file using the "-i" option. 
We can then choose to output the results to a specified file or directly to the front-end, 
using the UNIX STDOUT convention and the redirection operator (">"). 
Moreover, we can also select the output information content, 
such as whether to include positive and negative chains.

You can view and process dm file with dmtools:

Usage
^^^^^

.. code:: bash

    $ dmtools view -i mutant.methratio.dm | head
      #Chr1	34	35	0.600000	5	-	CHG
      #Chr1	80	81	0.333333	6	-	CHH
      #Chr1	116	117	1.000000	4	-	CG
      #Chr1	117	118	0.250000	4	-	CHG
    
obtained text format methylation results

Parameters
^^^^^^^^^^

``-i`` input DM file

``-o`` output file [stdout]

``-r`` region for view, can be seperated by space. chr1:1-2900 chr2:1-200

``--chr`` chromosome for view

``--bed`` bed file for view, format: chrom start end (strand).

``--strand`` [0/1/2] strand for show, 0 represent '+' positive strand, 1 '-' negative strand, 2 '.' all information

``--context`` [0/1/2/3] context for show, 0 represent 'C/ALL' context, 1 'CG' context, 2 'CHG' context, 3 'CHH' context.

``--mincover`` >= minumum coverage show, default: 0

``--maxcover`` <= maximum coverage show, default: 10000

``--outformat`` txt or dm format [txt]

``--zl`` The maximum number of zoom levels. [0-10], valid for dm out

``-h|--help``

.. tip:: For feature requests or bug reports please open an issue `on github <http://github.com/ZhouQiangwei/dmtools>`__.
