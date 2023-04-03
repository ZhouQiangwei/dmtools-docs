.. dmtools documentation master file, created by
   sphinx-quickstart on Thu Dec 10 21:24:25 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

The Basic DNA Methylation (DM) format and DMtools
=================================================

.. image:: media/dmtools.png
   :height: 490 px
   :width: 620 px
   :alt: coverage
   :align: center

The Basic DNA methylation (DM) format is a compressed binary indexed DNA methylation format for storing DNA methylation levels with methylation context, strand, coverage, and ID information. Compared with the commonly used file formats for DNA methylation, the storage space of the DM format is reduced by 80%-90%. Besides, based on the DM format file, users can realize fast random access and calculate DNA methylation levels of any chromosome region. Correspondingly, we provided dmtools, a manipulation tool in DM format. The dmtools implements various utilities for post-processing DNA methylation levels with DM format, such as fast and random access, calculation of DNA methylation profile across genes, and differential DNA methylation analysis. Moreover, we also provided a python package pydmtools for processing DM format files.

**Installation**

* Please download and install the tools (see :doc:`function/install`)


The functions you can use dmtools to do:

* :doc:`function/dmtools`: tools for DNA methylation in dm format, and prepare DM simalar bigwig file for browser.
* :doc:`function/bam2dm`: Calulate DNA methylation level (ML) across whole genome output dm format.
* :doc:`function/DiffMeth`: Perform differential analyses with auto defined regions or predefined regions. 
* :doc:`function/PlotMeth`: Plot DNA ML profile, heatmap or boxplot across genes/TEs/etc. 
* :doc:`function/pydmtools`: A python wrapper for dmtools. 


Contents
--------
.. toctree::
   :maxdepth: 2

   function/dmtools
   function/bam2dm
   function/PlotMeth
   function/DiffMeth
   function/Requirements
   function/pydmtools


While developing dmtools, we continuously strive to create software
that fulfills the following criteria:

-  **new methlation dm format with index** can calculate DNA methylation level
   quickly.
-  **calculate DNA methylation level based on sorted BAM file** for single
   base or chromosome region and genes.
-  enable **customized down-stream analyses**, espacially with visulization
-  generation of **highly customizable images** (change colours, size,
   labels, file format, etc.)


Citation
^^^^^^^^

Please cite dmtools as follows:

Zhou Q, Chou C, Li G: The Basic DNA Methylation (DM) format and dmtools



.. tip:: For feature requests or bug reports please open an issue `on github <http://github.com/ZhouQiangwei/dmtools>`__.

