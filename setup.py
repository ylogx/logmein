from distutils.core import setup

add_keywords = dict(
    entry_points={
        'console_scripts': ['logmein = logmein.main:main'],
    }, )

fhan = open('requirements.txt', 'rU')
requires = [line.strip() for line in fhan.readlines()]
fhan.close()
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    fhan = open('README.txt')
    long_description = fhan.read()
    fhan.close()

setup(
    name='LogMeIn',
    description='Log in to networks',
    version='0.1.2',
    packages=['logmein'],
    license='GPLv3+',
    author='Shubham Chaudhary',
    author_email='me@shubhamchaudhary.in',
    url='https://github.com/shubhamchaudhary/logmein',
    long_description=long_description,
    install_requires=requires, **add_keywords)
