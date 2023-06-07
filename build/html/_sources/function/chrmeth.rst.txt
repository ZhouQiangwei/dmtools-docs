dmtools chrmeth
===============

.. contents:: 
    :local:

Description
^^^^^^^^^^

DMtools can calculate cytosine methylation level of one chromosome. 

To calculate the methylation density level of one chromosome, 
only cytosines with coverage greater than the preset threshold are used. 
The DNA methylation level in this chromosome is defined as the total number of sequenced Cs over the 
total number of sequenced Cs and Ts at all cytosine positions across this chromosome, 
and the equation is as follows:

.. math::

    ML(x)_{method} = \begin{cases}
    \dfrac{\sum_{i=1}^{N} C}{\sum_{i=1}^{N} (C + T)}, & \text{if method = weighted} \\
    \dfrac{\sum_{i=1}^{N} ML(x_{i})}{N}, & \text{if method = mean} \\
    \end{cases}


where N is the total number of cytosine sites whose coverage is more than the predefined threshold in the chromosome.


Usage
^^^^^

Calculate DNA methylation level of one chromosome:

.. code:: bash

    $ dmtools chrmeth -i sample1.methratio.dm -o chromosome.chr1me.txt \
      --chr chr1
    #chr1	0	248956422	0.019026	C	+
    #chr1	0	248956422	0.303933	CG	+
    #chr1	0	248956422	0.004569	CHG	+
    #chr1	0	248956422	0.004762	CHH	+
    #chr1	0	248956422	0.018981	C	-
    #chr1	0	248956422	0.303064	CG	-
    #chr1	0	248956422	0.004570	CHG	-
    #chr1	0	248956422	0.004769	CHH	-

Please see 'dmtools chrmeth' for more details.

Parameters
^^^^^^^

``-i`` input DM file

``-o`` output file

``--chr`` chromosome for cal.

.. tip:: For feature requests or bug reports please open an issue `on github <http://github.com/ZhouQiangwei/dmtools>`__.
