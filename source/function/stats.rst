dmtools stats
=============

.. contents:: 
    :local:

Description
^^^^^^^^^^

In DNA methylation analysis, coverage refers to the number of sequence reads in which information about each cytosine site can be detected. Higher coverage ensures data reliability and accuracy. Therefore, it is important to calculate the number and proportion of cytosine sites that meet a specific coverage threshold.
By calculating the number and proportion of cytosine sites with coverage greater than or equal to a specific threshold, we can assess the quality and reliability of DNA methylation data. A coverage threshold is usually chosen to ensure data accuracy and reliability. Additionally, coverage thresholds may vary for different samples, and calculating the number and proportion of cytosine sites at different coverage levels can better compare differences and similarities between samples.
In summary, calculating the number and proportion of cytosine sites that meet a specific coverage threshold is a crucial step in DNA methylation data analysis, as it helps us evaluate data quality and reliability.


Dividing DNA methylation levels into different intervals can help us better understand the distribution of DNA methylation in different regions. By calculating the number of DNA methylation sites in each interval, we can more accurately assess the degree of methylation at different methylation levels. This is essential for understanding the role of DNA methylation in gene regulation and epigenetics.
For example, we can divide DNA methylation levels into different intervals, such as 0-25%, 25-50%, 50-75%, 75-100%, and calculate the number and proportion of DNA methylation sites in each interval. This can help us gain a more comprehensive understanding of the role of DNA methylation in gene expression and functional regulation. In addition, the distribution of DNA methylation in different samples may differ. By calculating the number and proportion of DNA methylation sites in different intervals among different samples, we can compare the differences and similarities between different samples.
In summary, dividing DNA methylation levels into different intervals and calculating the number of DNA methylation sites in each interval is a crucial step in DNA methylation data analysis, which can evaluate the differences and similarities between different samples.

The DMtools ``stats`` command can calculate the number and proportion of cytosine sites that meet different coverage thresholds, as well as the number of cytosine sites at different DNA methylation levels.


Usage
^^^^^

Calculate DNA methylation data coverage and DNA methylation level category
------------------

.. code:: bash

    $ dmtools stats -i sample1.methratio.dm -o chromosome.cover --tc 1200559022

`--tc` is the total number of C and G in the genome, we can obtained by 'python count_cg.py genome.fa' in DMtools dir.

Count number of GC of genome
------------

.. code:: bash

    $ python count_cg.py hg38.chr.fa
    #599043897 C, 601515125 G and 1200559022 CG in genome

Output
^^^^

1. Calculate the number of cytosine sites with coverage greater than or equal to N, as well as the proportion of these sites among all cytosine sites.
 
 `chromosome.cover`

For example, in this test sample, the number of sites with DNA methylation coverage greater than 1 is 803251004, which accounts for 0.67 of all genomic cytosine sites.

.. code:: bash

   #cover   1       2       3       4       5       6       7       8       9       10      11      12      13      14      15      16
   #count   803251004       803251004       803251004       803251004       803251004       708649278       616748604       530217962       450748375       379329620       316287005       261534457       214678989       175127002       142130490       114926346
   #percent 0.67    0.67    0.67    0.67    0.67    0.59    0.51    0.44    0.38    0.32    0.26    0.22    0.18    0.15    0.12    0.10

2. Calculate the number of cytosine sites at different methylation levels. ``-s`` parameter change the size number.

`chromosome.cover.stats`

For example, in this test sample, the number of sites with DNA methylation levels equal to 0 is 700990500, and between (0-0.1] is 60990560, between (0.1-0.2] is 19059281.

.. code:: bash

    #catary  0   0.0    0.10    0.20    0.30    0.40    0.50    0.60    0.70    0.80    0.90
    #percent 700990500   60990560    19059281        4978777 6203698 5038056 2986205 1880708 1318675 561500  233544

Parameters
^^^^^^

``-i`` input DM file

``-o`` output file [stdout]

``--tc`` total number of cytosine and guanine in genome, we will use the number of site in dm file if you not provide --tc

``-r`` region for calculate stats, can be seperated by space. chr1:1-2900 chr2:1-200

``--bed`` bed file for calculate stats, format: chrom start end (strand).

``--strand`` [0/1/2] strand for show, 0 represent '+' positive strand, 1 '-' negative strand, 2 '.' all information

``--context`` [0/1/2/3] context for show, 0 represent 'C/ALL' context, 1 'CG' context, 2 'CHG' context, 3 'CHH' context.

``-s`` size of bin for count cytosine number.

``--mincover`` >= minumum coverage show, default: 0

``--maxcover`` <= maximum coverage show, default: 10000

``-h|--help``

.. tip:: For feature requests or bug reports please open an issue `on github <http://github.com/ZhouQiangwei/dmtools>`__.
