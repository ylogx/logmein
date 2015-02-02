from distutils.core import setup

add_keywords = dict(
    entry_points = {
        'console_scripts': ['logmein = logmein.main:main'],
    },
)

setup(
        name='LogMeIn',
        description='Log in to networks',
        version='0.1.1',
        packages=['logmein'],
        license='GPLv3+',
        author='Shubham Chaudhary',
        author_email='me@shubhamchaudhary.in',
        url='https://github.com/shubhamchaudhary/logmein',
        long_description=open('README.txt').read(),
        **add_keywords
)

