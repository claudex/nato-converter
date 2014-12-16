#!/usr/bin/env python

from distutils.core import setup

if __name__ == '__main__':
    setup(name="Nato_converter",
            version="0.1",
            description="Convert list of character to the equivalent in Nato"+
            "alphabet",
            author="Xavier Claude",
            author_email="contact+python@xavierclaude.be",
            url="todo",
            license="GPL2+",
            scripts=["nato_converter.py"],
            )
