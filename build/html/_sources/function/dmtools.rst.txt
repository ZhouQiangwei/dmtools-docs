DMtools main modules
=======

.. contents:: 
    :local:

You can view and process dm file with dmtools:

.. code:: bash

    $ dmtools
    
obtained main modules in DMtools


+-----------------------------+------------------------------------------------------------------------+--------------------+
|                             | dmtools <mode> [opnions]                                               | Usage              |
+-----------------------------+------------------------------------------------------------------------+--------------------+
| [mode]                      | bam2dm mr2dm view ebsrate overlap regionstats bodystats profile etc.   |                    |
+-----------------------------+------------------------------------------------------------------------+--------------------+
| Methylation Calculate       |                                                                        |                    |
+-----------------------------+------------------------------------------------------------------------+--------------------+
| bam2dm                      | calculate DNA methylation (DM format) with BAM file                    | :doc:`bam2dm`      |
+-----------------------------+------------------------------------------------------------------------+--------------------+
| Format conversion           |                                                                        |                    |
+-----------------------------+------------------------------------------------------------------------+--------------------+
| mr2dm                       | convert txt meth file to dm format                                     | :doc:`mr2dm`       |
+-----------------------------+------------------------------------------------------------------------+--------------------+
| view                        | dm format to txt meth                                                  | :doc:`view`        |
+-----------------------------+------------------------------------------------------------------------+--------------------+
| Estimate bs conversion rate |                                                                        |                    |
+-----------------------------+------------------------------------------------------------------------+--------------------+
| ebsrate                     | estimate bisulfite conversion rate                                     | :doc:`ebsrate`     |
+-----------------------------+------------------------------------------------------------------------+--------------------+
| DM format                   |                                                                        |                    |
+-----------------------------+------------------------------------------------------------------------+--------------------+
| viewheader                  | view header of dm file                                                 | :doc:`viewheader`  |
+-----------------------------+------------------------------------------------------------------------+--------------------+
| Methylation analyses        |                                                                        |                    |
+-----------------------------+------------------------------------------------------------------------+--------------------+
| overlap                     | overlap cytosine site with more than two dm files                      | :doc:`overlap`     |
+-----------------------------+------------------------------------------------------------------------+--------------------+
| merge                       | merge more than 1 dm files to one dm file                              | :doc:`merge`       |
+-----------------------------+------------------------------------------------------------------------+--------------------+
| regionstats                 | calculate DNA methylation level of per region                          | :doc:`regionstats` |
+-----------------------------+------------------------------------------------------------------------+--------------------+
| bodystats                   | calculate DNA methylation level of body, upstream and downstream.      | :doc:`bodystats`   |
+-----------------------------+------------------------------------------------------------------------+--------------------+
| profile                     | calculate DNA methylation profile                                      | :doc:`profile`     |
+-----------------------------+------------------------------------------------------------------------+--------------------+
| chromstats                  | calculate DNA methylation level across chromosome                      | :doc:`chromstats`  |
+-----------------------------+------------------------------------------------------------------------+--------------------+
| chrmeth                     | calculate DNA methylation level of chromosomes                         | :doc:`chrmeth`     |
+-----------------------------+------------------------------------------------------------------------+--------------------+
| addzm                       | add or change zoom levels for dm format, need for browser visulization | :doc:`addzm`       |
+-----------------------------+------------------------------------------------------------------------+--------------------+
| stats                       | coverage and methylation level distribution of data                    | :doc:`stats`       |
+-----------------------------+------------------------------------------------------------------------+--------------------+
| dmDMR                       | differential DNA methylation analysis                                  | :doc:`DiffMeth`    |
+-----------------------------+------------------------------------------------------------------------+--------------------+
|                             |                                                                        |                    |
+-----------------------------+------------------------------------------------------------------------+--------------------+

.. toctree::
   :maxdepth: 2

   Calculate methylation from bam <bam2dm>
   Convert TXT to dm <mr2dm>
   View dm file <view>
   Add zoom level of dm file <addzm>
   Estimate bs conversion rate <ebsrate>
   View DM file header information <viewheader>
   Calculate DNA methylation <stats>
   Overlap dm files <overlap>
   Merge dm files <merge>
   Calculate DNA methylation for regions <regionstats>
   Calculate DNA methylation for gene body <bodystats>
   Calculate methylation profile across genes <profile>
   Calculate DNA methylation acorss chromosome <chromstats>
   Calculate DNA methylation for chromosome <chrmeth>


.. tip:: For feature requests or bug reports please open an issue `on github <http://github.com/ZhouQiangwei/dmtools>`__.
