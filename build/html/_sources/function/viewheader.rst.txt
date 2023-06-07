dmtools viewheader
==================

.. contents:: 
    :local:

Description
^^^^^^^^^^

The DM format is a binary file format suitable for computer programs, 
and DMtools is a powerful operating tool that can perform a series of analysis tasks 
on this format. However, as the DM format is difficult for humans to read, 
we may want to extract some statistical information contained in the DM format.

The ``dmtools viewheader`` command can be used to view statistical information in the DM format, 
including the amount of information contained, the chromosome information contained, 
and more.

You can view the format of dm file with dmtools:

Usage
^^^^^

.. code:: bash

    $ dmtools viewheader -i mutant.methratio.dm
      #BM_END:    yes
      #BM_COVER:    yes
      #BM_CONTEXT:    yes
      #BM_STRAND:    yes
      #BM_ID:    no
      #Levels:     2
      # ...
      #Chromosome List
      #idx	Chrom	Length (bases)
      #0	Chr1	30427671
      #1	Chr2	19698289
      # ... 
    
obtained format of methylation results

Parameters
^^^^^^^^^

``-i`` input DM file

.. tip:: For feature requests or bug reports please open an issue `on github <http://github.com/ZhouQiangwei/dmtools>`__.
