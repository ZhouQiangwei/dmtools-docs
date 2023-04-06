dmtools bodystats
=================

.. contents:: 
    :local:

Description
^^^^^^^^^^^^

DMtools provides a ``bodystats`` command that can be used to calculate DNA methylation levels in user-specified regions of interest and their upstream and downstream regions. This feature is useful for researchers who may be interested in the methylation levels of specific genes, transposable elements (TEs), or other specified regions, as well as their upstream and downstream regions.

While the "regionstats" command can only calculate DNA methylation levels in specific regions, "bodystats" can calculate methylation levels in both the specified regions and their upstream and downstream regions, by combining with the "--regionextend" parameter.

By using the dmtools bodystats command, researchers can quickly and easily calculate the methylation levels in each region of interest as well as its upstream and downstream regions, and conduct further analysis and comparison.

To calculate the methylation density level in a given genomic region, 
only cytosines with coverage greater than the preset threshold are used. 
The DNA methylation level in a genomic region is defined as the total number of sequenced Cs over the 
total number of sequenced Cs and Ts at all cytosine positions across the region, 
and the equation is as follows:


.. math::

    ML(x)_{method} = \begin{cases}
    \dfrac{\sum_{i=1}^{N} C}{\sum_{i=1}^{N} (C + T)}, & \text{if method = weighted} \\
    \dfrac{\sum_{i=1}^{N} ML(x_{i})}{N}, & \text{if method = mean} \\
    \end{cases}


where N is the total number of cytosine sites whose coverage is more than the predefined threshold in the genomic region.


Calculate DNA methylation level of gene body, upstream and downstream:

Usage and output
^^^^^^^^^^^^^^^

.. code:: bash

    $ dmtools bodystats -i sample1.methratio.dm --gtf gene.gtf -o gene.meth.txt

Or with bed file:

.. code:: bash

    $ dmtools bodystats -i sample1.methratio.dm --bed gene.bed -o gene.meth.txt

Or just calculate DNA methylation level of same regions:

.. code:: bash

    $ dmtools bodystats -i sample1.methratio.dm -r chr1:1-2900;chr2:1-200,+ \
      -o gene.meth.txt

Please see 'dmtools bodystats' for more details.

Parameters
^^^^^^

``-i`` input DM file

``--bed`` bed file for view, format: chrom start end [strand].

``--gtf`` gtf file for view, format: chrom * * start end * strand * xx geneid.

``--gff`` gff file for view, format: chrom * * start end * strand * xx=geneid.

``-o`` output file [stdout]

``-r`` region for view, can be seperated by space. chr1:1-2900 chr2:1-200,+

``--method`` weighted/ mean

``--regionextend`` also calculate DNA methylation level of upstream and downstream N-bp window. default 2000.

``--strand`` [0/1/2/3] strand for show, 0 represent '+' positive strand, 1 '-' negative strand, 2 '.' all information, 3 calculate and print strand meth level seperately, only valid while -r para

``--context`` [0/1/2/3/4] context for show, 0 represent 'C/ALL' context, 1 'CG' context, 2 'CHG' context, 3 'CHH' context, 4 calculate and print strand meth level seperately, default: 4.

``--printcoverage`` [0/1] also print countC and coverage of body instead of methratio. [0]

``--print2one`` [int] print all the countC and coverage results of C/CG/CHG/CHH context methylation to same file, only valid when --printcoverage 1. 0 for no, 1 for yes. [0]

``-h|--help``

.. tip:: For feature requests or bug reports please open an issue `on github <http://github.com/ZhouQiangwei/dmtools>`__.
