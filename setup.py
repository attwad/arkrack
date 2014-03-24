try:
    from setuptools import setup
    test_extras = {
        'test_suite': 'arkrack.test',
    }
except ImportError:
    from distutils.core import setup
    test_extras = {}


setup(
    name='arkrack',
    version='1.0',
    author='attwad',
    author_email='tmusoft@gmail.com',
    description=(
        'Intelligently crawls the internet and tries crawled words as '
        'password for a given protected archive.'),
    long_description=open('README.rst').read(),
    url='https://github.com/attwad/arkrack',
    platforms='any',
    packages=[
        'arkrack',
        'arkrack.crackers',
        'arkrack.test',
        'arkrack.test.crackers',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Topic :: Security',
        'Topic :: System :: Networking',
    ],
    **test_extras
)
