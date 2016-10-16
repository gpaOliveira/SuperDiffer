import os
from setuptools import setup,find_packages

project_name  =  "SuperDiffer"
__version__  =  "1.0.0"
__author__  =  "Gabriel Oliveira"
__author_email__  =  "gabriel.pa.oliveira@gmail.com"
__author_username__  =  "gpaOliveira"
__description__  =  "REST Service to calculate the difference between two input strings"

#adapted from https://pythonhosted.org/an_example_pypi_project/setuptools.html
def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except:
        pass
    return ""

setup(
    author = __author__,
    author_email = __author_email__,
    description = __description__,
    install_requires = read("requirements.txt"),
    license = read("LICENSE"),
    long_description = read("README.md"),
    name = project_name,
    packages = find_packages(),
    platforms = ["any"],
    test_suite = "nose2.collector.collector",
    url = "https://github.com/" + __author_username__ + "/" + project_name,
    version = __version__,
    classifiers = [
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ]
)