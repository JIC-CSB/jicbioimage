Working with microscopy data
============================

Introduction
------------

One of the main driving forces behind the development of :mod:`jicbioimage` has
been the need to simplify programmatic analysis of microscopy data.

Microscopy data differ from normal images in that they can be multidimensional.
For example a microscopy image can consist of several z-slices, creating
something like a 3D object, as well as several time points, creating something
like a movie.

What this means in practise is that a microscopy datum is in reality a
collection of 2D images. What :mod:`jicbioimage` tries to do is to provide easy
access to the individual 2D images in the microscopy datum. This is achieved by
unzipping the content of the microscopy datum into a backend, which acts as a
type of cache of the individual 2D images.

However, microscopy data comes in a multitude of differing formats and it is
not the intention that :mod:`jicbioimage` should understand these formats
natively. Particularly as this is something that the
`Open Microscopy team <https://www.openmicroscopy.org/site>`_ already
does through its BioFormats project.

In order to be able to process microscopy data :mod:`jicbioimage` therefore
depends on the BioFormats command line tools. In particular the ``bfconvert``
tool, which is used to populate the backend.

For more information on how to install :mod:`jicbioimage` and the BioFormats
command line tools please see the :doc:`installation_notes`.


Image collection classes
------------------------

There are two image collection classes:

- :class:`jicbioimage.core.image.ImageCollection`
- :class:`jicbioimage.core.image.MicroscopyCollection`

These are used for managing access to the images stored within them.
To this end the :class:`jicbioimage.core.image.ImageCollection` class has got
the functions below:

- :meth:`jicbioimage.core.image.ImageCollection.image`
- :meth:`jicbioimage.core.image.ImageCollection.proxy_image`


The :class:`jicbioimage.core.image.MicroscopyCollection` class is more advanced
in that individual images can be accessed by specifying the series, channel,
zslice and timepoint of interest. For more information have a look at the API
documentation of:

- :meth:`jicbioimage.core.image.MicroscopyCollection.image`
- :meth:`jicbioimage.core.image.MicroscopyCollection.proxy_image`
- :meth:`jicbioimage.core.image.MicroscopyCollection.zstack_proxy_iterator`
- :meth:`jicbioimage.core.image.MicroscopyCollection.zstack_array`


Obtaining image collections
---------------------------

One can obtain a basic :class:`jicbioimage.core.image.ImageCollection` by loading a
multipage TIFF file into a :class:`jicbioimage.core.io.DataManager`.  Let us
therefore create a :class:`jicbioimage.core.io.DataManager`.

.. code-block:: python

    >>> from jicbioimage.core.io import DataManager
    >>> data_manager = DataManager()

Into which we can load the sample ``multipage.tif`` file.

.. code-block:: python

    >>> multipagetiff_fpath = "./tests/data/multipage.tif"

..
    This is just to make the doctest pass.

    >>> import os.path
    >>> multipagetiff_fpath = os.path.basename(multipagetiff_fpath)
    >>> import os.path
    >>> import jicbioimage.core
    >>> JICIMAGLIB = os.path.dirname(jicbioimage.core.__file__)
    >>> multipagetiff_fpath = os.path.join(JICIMAGLIB, "..", "..", "tests", "data", multipagetiff_fpath)

The :meth:`jicbioimage.core.io.DataManager.load` function returns the image
collection.

.. code-block:: python

    >>> image_collection = data_manager.load(multipagetiff_fpath)
    >>> type(image_collection)
    <class 'jicbioimage.core.image.ImageCollection'>
    
Which contains a number of :class:`jicbioimage.core.image.ProxyImage` instances.

.. code-block:: python

    >>> image_collection  # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    [<ProxyImage object at ...>,
     <ProxyImage object at ...>,
     <ProxyImage object at ...>]


.. _accessing-data-from-microscopy-collections:

Accessing data from microscopy collections
------------------------------------------

Suppose instead that we had a microscopy file. Here we will use the 
`z-series.ome.tif
<http://www.openmicroscopy.org/Schemas/Samples/2015-01/bioformats-artificial/z-series.ome.tif.zip>`_
file.

.. code-block:: python

    >>> zseries_fpath = "z-series.ome.tif"

..
    This is just to make the doctest pass.

    >>> zseries_fpath = os.path.join(JICIMAGLIB, "..", "..", "tests", "data", zseries_fpath)


Let us now load a microscopy file instead.

.. code-block:: python

    >>> microscopy_collection = data_manager.load(zseries_fpath)
    >>> type(microscopy_collection)
    <class 'jicbioimage.core.image.MicroscopyCollection'>
    >>> microscopy_collection  # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    [<MicroscopyImage(s=0, c=0, z=0, t=0) object at ...>,
     <MicroscopyImage(s=0, c=0, z=1, t=0) object at ...>,
     <MicroscopyImage(s=0, c=0, z=2, t=0) object at ...>,
     <MicroscopyImage(s=0, c=0, z=3, t=0) object at ...>,
     <MicroscopyImage(s=0, c=0, z=4, t=0) object at ...>]


One can now use a variety of methods to access the underlying microscopy
images. For example to access the third z-slice one could use the code snipped
below.

.. code-block:: python

    >>> microscopy_collection.proxy_image(z=2)  # doctest: +ELLIPSIS
    <MicroscopyImage(s=0, c=0, z=2, t=0) object at ...>

Alternatively to access the raw underlying image data of the same z-slice one
could use the code snippet below.

.. code-block:: python

    >>> microscopy_collection.image(z=2)  # doctest: +ELLIPSIS
    <Image object at 0x..., dtype=uint8>

Similarly one could loop over all the slices in the z-stack using the code
snippet below.

.. code-block:: python

    >>> for i in microscopy_collection.zstack_proxy_iterator():  # doctest: +ELLIPSIS
    ...     print(i)
    ...
    <MicroscopyImage(s=0, c=0, z=0, t=0) object at ...>
    <MicroscopyImage(s=0, c=0, z=1, t=0) object at ...>
    <MicroscopyImage(s=0, c=0, z=2, t=0) object at ...>
    <MicroscopyImage(s=0, c=0, z=3, t=0) object at ...>
    <MicroscopyImage(s=0, c=0, z=4, t=0) object at ...>


One can also access the z-stack as a :class:`numpy.ndarray`.

.. code-block:: python

    >>> microscopy_collection.zstack_array()  # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    array([[[ 0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0],
            ...
            [96, 96, 96, 96, 96],
            [96, 96, 96, 96, 96],
            [96, 96, 96, 96, 96]]], dtype=uint8)
    

However, it is often more convenient to access the z-stack as a
:class:`jicbioimage.core.image.Image3D` using the
:meth:`jicbioimage.core.image.MicroscopyCollection.zstack` method.

.. code-block:: python

    >>> microscopy_collection.zstack()  # doctest: +ELLIPSIS
    <Image3D object at 0x..., dtype=uint8>


..
    Tidy up: remove the ./backend directory we created and the png files

    >>> import shutil, glob
    >>> shutil.rmtree(data_manager.backend.directory)
    >>> png_files = glob.glob("*.png")
    >>> for file in png_files:
    ...     os.remove(file)
