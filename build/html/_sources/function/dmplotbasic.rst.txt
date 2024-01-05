dmPlotBasic
===========

.. code:: bash

    $ dmtools stats -i sample1.methratio.dm -o prefix1 

    # user also can obtained coverage and levels of CG:
    $ dmtools stats -i sample1.methratio.dm -o prefix1.cg --context 1
      
    $ python3 dmPlotBasic.py -c prefix1.cover.txt prefix2.cover.txt -o tt.pdf


.. image:: ../media/plot-basic-coverage.png
   :height: 300 px
   :width: 560 px
   :alt: coverage
   :align: center

.. code:: bash

    $ dmtools bodystats -i prefix1.dm --gff gene.gff -o prefix1.bodym \
        --printcoverage 1

    $ python3 dmPlotBasic.py -f prefix1.bodym.cover.cg prefix2.bodym.cover.cg \
        -c prefix1.cover.txt prefix2.cover.txt -o tt.pdf

.. image:: ../media/plot-basic-boxplot.png
   :height: 300 px
   :width: 600 px
   :alt: boxplot
   :align: center

.. image:: ../media/plot-basic-corplot1.png
   :height: 300 px
   :width: 600 px
   :alt: corplot1
   :align: center

.. image:: ../media/plot-basic-corplot2.png
   :height: 300 px
   :width: 360 px
   :alt: corplot2
   :align: center

.. image:: ../media/plot-basic-coverage.png
   :height: 300 px
   :width: 600 px
   :alt: coverage
   :align: center