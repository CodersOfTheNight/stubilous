from setuptools import setup
from pip.req import parse_requirements

install_reqs = list(parse_requirements("requirements.txt", session={}))


def version():
    import version
    return version.get_version()


setup(name="stubilous",
      version=version(),
      description="A plain simple Python http stub server",
      author="Šarūnas Navickas",
      author_email="zaibacu@gmail.com",
      url="https://github.com/CodersOfTheNight/stubilous",
      license="MIT",
      packages=["stubilous"],
      install_requires=[str(ir.req) for ir in install_reqs],
      test_suite="nose.collector",
      tests_require=["nose"])
