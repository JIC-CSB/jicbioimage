Working with transformations
============================

Introduction
------------

In image analysis one commonly wants to transform images. When putting an
image through several transforms it can be really useful to save out the
intermediate images to disk. Creating a visual audit track of the image
processing.

To make it painless to set-up such an audit trail :mod:`jicbioimage` provides
the function decorator
:func:`jicbioimage.core.transform.transformation`. When applied to a
transformation function the decorator adds both "autowriting" of the tranformed
image as well as a log in the history of the image.

Pre-built transformations
-------------------------

The :mod:`jicbioimage.transform` package constains a number of standard
image transformations that have had the
:func:`jicbioimage.core.transform.transformation` function decorator applied to
them.

For more information see
`<http://jicbioimage.readthedocs.org/projects/jicbioimagetransform>`_.


Creating a custom transform
---------------------------

Suppose that we wanted to create a transformation to invert our image. We can
achieve this by importing the :func:`jicbioimage.core.transform.transformation`
decorator.

.. code-block:: python

    >>> import numpy as np
    >>> from jicbioimage.core.transform import transformation
    >>> @transformation
    ... def invert(image):
    ...     """Return an inverted image."""
    ...     maximum = np.iinfo(image.dtype).max
    ...     maximum_array = np.ones(image.shape, dtype=image.dtype) * maximum
    ...     return maximum_array - image
    ...

..  
        # We do not want to write out the transforms to disk.
    >>> from jicbioimage.core.io import AutoWrite
    >>> AutoWrite.on = False

Let us create an image to apply our tranformation to.

.. code-block:: python

    >>> from jicbioimage.core.image import Image
    >>> ar = np.zeros((3,3), dtype=np.uint8)
    >>> im = Image.from_array(ar)

We can now apply the transformation to our image.

.. code-block:: python

    >>> invert(im)
    Image([[255, 255, 255],
           [255, 255, 255],
           [255, 255, 255]], dtype=uint8)


Specifying ``dtype`` contracts
------------------------------

Sometimes one want to be able to ensure that the input/output image(s)
are of a particular ``dtype``. This can be achieved using the function
decorator
:func:`jicbioimage.core.util.array.dtype_contract`.

.. code-block:: python

    >>> from jicbioimage.core.util.array import dtype_contract
    >>> @transformation
    ... @dtype_contract(input_dtype=bool, output_dtype=bool)
    ... def bool_invert(image):
    ...     """Return an inverted image."""
    ...     return np.logical_not(image)
    ...
    
If we try to apply this transform to an image of the wrong ``dtype`` we get
an informative error message.

.. code-block:: python

    >>> bool_invert(im)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: Invalid dtype uint8. Allowed dtype(s): [<type 'bool'>]


Customising the behaviour of the visual audit trail
---------------------------------------------------

By default the audit trail images are written to the working directory.
The location can be customised using
:attr:`jicbioimage.core.io.AutoName.directory` attribute.

The generation of the audit trail images can be turned off by setting
:attr:`jicbioimage.core.io.AutoWrite.on` attribute to ``False``.
