dmtools merge
==============

.. contents:: 
    :local:

Description
^^^^^^^^^^^

The merging of methylation results from multiple samples at the single-base resolution is crucial for downstream analysis and interpretation of DNA methylation patterns. It enables the identification of methylation differences between groups and provides a comprehensive view of the DNA methylation landscape across different samples. Moreover, it increases the statistical power of the analysis and facilitates the discovery of biologically significant changes in methylation patterns. Overall, merging methylation results from multiple samples is a critical step in epigenetic research that can uncover valuable insights into the role of DNA methylation in other analysis.

Usually, samples have different coverage, and some of them may even have insufficient sequence coverage at certain sites. Therefore, merging different samples is a complex task. DMtools supports the merging of DNA methylation results of one or multiple samples based on individual base pairs, which provides convenience for downstream analysis.

Merge cytosine site with more than two dm files:

Usage and output
^^^^^^^^

merge two dm files
---------------

.. code:: bash

    $ dmtools merge -i sample1.methratio.dm,sample2.methratio.dm
      ### sample1
      #chr1	13079	CG	+	2	6
      #chr1	13082	CHG	+	0	7
      #chr1	13086	CHG	+	1	6
      #chr1	13092	CHG	+	0	6
      ### sample2
      #chr1	13079	CG	+	3	9
      #chr1	13082	CHG	+	0	9
      #chr1	13086	CHG	+	0	9
      #chr1	13124	CHH	+	0	8

      ### out file
      #chr1	13079	CG	+	5	15
      #chr1	13082	CHG	+	0	16
      #chr1	13086	CHG	+	1	15
      #chr1	13092	CHG	+	0	6
      #chr1	13124	CHH	+	0	8

Or with two or more DM files
---------------

.. code:: bash

    $ dmtools overlap -i sample1.methratio.dm,sample2.methratio.dm,sample3.methratio.dm --method weighted
    #chr1	13058	CHH	+	0	5
    #chr1	13059	CHG	+	0	5

Parameters
^^^^^^

``-i`` input DM file

``-o`` output file

``--method`` method for merge overlap sites, weighted/ mean, [weighted]

``--mincover`` >= minumum coverage show, default: 0

``--maxcover`` <= maximum coverage show, default: 10000

``--outformat`` txt or dm format [txt]

``--zl`` The maximum number of zoom levels. [0-10], valid for dm out

``-h|--help``

.. tip:: For feature requests or bug reports please open an issue `on github <http://github.com/ZhouQiangwei/dmtools>`__.
