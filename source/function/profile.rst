dmtools profile
===============

.. contents:: 
    :local:

Description
^^^^^^^^^^^

DMtools can also calculate the DNA methylation profiles around genes, 
introns, exons, intergenic regions and TEs.

Calculating the distribution pattern of DNA methylation levels across genes and their 
upstream and downstream regions is crucial for understanding the role of gene regulation and epigenetics. 
Changes in the methylation levels of genes and promoter regions can affect gene expression and function. 
Previous studies have shown that high DNA methylation in promoter regions suppresses 
gene expression, while the opposite is true for gene regions. 
The distribution pattern of methylation levels in different genes and their upstream and downstream 
regions across different samples may be associated with specific biological processes and diseases. 
Therefore, by calculating and comparing the distribution patterns of DNA methylation levels in 
different samples and different genes' upstream and downstream regions within the same sample, 
we can better understand the role of DNA methylation in gene regulation and epigenetics.

Usage
^^^^^

Calculate DNA methylation profile matrix and average matrix across gene body, upstream and downstream:

.. code:: bash

    $ dmtools profile -i sample1.methratio.dm --gtf gene.gtf -o gene.profile \
      --regionextend 2000 --bodyX 1 --matrixX 5 --profilemode 0

Or with bed file:

.. code:: bash

    $ dmtools profile -i sample1.methratio.dm --bed gene.bed -o gene.profile \
      --regionextend 2000 --bodyX 1 --matrixX 5 --profilemode 0

Please see 'dmtools profile' for more details.


Parameters
^^^^^^^^^

``-i`` input DM file

``--bed`` bed file for view, format: chrom start end [strand].

``--gtf`` gtf file for view, format: chrom * * start end * strand * xx geneid.

``--gff`` gff file for view, format: chrom * * start end * strand * xx=geneid.

``-o`` output file [stdout]

``-p`` [int] threads

``--regionextend`` region extend for upstream and downstram, [2000]

``--profilestep`` [double] step mean bin size for chromosome region, default: 0.02 (2%)

``--profilemovestep`` [double] step move, default: profilestep/2, if no overlap, please define same as --profilestep

``--profilemode`` calculate the methylation matrix mode of every region or gene. 0 for gene and flanks mode, 1 for tss and flanks, 2 for tts and flanks, 3 for region center and flanks. [0]

``--bodyX`` [double] the gene body bin size is N multiple of the bin size of the upstream and downstream extension region. [1]

``--matrixX`` [int] the bin size is N times of the profile bin size, so the bin size should be N*profilestep [5], please note N*profilestep must < 1 and N must >= 1, used for calculation per gene.

``--strand`` [0/1/2] strand for calculate, 0 represent '+' positive strand, 1 '-' negative strand, 2 '.' all information, [2]

``--context`` [0/1/2/3] context for calculate, 0 represent 'C/ALL' context, 1 'CG' context, 2 'CHG' context, 3 'CHH' context. [0]

``--print2one`` [int] print all the matrix results of C/CG/CHG/CHH context methylation to same file. 0 for no, 1 for yes. [0]

``-h|--help``

.. tip:: For feature requests or bug reports please open an issue `on github <http://github.com/ZhouQiangwei/dmtools>`__.
