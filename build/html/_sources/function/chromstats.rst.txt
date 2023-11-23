dmtools chromstats
==================

.. contents:: 
    :local:

Description
^^^^^^^^^^

DMtools can calculate and visualize cytosine methylation density at the chromosome level. 
The bins represent a sliding window of N-kb with a step of S-kb.
N represent --chromstep paramater and S represent --stepmove paramater.

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


Calculate DNA methylation level across chromosome

Usage
^^^^^

.. code:: bash

    $ dmtools chromstats -i sample1.methratio.dm -o chromosome.meth.txt \
      --chromstep 100000 --stepmove 50000
    ## output file format `chromosome.meth.txt`
    ## chrom start end methlevel context strand
    #chrM    0       16569   0.004313        C       .
    #chrM    0       16569   0.005997        CG      .
    #chrM    0       16569   0.003897        CHG     .
    #chrM    0       16569   0.003890        CHH     .
    # ... ...
    #chr1    200000  300000  0.022242        C       .
    #chr1    200000  300000  0.313409        CG      .
    #chr1    200000  300000  0.003797        CHG     .
    #chr1    200000  300000  0.005633        CHH     .

Parameters
^^^^^^^^

``-i`` input dm file

``-o`` output file of calculated DNA methylation levels for all bins

``--method`` weighted/ mean/ min/ max/ cover/ dev methods for calculate DNA methylation in per bin

``--chromstep`` [int] step mean bin size for chromosome region, default: 100000

``--stepmove`` [int] step move, default: 50000, if no overlap, please define same as --chromstep

``--fstrand`` [0/1/2/3] strand for calculation, 0 represent '+' positive strand, 1 '-' negative strand, 2 '.' without strand information, 3 calculate and print strand meth level seperately. [2]

``--context`` [0/1/2/3/4] context for calculate, 0 represent 'C/ALL' context, 1 'CG' context, 2 'CHG' context, 3 'CHH' context, 4 calculate and print context meth level seperately. [4]
 
``--printcoverage`` [0/1] print countC and coverage instead of methratio. [0]

``--print2one`` [int] print all the countC and coverage results of C/CG/CHG/CHH context methylation to same file, only valid when --printcoverage 1. 0 for no, 1 for yes. [0]

``-h|--help`` usage

Please see 'dmtools chromstats' for more details.

.. tip:: For feature requests or bug reports please open an issue `on github <http://github.com/ZhouQiangwei/dmtools>`__.

