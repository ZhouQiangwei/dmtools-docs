pydmtools
=========

.. contents:: 
    :local:

A python wrapper for dmtools

A python extension, written in C, for quick access to DM files and access to and creation of DM files. This extension uses dmtools for local and remote file access.

Installation
^^^^^^^^^^^^

You can install this extension directly from github with:

    $ pip install pydmtools

or with conda

    $ conda install pydmtools -c bioconda

Requirements
^^^^^^^^^^^^

The follow non-python requirements must be installed:

    libcurl (and the curl-config config)
    zlib

The headers and libraries for these are required.

Usage
^^^^^

Basic usage is as follows:

Load the extension
------------------

>>> import pydmtools as pydm

Open a DM file
This will work if your working directory is the pydmtools source code directory.

>>> dm = pydm.openfile("test/test.dm")
Note that if the file doesn't exist you'll see an error message and None will be returned. Be default, all files are opened for reading and not writing. You can alter this by passing a mode containing w:

>>> dm = pydm.openfile("test/output.dm", "w")
Note that a file opened for writing can't be queried for its intervals or statistics, it can only be written to. If you open a file for writing then you will next need to add a header (see the section on this below).


Access the list of chromosomes and their lengths
------------------------------------------------

binaMethFile objects contain a dictionary holding the chromosome lengths, which can be accessed with the chroms() accessor.

>>> dm.chroms()
dict_proxy({'chr1': 195471971L, 'chr10': 130694993L})
You can also directly query a particular chromosome.

>>> dm.chroms("chr1")
195471971L
The lengths are stored a the "long" integer type, which is why there's an L suffix. If you specify a non-existant chromosome then nothing is output.

>>> dm.chroms("chr1")

Print the header
----------------

It's sometimes useful to print a DM's header. This is presented here as a python dictionary containing: the version (typically 4), the number of zoom levels (nLevels), the number of bases described (nBasesCovered), the minimum value (minVal), the maximum value (maxVal), the sum of all values (sumData), and the sum of all squared values (sumSquared). The last two of these are needed for determining the mean and standard deviation.

>>> dm.header()
{'version': 61951, 'nLevels': 1, 'nBasesCovered': 2669, 'minVal': 0, 'maxVal': 1, 'sumData': 128.40874156728387, 'sumSquared': 97.26764956510321}


Compute summary information on a range
--------------------------------------

DM files are used to store values associated with positions and ranges of them. Typically we want to quickly access the average value over a range, which is very simple:

>>> dm.stats("chr1", 0, 10000)
[0.2000000054637591]
Suppose instead of the mean value, we instead wanted the maximum value:

>>> dm.stats("chr1", 0, 1000, type="max")
[0.30000001192092896]
Other options are "weighted" (the weighted average DNA methylation value)

It's often the case that we would instead like to compute values of some number of evenly spaced bins in a given interval, which is also simple:

>>> dm.stats("1",99, 200, nBins=2)
[1.399999976158142, 1.5]
nBins defaults to 1, just as type defaults to mean.

If the start and end positions are omitted then the entire chromosome is used:

>>> dm.stats("chr1")
[1.3351851569281683]


Retrieve values for individual bases in a range
-----------------------------------------------

While the stats() method can be used to retrieve the original values for each base (e.g., by setting nBins to the number of bases), it's preferable to instead use the getvalues() accessor.

>>> dm.getvalues("chr1", 0, 3)
[0.10000000149011612, 0.20000000298023224, 0.30000001192092896]
The list produced will always contain one value for every base in the range specified. If a particular base has no associated value in the DM file then the returned value will be nan.

>>> dm.getvalues("chr1", 0, 4)
[0.10000000149011612, 0.20000000298023224, 0.30000001192092896, nan]

Retrieve all intervals in a range
---------------------------------

Sometimes it's convenient to retrieve all entries overlapping some range. This can be done with the intervals() function:

>>> dm.intervals("chr1", 0, 3)
((0, 1, 0.10000000149011612), (1, 2, 0.20000000298023224), (2, 3, 0.30000001192092896))
What's returned is a list of tuples containing: the start position, end end position, and the value. Thus, the example above has values of 0.1, 0.2, and 0.3 at positions 0, 1, and 2, respectively.

If the start and end position are omitted then all intervals on the chromosome specified are returned:

>>> dm.intervals("chr1")
((0, 1, 0.10000000149011612), (1, 2, 0.20000000298023224), (2, 3, 0.30000001192092896), (100, 150, 1

Adding entries to a DM file
---------------------------

Assuming you've opened a file for writing and added a header, you can then add entries. Note that the entries must be added in order, as DM files always contain ordered intervals. There are three formats that DM files can use internally to store entries.

chr1	0	100	0.0
chr1	100	120	1.0
chr1	125	126	200.0
These entries would be added as follows:

>>> dm.addEntries(["chr1", "chr1", "chr1"], [0, 100, 125], ends=[5, 120, 126], values=[0.0, 1.0, 200.0])
Each entry occupies 12 bytes before compression.

Note that pydmtools will try to prevent you from adding entries in an incorrect order. This, however, requires additional over-head. Should that not be acceptable, you can simply specify validate=False when adding entries:

>>> dm.addEntries(["chr1", "chr1", "chr1"], [100, 0, 125], ends=[120, 5, 126], values=[0.0, 1.0, 200.0], validate=False)
You're obviously then responsible for ensuring that you do not add entries out of order. The resulting files would otherwise largley not be usable.

Close a DM file
---------------

A file can be closed with a simple 'dm.close()', as is commonly done with other file types. For files opened for writing, closing a file writes any buffered entries to disk, constructs and writes the file index, and constructs zoom levels. Consequently, this can take a bit of time.


**A note on coordinates and library using**

DM files use 1-based coordinates. And pydmtools and dmtools are based on libbigwig and pyBigWig

.. tip:: For feature requests or bug reports please open an issue `on github <http://github.com/ZhouQiangwei/pydmtools>`__.
