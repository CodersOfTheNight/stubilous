# -*- coding: utf-8 -*-
from setuptools import setup
from pip.req import parse_requirements

install_reqs = list(parse_requirements("requirements.txt", session={}))


def version():
    from stubilous import version
    return version.get_version()


setup(name="stubilous",
      version=version(),
      description="A plain simple Python http stub server",
      author="Šarūnas Navickas",
      author_email="zaibacu@gmail.com",
      url="https://github.com/CodersOfTheNight/stubilous",
      license="MIT",
      packages=["stubilous"],
      setup_requires=[str(ir.req) for ir in install_reqs] + ["pytest-runner"],
      test_suite="pytest",
      tests_require=["pytest", "requests"])
