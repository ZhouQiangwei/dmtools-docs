BMtools
=======

.. contents:: 
    :local:

BMtools main modules
^^^^^^^^^^^^^^^^^^^^

You can view and process bm file with bmtools:

.. code:: bash

    $ bmtools view -i mutant.methratio.bm | head
    
obtained text format methylation results


Main functions
^^^^^^^^^^^^^^

+---------------------+--------------------------------------------------------------------------+
| **[ Main paramaters ]**                                                                        |
+=====================+==========================================================================+
|                     | bmtools <mode> [opnions]                                                 |
+---------------------+--------------------------------------------------------------------------+
|Usage:                                                                                          |
+---------------------+--------------------------------------------------------------------------+
| [mode]              | mr2bm view overlap regionstats bodystats profile chromstats              |
+---------------------+--------------------------------------------------------------------------+
| bam2bm              | calculate DNA methylation (BM format) with BAM file                      |
+---------------------+--------------------------------------------------------------------------+
| mr2bm               | convert txt meth file to bm format                                       |
+---------------------+--------------------------------------------------------------------------+
| view                | bm format to txt meth                                                    |
+---------------------+--------------------------------------------------------------------------+
| viewheader          | view header of bm file                                                   |
+---------------------+--------------------------------------------------------------------------+
| overlap             | overlap cytosine site with more than two bm files                        |
+---------------------+--------------------------------------------------------------------------+
| regionstats         | calculate DNA methylation level of per region                            |
+---------------------+--------------------------------------------------------------------------+
| bodystats           | calculate DNA methylation level of body, upstream and downstream.        |
+---------------------+--------------------------------------------------------------------------+
| profile             | calculate DNA methylation profile                                        |
+---------------------+--------------------------------------------------------------------------+
| chromstats          | calculate DNA methylation level across chromosome                        |
+---------------------+--------------------------------------------------------------------------+
| addzm               | add or change zoom levels for bm format, need for browser visulization   |
+---------------------+--------------------------------------------------------------------------+
| stats               | coverage and methylation level distribution of data                      |
+---------------------+--------------------------------------------------------------------------+
| -h|--help                                                                                      |
+---------------------+--------------------------------------------------------------------------+


bmtools bam2bm
^^^^^^^^^^^^^^

Calculate DNA methylation level from alignment BAM file to bm binary file:

.. code:: bash

    $ bmtools bam2bm -g genome.fa -b sample.sort.bam -m sample.methratio.bm
    
you can see more details with 'bmtools bam2bm -h'


bmtools mr2bm
^^^^^^^^^^^^^

Convert methratio txt file to bm binary file:

.. code:: bash

    $ bmtools mr2bm -g genome.fa.size -m mutant.methratio.txt --outbm mutant.methratio.bm
    
obtained bm format methylation results, you can see more details with 'bmtools mr2bm -h'

bmtools view
^^^^^^^^^^^^

You can view and process bm file with bmtools:

.. code:: bash

    $ bmtools view -i mutant.methratio.bm | head
      #Chr1	34	35	0.600000	5	-	CHG
      #Chr1	80	81	0.333333	6	-	CHH
      #Chr1	116	117	1.000000	4	-	CG
      #Chr1	117	118	0.250000	4	-	CHG
    
obtained text format methylation results

bmtools viewheader
^^^^^^^^^^^^^^^^^^

You can view the format of bm file with bmtools:

.. code:: bash

    $ bmtools viewheader -i mutant.methratio.bm
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

bmtools overlap
^^^^^^^^^^^^^^^

Overlap cytosine site with more than two bm files:

.. code:: bash

    $ bmtools overlap -i sample1.methratio.bm -i2 sample2.methratio.bm
      ## chromsome pos context strand methy-sample1 coverage-sample1 methy-sample2 coverage-sample2
      #Chr1	34	CHG	-	0.600000	5	0.600000	5
      #Chr1	80	CHH	-	0.333333	6	0.333333	6
      #Chr1	116	CG	-	1.000000	4	1.000000	4
      #Chr1	117	CHG	-	0.250000	4	0.250000	4
      #Chr1	125	CHG	-	1.000000	4	1.000000	4

