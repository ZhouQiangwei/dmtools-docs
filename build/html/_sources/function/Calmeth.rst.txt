Calculate DNA methylation level
===============================

.. contents:: 
    :local:

Calmeth
-------

Calculate DNA methylation level from alignment files, you can obtained single-base cytosine DNA
methylation results, and the chromosome region DNA methylation levels files.

.. code:: bash

    An example usage is:
      with bam file:
        bmtools bam2bm [options] -g genome.fa -b alignment.sort.bam -m output.methrario.bm

.. important:: The sam or bam file MUST sorted by `samtools sort`.


Paramaters
----------

+---------------------+--------------------------------------------------------------------------+
| **[ Main paramaters ]**                                                                        |
+=====================+==========================================================================+
| -m/--methratio      | [MethFileNamePrefix]  Predix of methratio output file (bm)               |
+---------------------+--------------------------------------------------------------------------+
| --genome/-g         | Name of the genome mapped against, MUST build index first :doc:`bdindex` |
+---------------------+--------------------------------------------------------------------------+
| -i/--input          | Sam format file, sorted by samtools sort.                                |
+---------------------+--------------------------------------------------------------------------+
| -b/--binput         | Bam format file, sorted by samtools sort.                                |
+---------------------+--------------------------------------------------------------------------+
| -Q [int]            | caculate the methratio while read QulityScore >= Q. default:20           |
+---------------------+--------------------------------------------------------------------------+
| -n [float]          | Number of mismatches, default 0.06 percentage of read length. [0-1]      |
+---------------------+--------------------------------------------------------------------------+
| -c|--coverage       | >= <INT> coverage. default:4                                             |
+---------------------+--------------------------------------------------------------------------+
| -nC                 | >= <INT> Cs per region. default:1                                        |
+---------------------+--------------------------------------------------------------------------+
| -r/--remove_dup     |  REMOVE_DUP, default:true                                                |
+----+----------------+--------------------------------------------------------------------------+
| --zl                | The maximum number of zoom levels. [1-10], default: 2                    |
+----+----------------+--------------------------------------------------------------------------+
| -as [0/1]           | If print calculated alignment reads in sam/bam file. default:0           |
+----+----------------+--------------------------------------------------------------------------+
| --mrtxt             |  also print prefix.methratio.txt file                                    |
+----+----------------+--------------------------------------------------------------------------+
| --help/-h           | Print help                                                               |
+---------------------+--------------------------------------------------------------------------+


Output files
------------

.. code:: bash

    1. prefix.methratio.bm (binary file with index, view and processed with BMtools)

Output file format
------------------

.. code:: bash

    1. methratio.bm (binary file, view and processed with bmtools)
        Chromosome Loci (end) methlevel CT_count Strand Context
        # ex. bmtools view -i test.mr.bm -r Chr1:61-61
        # ex. Chr1    61      0.286364  11  +       CHH
        # CT_count     The number of coverage in this base pair.
        # BigWig for genome browser, suggest with end col.


.. tip:: For feature requests or bug reports please open an issue `on github <http://github.com/ZhouQiangwei/BMtools>`__.
