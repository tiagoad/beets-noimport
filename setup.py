from setuptools import setup

setup(
    name='beets-noimport',
    version='0.1.0-beta',
    description='add directories to the incremental import "do not import" list',
    long_description=open('README.md').read(),
    author='Tiago Dias',
    author_email='tiagoadias@gmail.com',
    url='http://www.github.com/ttsda/beets-noimport',
    license='MIT',
    platforms='ALL',

    packages=['beetsplug'],

    install_requires=[
        'beets>=1.3.7'
    ],

    classifiers=[
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Players :: MP3',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        ],
    )
