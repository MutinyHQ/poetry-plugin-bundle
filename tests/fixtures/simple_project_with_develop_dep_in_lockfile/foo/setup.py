from __future__ import annotations

from distutils.core import setup


setup(
    name="foo",
    version="1",
    py_modules=["demo"],
    package_dir={"src": "src"},
    install_requires=[],
)
