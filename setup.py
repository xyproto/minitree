# -*- coding: utf-8 -*-
import os
import sys

from setuptools import setup

setup(name="minitree",
      version="0.4.1",
      description="List files in columns",
      url="https://github.com/xyproto/minitree",
      author="Alexander F. Rødseth",
      author_email="xyproto@archlinux.org",
      license="MIT",
      py_modules=["mt"],
      entry_points={
        "console_scripts" : [
            "mt = mt:main",
        ]
      },
      classifiers=[
          "Environment :: Console",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          "Topic :: System :: Shells",
          "Topic :: Utilities",
      ]
)