Or just with --bmfiles:

.. code:: bash

    $ bmtools overlap --bmfiles sample1.methratio.bm sample2.methratio.bm


bmtools regionstats
^^^^^^^^^^^^^^^^^^^

Calculate DNA methylation level of chromosome region, genes, or TEs:

.. code:: bash

    $ bmtools regionstats -i sample1.methratio.bm --gtf gene.gtf -o gene.meth.txt --printcoverage 1
      ## chromosome pos strand meth coverage geneid
      #Chr1	4396348	-	6	567	AT1G12920
      #Chr1	4396348	-	12	1552	AT1G12920
      #Chr1	4398375	-	114	3381	AT1G12930

or only print methylation level without coverage:

.. code:: bash

    $ bmtools regionstats -i sample1.methratio.bm --gtf gene.gtf -o gene.meth.txt --printcoverage 0
      ## chromosome pos methy-level geneid
      #Chr1	1618602	-	0.009665	AT1G05490
      #Chr1	1618602	-	0.014290	AT1G05490
      #Chr1	1624955	+	0.048446	AT1G05500
      #Chr1	1624955	+	0.213080	AT1G05500

Or with bed file:

.. code:: bash

    $ bmtools regionstats -i sample1.methratio.bm --bed gene.bed -o gene.meth.txt

Or just calculate DNA methylation level of same regions:

.. code:: bash

    $ bmtools regionstats -i sample1.methratio.bm -r chr1:1-2900;chr2:1-200,+ \
      -o gene.meth.txt

Please see 'bmtools regionstats' for more details.


bmtools bodystats
^^^^^^^^^^^^^^^^^

Calculate DNA methylation level of gene body, upstream and downstream:

.. code:: bash

    $ bmtools bodystats -i sample1.methratio.bm --gtf gene.gtf -o gene.meth.txt

Or with bed file:

.. code:: bash

    $ bmtools bodystats -i sample1.methratio.bm --bed gene.bed -o gene.meth.txt

Or just calculate DNA methylation level of same regions:

.. code:: bash

    $ bmtools bodystats -i sample1.methratio.bm -r chr1:1-2900;chr2:1-200,+ \
      -o gene.meth.txt

Please see 'bmtools bodystats' for more details.


bmtools profile
^^^^^^^^^^^^^^^

Calculate DNA methylation profile matrix and avarage matrix across gene body, upstream and downstream:

.. code:: bash

    $ bmtools profile -i sample1.methratio.bm --gtf gene.gtf -o gene.profile \
      --regionextend 2000 --bodyX 1 --matrixX 5 --profilemode 0

Or with bed file:

.. code:: bash

    $ bmtools profile -i sample1.methratio.bm --bed gene.bed -o gene.profile \
      --regionextend 2000 --bodyX 1 --matrixX 5 --profilemode 0

Please see 'bmtools profile' for more details.


bmtools chromstats
^^^^^^^^^^^^^^^^^^

Calculate DNA methylation level across chromosome:

.. code:: bash

    $ bmtools chromstats -i sample1.methratio.bm -o chromosome.meth.txt \
      --chromstep 100000 --stepmove 50000 --fstrand 3 --context 4

Please see 'bmtools chromstats' for more details.

bmtools addzm
^^^^^^^^^^^^^

Add or change zoom levels in BM file, needed for IGV browser:

.. code:: bash

    $ bmtools addzm -i sample.mr.bm -o sample.mr.zm5.bm --zl 5 

Please see 'bmtools addzm' for more details.


bmtools stats
^^^^^^^^^^^^^

Calculate DNA methylation data coverage and DNA methylation level category:

.. code:: bash

    $ bmtools stats -i sample1.methratio.bm -o chromosome.cover 

Please see 'bmtools stats' for more details.

.. tip:: For feature requests or bug reports please open an issue `on github <http://github.com/ZhouQiangwei/BMtools>`__.
