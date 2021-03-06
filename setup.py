from setuptools import setup, find_packages
import codecs
from os import path

here = path.abspath(path.dirname(__file__))

with codecs.open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='loadleveler-client',

    version='1.0.0',

    description='Loadleveler Client',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/nwpc-oper/loadleveler-client',

    author='perillaroc',
    author_email='perillaroc@gmail.com',

    license='GPL-3.0',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],

    keywords='nwpc loadleveler client',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    include_package_data=True,
    package_data={
        'loadleveler_client': ['conf/*.yml']
    },

    install_requires=[
        'pyyaml',
        'click',
        'nwpc-hpc-model<=0.3.2'
    ],

    entry_points={
        'console_scripts': [
            'llclient=loadleveler_client.llclient:cli'
        ]
    }
)
