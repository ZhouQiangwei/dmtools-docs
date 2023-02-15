DiffMeth
========

.. contents:: 
    :local:

DMC or DMR/DMG
^^^^^^^^^^^^^^^

.. image:: ../media/diffmeth.png
   :height: 580px
   :width: 800 px
   :scale: 80 %
   :alt: alternate text
   :align: center

You can get dmc and dmr result with:

.. code:: bash

    $ dmDMR -p mutant.output.dm \
    -1 mutant.methratio.dm -2 WT.methratio.dm \
    --methdiff 0.2 --minstep 100 --mindmc 5 --pval 0.01
    
obtained hyper、hypo dmc/dmr from dmc/dmr results

.. code:: bash

    $ awk -v OFS="\t" 'gsub(/\,/,"\t",$NF)' mutant.output.dmr | \
    awk '$(NF-2)>4 && $NF<=1'  > mutant.output.hyper.dmr
    $ awk -v OFS="\t" 'gsub(/\,/,"\t",$NF)' mutant.output.dmr | \
    awk '!($(NF-2)>4 && $NF<=1)'  > mutant.output.hypo.dmr
    $ awk '$NF>0' mutant.output.dmc | awk '{print $1"\t"$2"\t"$2}' \
    > mutant.output.hyper.dmc
    $ awk '$NF<0' mutant.output.dmc | awk '{print $1"\t"$2"\t"$2}' \
    > mutant.output.hypo.dmc

Usage
^^^^^

+---------------------+--------------------------------------------------------------------------+
| **[ Main paramaters ]**                                                                        |
+=====================+==========================================================================+
| -p                  | output file prefix                                                       |
+---------------------+--------------------------------------------------------------------------+
| -1                  | sample1 methy dm files, sperate by comma.                                |
+---------------------+--------------------------------------------------------------------------+
| -2                  | sample2 methy dm files, sperate by comma.                                |
+---------------------+--------------------------------------------------------------------------+
| --mindmc            | min dmc sites in dmr region. [default : 4]                               |
+---------------------+--------------------------------------------------------------------------+
| --minstep           | min step in bp [default : 100]                                           |
+---------------------+--------------------------------------------------------------------------+
| --maxdis            | max length of dmr [default : 0]                                          |
+---------------------+--------------------------------------------------------------------------+
| --pvalue            | pvalue cutoff, default: 0.01                                             |
+---------------------+--------------------------------------------------------------------------+
| --FDR               | adjust pvalue cutoff default : 1.0                                       |
+---------------------+--------------------------------------------------------------------------+
| --methdiff          | the cutoff of methylation differention. default: 0.25 [CpG]              |
+---------------------+--------------------------------------------------------------------------+
| --element           | caculate predefinded region, input file with id.                         |
+---------------------+--------------------------------------------------------------------------+
| --context           | Context for DM. CG/CHG/CHH/C, [C]                                        |
+---------------------+--------------------------------------------------------------------------+
| -h|--help                                                                                      |
+---------------------+--------------------------------------------------------------------------+


1. Auto define DMR region according the dmc 

.. code:: bash

    dmDMR -p dm.output -1 [sample1.methC.dm,replicates ..] \
    -2 [sample2.methC.dm,replicates ..]

2. Pre-definded regions (Gene/TE/UTR/CDS or other regions, not suggest) 

.. code:: bash

    dmDMR -L -o_dm dm.output -1 [sample1.methC.dm,replicates ..] \
    -2 [sample2.methC.dm,replicates ..]


Output file
^^^^^^^^^^^

1. DMC

.. code:: bash

    # format
    Chrom position starnd context pvalue adjust_pvalue combine_pvalue corrected_pvalue \
    cover_sample1 meth_sample1 cover_sample2 cover_sample2 meth.diff 
    
2. DMR

.. code:: bash

    # format
    Chrom start end methlevelInSample1 methlevelInSample2 NdmcInRegion hypermdc,hypodmc



.. tip:: For feature requests or bug reports please open an issue `on github <http://github.com/ZhouQiangwei/dmtools>`__.
