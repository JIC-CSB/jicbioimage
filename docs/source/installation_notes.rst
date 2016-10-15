Installation notes
==================

Introduction
^^^^^^^^^^^^

We have tried to make it as easy as possible to install
and use the :mod:`jicbioimage` package. Here we detail two
options:

- :ref:`Manual install`
- :ref:`Using Docker`

If you are not familiar with  `Docker <https://www.docker.com/>`_ it
is probably easiest to start with a manual install.
However, if you are already familiar with Docker it is certainly a
very convenient way of creating an environment in which to install and run
:mod:`jicbioimage`.


.. _Manual install:

Manual install
^^^^^^^^^^^^^^

Install the freeimage library
-----------------------------

The :mod:`jicbioimage` package depends on
`freeimage <http://freeimage.sourceforge.net/>`_ to open image file.

On Linux bases system freeimage can usually be installed using the package
manager.  For example on Fedora it can be installed using the command below.

::

    yum install freeimage

On Macs it can be installed using `homebrew <http://brew.sh/>`_ using the
command below.

::

    brew install freeimage

On Windows download and unzip the
`FreeImage DLL <http://downloads.sourceforge.net/freeimage/FreeImage3170Win32Win64.zip>`_
(in the example below this was done to the root of the ``C:`` drive).
You will then need to add the relevant directory to your ``PATH``, for example on a
64-bit system::

    set PATH=C:\FreeImage\Dist\x64;%PATH%

Install the Python package dependencies
---------------------------------------

The :mod:`jicbioimage` package depends on a number of other scientific Python
packages. These can be installed using
`pip <https://pypi.python.org/pypi/pip>`_.

::

    pip install numpy
    pip install scipy
    pip install scikit-image

Although the :mod:`jicbioimage` package does not depend on it you may also want
to install the IPython notebook. The :mod:`jicbioimage` package has been
designed to work well with IPython notebook, for example by providing the
ability to view :class:`jicbioimage.core.image.Image` and
:class:`jicbioimage.core.image.ImageCollection` objects as images and tables of
images in the IPython notebook.

::

    pip install jupyter



Install the BioFormats command line tools
-----------------------------------------

The :mod:`jicbioimage` package does not explicitly depend on the BioFormats
command line tools. However, they are needed if you want to be able to work
with microscopy files.

Download the `bftools.zip
<http://downloads.openmicroscopy.org/latest/bio-formats/artifacts/bftools.zip>`_
file from the `openmicroscopy website
<https://downloads.openmicroscopy.org/latest/bio-formats/>`_.

.. warning:: :mod:`jicbioimage.core` version 0.14 and greater require
             BioFormats to be version 5.2.1 or greater to make use of the
             ``-nolookup`` option.

You will then need to unzip the file and add it to your ``PATH``.

On Linux and Mac based systems unzip the ``bftools.zip`` file into a
memorable location, for example a directory named ``tools``.

::

    mkdir ~/tools
    mv ~/Downloads/bftools.zip ~/tools/
    cd ~/tools
    unzip bftools.zip

Finally add the ``bftools`` directory to your ``PATH``.

::

    export PATH=$PATH:~/tools/bftools

.. note:: You may want to add the line above to your ``.bashrc`` file.

On Windows unzip the ``bftools.zip`` file to a memorable location, for
example the ``C:\`` drive and set the ``PATH`` appropriately::

    set PATH=C:\bftools;%PATH%

Install the :mod:`jicbioimage` package
--------------------------------------

Finally install the :mod:`jicbioimage` package using ``pip``.

::

    pip install jicbioimage.core
    pip install jicbioimage.transform
    pip install jicbioimage.segment
    pip install jicbioimage.illustrate


.. _Using Docker:

Using Docker
^^^^^^^^^^^^

`Docker <https://www.docker.com/>`_ is a technology that allows one
to package software along with all its dependencies in a fashion that
ensures that the software will always run the same.

For this purpose we have created the ``jicscicomp/bioformats`` docker
image. It contains all the :mod:`jicbioimage` dependencies, but not
the :mod:`jicbioimage` package itself. You can find out how this Docker image
was built in the `JIC-CSB/scicomp_docker <https://github.com/JIC-CSB/scicomp_docker>`_
GitHub repository.

If you are already familiar with Docker you can try it out using the command
below.

.. code-block:: none

    $ docker run -it --rm jicscicomp/bioformats
    [root@03fda753e799 /]# pip install jicbioimage.core
    [root@03fda753e799 /]# pip install jicbioimage.transform
    [root@03fda753e799 /]# pip install jicbioimage.segment
    [root@03fda753e799 /]# pip install jicbioimage.illustrate

If you have not used Docker before you will need to install it.
On Mac and Windows download and install the
`Docker Toolbox <https://www.docker.com/products/docker-toolbox>`_.
Docker runs natively on Linux, but you will need to install it,
see the `Docker Installation Notes <https://docs.docker.com/engine/installation/>`_.

For our image analysis projects we tend to create three directories
in our project: ``scripts`` (where we put the Python scripts),
``data`` (where we put the raw images) and ``output`` (where our scripts
write their output). When then use a bash script along the lines of the
below to launch a container that has access to these directories
(read only for the ``data`` and ``scripts`` directories).

.. code-block:: bash

    #!/bin/bash

    docker run -it --rm -v `pwd`/data:/data:ro  \
                        -v `pwd`/scripts:/scripts:ro  \
                        -v `pwd`/output:/output jicscicomp/bioformats

You will have noticed that we did not include the :mod:`jicbioimage` package in
the ``jicscicomp/bioformats`` Docker image. The reason for this is that we like
to create a specific Docker image for each bioimage analysis project.

If you want to do this you need to create a directory for your Docker image, for
example ``cell_analysis``. In that directory you then create a ``requirements.txt``
file with all your Python requirements, e.g.:

.. code-block:: none

    jicbioimage.core
    jicbioimage.transform
    jicbioimage.segment
    jicbioimage.illustrate

And a ``Dockerfile`` containing the instructions below.

.. code-block:: none

    FROM jicscicomp/bioformats

    COPY requirements.txt .
    RUN pip install -r requirements.txt

You can now use this setup to build your own Docker image using the command below.

.. code-block:: none

    docker build -t cell_analysis .

Now you can update your bash script to make use of your custom built image,
tagged ``cell_analysis``.

.. code-block:: bash

    #!/bin/bash

    docker run -it --rm -v `pwd`/data:/data:ro  \
                        -v `pwd`/scripts:/scripts:ro  \
                        -v `pwd`/output:/output cell_analysis

In our day to day work, providing bioimage analysis support across the John Innes Centre,
we have templated much of our initial project setup using
`Cookiecutter <https://cookiecutter.readthedocs.io>`_. For some inspiration you may
want to install Cookiecutter and create a project setup using our
`JIC-Image-Analysis/cookiecutter-image-analysis <https://github.com/JIC-Image-Analysis/cookiecutter-image-analysis>`_ template hosted on GitHub.
The command below uses Cookiecutter to create a new project using this template.

.. code-block:: none

    $ cookiecutter gh:JIC-Image-Analysis/cookiecutter-image-analysis

Enjoy!
