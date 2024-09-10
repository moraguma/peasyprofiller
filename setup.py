# setup.py

from setuptools import setup, find_packages

setup(
    name='peasyprofiller',
    version='0.1.0',    
    description='Easy and simple profiller for Python',
    url='https://github.com/moraguma/peasyprofiller',
    author='Moraguma',
    author_email='g170603@dac.unicamp.br',
    license='MIT',
    packages=["peasyprofiller", "peasyprofiller.tests"],
    install_requires=[
        'setuptools>=70.0.0'           
    ],

		# Full list @ https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',  
        'Programming Language :: Python' 
    ],
)
