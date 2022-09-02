from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.3'
DESCRIPTION = 'Package for cricket analytics'
LONG_DESCRIPTION = 'Visualizaiton, Analysis, and more (will add later)'

# Setting up
setup(
    name="criccatapult",
    version=VERSION,
    author="Aadrij Upadya, Pradyum Chitlu",
    author_email="<adrij2005@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'matplotlib',
                      'requests', 'bs4', 'geocoder', 'folium', 'geopandas', 'seaborn', 'pygame', 'pipwin', 'gdal', 'fiona', 'shapely'],
    keywords=['python', 'cricket', 'sports analytics',
              'data analytics', 'visualiation', 'geospatial data', 'GIS'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
