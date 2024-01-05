align
======

.. contents:: 
    :local:

Description
-----------

In the preprocessing and alignment of DNA methylation data, the combination of Fastp and BWA-MEM provides a robust and efficient solution. 
Fastp ensures the removal of low-quality reads and adapter contamination, thereby enhancing the overall data quality.

Following preprocessing with Fastp, the cleaned data is then subjected to alignment using BWA-MEM, a widely used aligner for mapping sequencing reads to a reference genome. 
The aligned data serves as a crucial foundation for downstream analyses, enabling the identification of methylated regions and providing insights into the epigenetic landscape.


Usage
-----

.. code:: bash

    An example usage is:
        dmtools align --fastp fastp -g genome.fa -1 te1.fq -2 te2.fq -g genome.fa -o meth.bam

.. important:: genome.fa should be indexed with `dmtools index -g genome.fa`.

.. important:: if --fastp is not defined, the input file should be clean data.


Paramaters
----------

+---------------------+--------------------------------------------------------------------------+
| **[ Main paramaters ]**                                                                        |
+=====================+==========================================================================+
| --genome/-g         | Name of the genome mapped against, MUST build index first `dmtools index`|
+---------------------+--------------------------------------------------------------------------+
| -i                  | input file, support .fq/.fastq and .gz/.gzip format.                     |
+---------------------+--------------------------------------------------------------------------+
| -1                  | input file left end, if single-end. please use -i                        |
+---------------------+--------------------------------------------------------------------------+
| -2                  | input file right end                                                     |
+---------------------+--------------------------------------------------------------------------+
| -o                  | Prefix of BAM output file                                                |
+---------------------+--------------------------------------------------------------------------+
| --fastp             | fastp program location for fastq preprocess.                             |
+---------------------+--------------------------------------------------------------------------+
| -p                  | [int] threads                                                            |
+---------------------+--------------------------------------------------------------------------+
| --help/-h           | Print help                                                               |
+---------------------+--------------------------------------------------------------------------+


.. tip:: For feature requests or bug reports please open an issue `on github <http://github.com/ZhouQiangwei/dmtools>`__.
