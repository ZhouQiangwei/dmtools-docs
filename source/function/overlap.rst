dmtools overlap
===============

.. contents:: 
    :local:

Description
^^^^^^^^^^^

The significance of calculating the overlap of DNA methylation sites across multiple methylome samples lies in identifying common methylation sites that may be associated with specific biological processes or diseases. By comparing methylation sites among different samples, researchers can determine which sites are methylated in multiple samples, thereby identifying potential regulatory regions and signaling pathways. Additionally, this analysis can help to determine DNA methylation patterns among different samples, further elucidating their relationships and relevance to specific diseases or biological processes. Therefore, calculating the overlap of DNA methylation sites across multiple methylome samples is of great significance in understanding the function and mechanisms of DNA methylation in biology and medicine.

Overlap cytosine site with more than two dm files:

Usage and output
^^^^^^^^

overlap with two dm files
---------------

.. code:: bash

    $ dmtools overlap -i sample1.methratio.dm -i2 sample2.methratio.dm
      ## chromsome pos context strand methy-sample1 coverage-sample1 methy-sample2 coverage-sample2
      #chr1	13079	CG	+	2	6	3	9
      #chr1	13082	CHG	+	0	7	0	9
      #chr1	13086	CHG	+	1	6	0	9
      #chr1	13092	CHG	+	0	6	0	8
      #chr1	13124	CHH	+	0	8	0	9

Or with --dmfiles for two or more DM files
---------------

.. code:: bash

    $ dmtools overlap --dmfiles sample1.methratio.dm,sample2.methratio.dm -r chr1:100-19000
    #chr1	13058	CHH	+	0	5	0	7
    #chr1	13059	CHG	+	0	5	0	7

Parameters
^^^^^^

``-i`` input DM file

``-i2`` input DM file2

``-r`` region for view, can be seperated by space. chr1:1-2900 chr2:1-200

``--bed`` bed file for view, format: chrom start end [strand].

``--dmfiles`` input DM files, seperated by comma. This is no need if you provide -i and -i2.

``-h|--help``

.. tip:: For feature requests or bug reports please open an issue `on github <http://github.com/ZhouQiangwei/dmtools>`__.
