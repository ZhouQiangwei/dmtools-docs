DMtools
=======

.. contents:: 
    :local:

dmtools main modules
^^^^^^^^^^^^^^^^^^^^

You can view and process dm file with dmtools:

.. code:: bash

    $ dmtools view -i mutant.methratio.dm | head
    
obtained text format methylation results


Main functions
^^^^^^^^^^^^^^

+---------------------+--------------------------------------------------------------------------+
| **[ Main paramaters ]**                                                                        |
+=====================+==========================================================================+
|                     | dmtools <mode> [opnions]                                                 |
+---------------------+--------------------------------------------------------------------------+
|Usage:                                                                                          |
+---------------------+--------------------------------------------------------------------------+
| [mode]              | bam2dm mr2dm view overlap regionstats bodystats profile chromstats       |
+---------------------+--------------------------------------------------------------------------+
| bam2dm              | calculate DNA methylation (DM format) with BAM file                      |
+---------------------+--------------------------------------------------------------------------+
| mr2dm               | convert txt meth file to dm format                                       |
+---------------------+--------------------------------------------------------------------------+
| view                | dm format to txt meth                                                    |
+---------------------+--------------------------------------------------------------------------+
| viewheader          | view header of dm file                                                   |
+---------------------+--------------------------------------------------------------------------+
| overlap             | overlap cytosine site with more than two dm files                        |
+---------------------+--------------------------------------------------------------------------+
| regionstats         | calculate DNA methylation level of per region                            |
+---------------------+--------------------------------------------------------------------------+
| bodystats           | calculate DNA methylation level of body, upstream and downstream.        |
+---------------------+--------------------------------------------------------------------------+
| profile             | calculate DNA methylation profile                                        |
+---------------------+--------------------------------------------------------------------------+
| chromstats          | calculate DNA methylation level across chromosome                        |
+---------------------+--------------------------------------------------------------------------+
| addzm               | add or change zoom levels for dm format, need for browser visulization   |
+---------------------+--------------------------------------------------------------------------+
| stats               | coverage and methylation level distribution of data                      |
+---------------------+--------------------------------------------------------------------------+
| -h|--help                                                                                      |
+---------------------+--------------------------------------------------------------------------+


dmtools bam2dm
^^^^^^^^^^^^^^

Calculate DNA methylation level from alignment BAM file to dm binary file:

.. code:: bash

    $ dmtools bam2dm -g genome.fa -b sample.sort.bam -m sample.methratio.dm
    
you can see more details with 'dmtools bam2dm -h'


dmtools mr2dm
^^^^^^^^^^^^^

Convert methratio txt file to dm binary file:

.. code:: bash

    $ dmtools mr2dm -g genome.fa.size -m mutant.methratio.txt --outdm mutant.methratio.dm
    
obtained dm format methylation results, you can see more details with 'dmtools mr2dm -h'

dmtools view
^^^^^^^^^^^^

You can view and process dm file with dmtools:

.. code:: bash

    $ dmtools view -i mutant.methratio.dm | head
      #Chr1	34	35	0.600000	5	-	CHG
      #Chr1	80	81	0.333333	6	-	CHH
      #Chr1	116	117	1.000000	4	-	CG
      #Chr1	117	118	0.250000	4	-	CHG
    
obtained text format methylation results

dmtools viewheader
^^^^^^^^^^^^^^^^^^

You can view the format of dm file with dmtools:

.. code:: bash

    $ dmtools viewheader -i mutant.methratio.dm
      #BM_END:    yes
      #BM_COVER:    yes
      #BM_CONTEXT:    yes
      #BM_STRAND:    yes
      #BM_ID:    no
      #Levels:     2
      # ...
      #Chromosome List
      #idx	Chrom	Length (bases)
      #0	Chr1	30427671
      #1	Chr2	19698289
      # ... 
    
obtained format of methylation results

dmtools overlap
^^^^^^^^^^^^^^^

Overlap cytosine site with more than two dm files:

