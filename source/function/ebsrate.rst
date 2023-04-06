dmtools ebsrate
===============

.. contents:: 
    :local:

Description
^^^^^^^^^^

For bisulfite sequencing data, the level of DNA methylation is estimated by converting unmethylated cytosine (C) to thymine (T) and then calculating the percentage of T at sites where the reference genome is C. The accuracy of this estimation depends on the bisulfite conversion rate, which directly affects the percentage of C to T. To evaluate the conversion rate of bisulfite, lambda sequences are typically added during library construction. The Lambda sequence is a completely unmethylated sequence, so after bisulfite treatment, all C sites should be converted to T with 100% efficiency.

However, some WGBS data do not include lambda sequences for estimating the conversion rate of bisulfite. In such cases, we can use several alternative methods to evaluate the conversion rate: (1) calculating the mitochondrial methylation level (applicable to some mammals); (2) calculating the DNA methylation level of CHH (applicable to some animals); (3) calculating the methylation level of a specific chromosome specified by the user; and (4) calculating the methylation level of chloroplasts (applicable to some plants). It is important to note that some studies have reported DNA methylation in mitochondria, so using mitochondrial DNA methylation level to estimate the conversion rate of bisulfite requires careful consideration.

You can estimate the bisulfite conversion rate with dmtools:

Usage
^^^^^

.. code:: bash

    $ dmtools ebsrate -i mutant.methratio.dm --bsmode chh
      #dm bs-c-rate
      ###bs rate calculated by chh
      #ebsrate chh mode
      #CHH	chrM	0.004437
      #CHH	chr1	0.004765
      #CHH	chr2	0.004755
      #...
      #...
      #CHH	chrX	0.004585
      ###CHH level in all chromosome
      #CHH	+	0.004752
      #CHH	-	0.004714
      #CHH	.	0.004733
      ###estimated bs rate by CHH level in all chromosome
      #bsrate   0.004733
    
    $ dmtools ebsrate -i GSM1329865.zm0.dm --bsmode chrM
      #dm bs-c-rate
      ###bs rate calculated by chrM
      #ebsrate chr mode
      #Chromosome List chrM 16569
      #chrM	0	16569	0.005053	C	+
      #chrM	0	16569	0.005588	CG	+
      #chrM	0	16569	0.005007	CHG	+
      #chrM	0	16569	0.005001	CHH	+
      #chrM	0	16569	0.004336	C	-
      #chrM	0	16569	0.006145	CG	-
      #chrM	0	16569	0.003907	CHG	-
      #chrM	0	16569	0.003873	CHH	-
      ###estimated bs rate by chrM level
      #bsrate   0.004694

    $ dmtools ebsrate -i GSM1329865.zm0.dm --bsmode lambda
      ###estimated bs rate by lambda level
      #bsrate   0.01092
    
Parameters
^^^^^^^^

``-i`` input DM file

``-o`` output file

``--bsmode`` chh or chr mode, suggest chh for human, mouse etc.

``--chr`` chromosome used for calculate bisulfite convertion rate, default, chrM and chrC


.. tip:: For feature requests or bug reports please open an issue `on github <http://github.com/ZhouQiangwei/dmtools>`__.
