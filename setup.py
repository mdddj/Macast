"""
This is a setup.py script

"""

import os
from setuptools import setup, find_packages

VERSION = "0.0.0"
with open('macast/.version', 'r') as f:
    VERSION = f.read().strip()
LONG_DESCRIPTION = ""
with open('README.md', 'r', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()
OPTIONS = {}
INSTALL = [
    "appdirs>=1.4.4,<2",
    "CherryPy>=18.8,<19",
    "lxml>=5,<7",
    "netifaces>=0.11,<1",
    "requests>=2.31,<3",
    "pyperclip>=1.9,<2",
    "rumps>=0.4,<0.5; sys_platform == 'darwin'",
    "Pillow>=10,<13; sys_platform != 'darwin'",
    "pystray>=0.19.5,<0.20; sys_platform != 'darwin'",
    "pywin32>=306; sys_platform == 'win32'",
]
PACKAGES = find_packages()

setup(
    name="macast",
    version=VERSION,
    author="xfangfang",
    author_email="xfangfang@126.com",
    description="a DLNA Media Renderer",
    license="GPL3",
    url="https://github.com/mdddj/Macast",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    classifiers=["Topic :: Multimedia :: Sound/Audio",
                 "Topic :: Multimedia :: Video",
                 'Programming Language :: Python :: 3 :: Only',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.10',
                 'Programming Language :: Python :: 3.11',
                 'Programming Language :: Python :: 3.12',
                 'Programming Language :: Python :: 3.13',
                 'Programming Language :: Python :: 3.14',
                 'Operating System :: MacOS :: MacOS X',
                 'Operating System :: Microsoft :: Windows :: Windows NT/2000',
                 'Operating System :: POSIX',
                 ],
    platforms=["MacOS X", "Windows", "POSIX"],
    keywords=["mpv", "dlna", "renderer"],
    options=OPTIONS,
    install_requires=INSTALL,
    packages=PACKAGES,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'macast-cli = macast.macast:cli',
            'macast-gui = macast.macast:gui'
        ]
    },
    python_requires=">=3.10",
)
