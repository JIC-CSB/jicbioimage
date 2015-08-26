Quick start guide
=================

Here we illustrate the use of :mod:`jicbioimage` to segment an image of Greek
coins from Pompeii.

First we load the image from `scikit-image <http://scikit-image.org/>`_
as a numpy array.

.. code-block:: python

    >>> import skimage.data
    >>> ar = skimage.data.coins()

We then create a :class:`jicbioimage.core.image.Image` instance from the array.

.. code-block:: python

    >>> from jicbioimage.core.image import Image
    >>> im = Image.from_array(ar)

If using IPython qtconsole/notebook the image can be viewed directly in
the interpreter.

.. code-block:: python

    >>> im  # doctest: +SKIP

.. image:: images/coins_raw.png
   :alt: Coins.


We can now segment the image using a number of standard transformations.

.. code-block:: python

    >>> from jicbioimage.transform import equalize_adaptive_clahe, smooth_gaussian, threshold_otsu
    >>> im = equalize_adaptive_clahe(im)
    >>> im = smooth_gaussian(im)
    >>> im = threshold_otsu(im)
    >>> im  # doctest: +SKIP

.. image:: images/coins_thresholded.png
   :alt: Coins thresholded.

When doing interactive image analysis it is often easy to forget what
transforms an image has undergone. Let us find out what the history of our
final image is.

.. code-block:: python

    >>> im.history  # doctest: +NORMALIZE_WHITESPACE
    ['Created image from array',
     'Applied equalize_adaptive_clahe transform',
     'Applied smooth_gaussian transform',
     'Applied threshold_otsu transform']