.. code:: bash

    $ dmtools overlap -i sample1.methratio.dm -i2 sample2.methratio.dm
      ## chromsome pos context strand methy-sample1 coverage-sample1 methy-sample2 coverage-sample2
      #Chr1	34	CHG	-	0.600000	5	0.600000	5
      #Chr1	80	CHH	-	0.333333	6	0.333333	6
      #Chr1	116	CG	-	1.000000	4	1.000000	4
      #Chr1	117	CHG	-	0.250000	4	0.250000	4
      #Chr1	125	CHG	-	1.000000	4	1.000000	4

Or just with --dmfiles:

.. code:: bash

    $ dmtools overlap --dmfiles sample1.methratio.dm sample2.methratio.dm


dmtools regionstats
^^^^^^^^^^^^^^^^^^^

Calculate DNA methylation level of chromosome region, genes, or TEs:

.. code:: bash

    $ dmtools regionstats -i sample1.methratio.dm --gtf gene.gtf -o gene.meth.txt --printcoverage 1
      ## chromosome pos strand meth coverage geneid
      #Chr1	4396348	-	6	567	AT1G12920
      #Chr1	4396348	-	12	1552	AT1G12920
      #Chr1	4398375	-	114	3381	AT1G12930

or only print methylation level without coverage:

.. code:: bash

    $ dmtools regionstats -i sample1.methratio.dm --gtf gene.gtf -o gene.meth.txt --printcoverage 0
      ## chromosome pos methy-level geneid
      #Chr1	1618602	-	0.009665	AT1G05490
      #Chr1	1618602	-	0.014290	AT1G05490
      #Chr1	1624955	+	0.048446	AT1G05500
      #Chr1	1624955	+	0.213080	AT1G05500

Or with bed file:

.. code:: bash

    $ dmtools regionstats -i sample1.methratio.dm --bed gene.bed -o gene.meth.txt

Or just calculate DNA methylation level of same regions:

.. code:: bash

    $ dmtools regionstats -i sample1.methratio.dm -r chr1:1-2900;chr2:1-200,+ \
      -o gene.meth.txt

Please see 'dmtools regionstats' for more details.


dmtools bodystats
^^^^^^^^^^^^^^^^^

Calculate DNA methylation level of gene body, upstream and downstream:

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


dmtools profile
^^^^^^^^^^^^^^^

Calculate DNA methylation profile matrix and avarage matrix across gene body, upstream and downstream:

.. code:: bash

    $ dmtools profile -i sample1.methratio.dm --gtf gene.gtf -o gene.profile \
      --regionextend 2000 --bodyX 1 --matrixX 5 --profilemode 0

Or with bed file:

.. code:: bash

    $ dmtools profile -i sample1.methratio.dm --bed gene.bed -o gene.profile \
      --regionextend 2000 --bodyX 1 --matrixX 5 --profilemode 0

Please see 'dmtools profile' for more details.


dmtools chromstats
^^^^^^^^^^^^^^^^^^

Calculate DNA methylation level across chromosome:

.. code:: bash

    $ dmtools chromstats -i sample1.methratio.dm -o chromosome.meth.txt \
      --chromstep 100000 --stepmove 50000 --fstrand 3 --context 4

Please see 'dmtools chromstats' for more details.

dmtools addzm
^^^^^^^^^^^^^

Add or change zoom levels in DM file, needed for IGV browser:

.. code:: bash

    $ dmtools addzm -i sample.mr.dm -o sample.mr.zm5.dm --zl 5 

Please see 'dmtools addzm' for more details.


dmtools stats
^^^^^^^^^^^^^

Calculate DNA methylation data coverage and DNA methylation level category:

.. code:: bash

    $ dmtools stats -i sample1.methratio.dm -o chromosome.cover 

Please see 'dmtools stats' for more details.

.. tip:: For feature requests or bug reports please open an issue `on github <http://github.com/ZhouQiangwei/dmtools>`__.
