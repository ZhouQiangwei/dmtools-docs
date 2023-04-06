dmtools overlap
===============

.. contents:: 
    :local:

Description
^^^^^^^^^^^

The merging of methylation results from multiple samples at the single-base resolution is crucial for downstream analysis and interpretation of DNA methylation patterns. It enables the identification of methylation differences between groups and provides a comprehensive view of the DNA methylation landscape across different samples. Moreover, it increases the statistical power of the analysis and facilitates the discovery of biologically significant changes in methylation patterns. Overall, merging methylation results from multiple samples is a critical step in epigenetic research that can uncover valuable insights into the role of DNA methylation in other analysis.

Usually, samples have different coverage, and some of them may even have insufficient sequence coverage at certain sites. Therefore, merging different samples is a complex task. DMtools supports the merging of DNA methylation results of one or multiple samples based on individual base pairs, which provides convenience for downstream analysis.

Overlap cytosine site with more than two dm files:

Usage and output
^^^^^^^^

.. code:: bash

    $ dmtools overlap -i sample1.methratio.dm -i2 sample2.methratio.dm
      ## chromsome pos context strand methy-sample1 coverage-sample1 methy-sample2 coverage-sample2
      #chr1	13079	CG	+	2	6	3	9
      #chr1	13082	CHG	+	0	7	0	9
      #chr1	13086	CHG	+	1	6	0	9
      #chr1	13092	CHG	+	0	6	0	8
      #chr1	13124	CHH	+	0	8	0	9

Or just with --dmfiles:

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
