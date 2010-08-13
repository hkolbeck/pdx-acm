from setuptools import setup, find_packages

readme = open('README.rst')

setup(name="pdxacm",
      version="dev",
      packages=find_packages(),
      namespace_packages=['pdxacm'],
      include_package_data=True,
      author='Dan Colish',
      author_email='dcolish@gmail.com',
      description='Portland State ACM Website',
      long_description=readme.read(),
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

readme.close()
