IPython integration
===================

The image classes in :mod:`jicbioimage` have been designed to integrate with
IPython qtconsole/notebook in that the image can be displayed directly in the
console/notebook.

To illustrate the behaviour let us create a simple RGB image with some coloured
squares.

.. code-block:: python

    >>> import numpy as np
    >>> from jicbioimage.core.image import Image
    >>> 
    >>> # Create the initial black image.
    >>> ar = np.zeros((175, 175, 3), dtype=np.uint8)
    >>> im = Image.from_array(ar)
    >>> 
    >>> # Add full intensity to R, G, B channels at offset squares.
    >>> im[25:100:, 25:100, 0] = 255
    >>> im[50:125, 50:125, 1] = 255
    >>> im[75:150, 75:150, 2] = 255

To display the image in the IPython qtconsole/notebook one simply needs access
it.

.. code-block:: python

    >>> im  # doctest: +SKIP

.. image:: images/rgb_squares.png
   :alt: RGB image with some coloured squares.

The behaviour works in IPython qtconsole/notebook with the classes listed
below.

- :class:`jicbioimage.core.image.Image`
- :class:`jicbioimage.core.image.ProxyImage`
- :class:`jicbioimage.core.image.MicroscopyImage`
- :class:`jicbioimage.segment.SegmentedImage`
- :class:`jicbioimage.illustrate.Canvas`
- :class:`jicbioimage.illustrate.AnnotatedImage`

Furthermore the collection classes listed below will display summary
information and thumbnails of all the images in the collection in IPython
notebook.

- :class:`jicbioimage.core.image.ImageCollection`
- :class:`jicbioimage.core.image.MicroscopyCollection`
