"""
Portland State ACM
------------------

This is the code repository for Portland State's ACM chapter website. Clearly
this code is very new and experimental. If you try to use it don't always expect
it to work correctly. In other words, YRMV. To install checkout this repo and
run::

  python setup.py develop


Links
`````

* `development version
  <http://github.com/dcolish/pdx-acm/zipball/master#egg=pdxacm-dev>`_

"""
from setuptools import setup, find_packages

setup(name="pdxacm",
      version="dev",
      packages=find_packages(),
      namespace_packages=['pdxacm'],
      include_package_data=True,
      author='Dan Colish',
      author_email='dcolish@gmail.com',
      description='Portland State ACM Website',
      long_description=__doc__,
      zip_safe=False,
      platforms='any',
      license='BSD',
      url='http://www.github.com/dcolish/pdx-acm',

      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Environment :: Console',
        'Intended Audience :: Education',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Operating System :: Unix',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],

      extras_require={
        'doc': ['sphinx', 'Sphinx-PyPI-upload'],
        },

      install_requires=[
        'flask',
        'Flask-Markdown==dev',
        'Flask-SQLAlchemy',
        'Flask-Script',
        'flatland',
        'SQLAlchemy',
        ],

      test_suite="nose.collector",
      tests_require=[
        'nose',
        'alfajor',
        ],
      )
