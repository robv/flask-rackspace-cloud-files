"""
Flask-RSF
-------------

Easily serve your static files from Rackspace Cloud Files.
"""
from setuptools import setup


setup(
    name='Flask-RSF',
    version='0.1.1',
    url='http://github.com/robv/flask-rackspace-cloud-files',
    license='WTFPL',
    author='Robert Velasquez',
    author_email='thisisrobv@gmail.com',
    description='Seamlessly serve the static files of your Flask app from Rackspace Cloud Files',
    long_description=__doc__,
    py_modules=['fask_rsf'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'pyrax'
    ],
    tests_require=['nose', 'mock'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
