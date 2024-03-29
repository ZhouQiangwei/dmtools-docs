Getting started
###############

.. contents::
    :depth: 2


DMtools is a C++ toolkits for the analysis and visulization of DNA methylation data.
For command analysis, you can use the ``dmtools`` executable.
For python analyses, user can use the ``Python API``.

The Basic DNA methylation (DM) format is a compressed binary indexed DNA methylation format for storing DNA methylation levels with methylation context, strand, coverage, and ID information. Compared with the commonly used file formats for DNA methylation, the storage space of the DM format is reduced by 80%-90%. Besides, based on the DM format file, users can realize fast random access and calculate DNA methylation levels of any chromosome region. Correspondingly, we provided dmtools, a manipulation tool in DM format. The dmtools implements various utilities for post-processing DNA methylation levels with DM format, such as fast and random access, calculation of DNA methylation profile across genes, and differential DNA methylation analysis. Moreover, we also provided a python package pydmtools for processing DM format files.



.. toctree::
    :maxdepth: 2
    
    Process raw fastq data <function/align>
    Calculate DNA meth from bam <function/bam2dm>
    Format convertion <function/dmtools-format>
    Estimate bs conversion rate <function/ebsrate>
    Calculate DNA meth with dm <function/dmtools-calme>
    Merge or overlap dm files <function/dmtools-merge>
    Manipulate dm format <function/dmtools-manu>
