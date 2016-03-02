from setuptools import setup

readme = open('README.rst').read()

version = "0.10.1"

setup(name='jicbioimage',
      packages=['jicbioimage', ],
      version=version,
      description='Python package designed to make it easy to work with bio images.',
      long_description=readme,
      author='Tjelvar Olsson',
      author_email = 'tjelvar.olsson@jic.ac.uk',
      url = 'https://github.com/JIC-CSB/jicbioimage',
      download_url = 'https://github.com/JIC-CSB/jicbioimage/tarball/{}'.format(version),
      license='MIT',
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Image Recognition",
      ],
      keywords = ['microscopy', 'image analysis'],
)
