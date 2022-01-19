from setuptools import find_namespace_packages, setup
from emmet.builders import __version__ as fallback_version
from emmet.core import __version__ as core_version

if "+" in fallback_version:
    fallback_version = fallback_version.split("+")[0]

if "+" in core_version:
    core_version = core_version.split("+")[0]

setup(
    name="emmet-builders",
    use_scm_version={
        "root": "..",
        "relative_to": __file__,
        "write_to": "emmet-builders/emmet/builders/_version.py",
        "write_to_template": '__version__ = "{version}"',
        "fallback_version": fallback_version,
    },
    setup_requires=["setuptools_scm"],
    description="Builders for the Emmet Library",
    author="The Materials Project",
    author_email="feedback@materialsproject.org",
    url="https://github.com/materialsproject/emmet",
    packages=find_namespace_packages(include=["emmet.*"]),
    install_requires=[f"emmet-core~={core_version}", "maggma>=0.38.1"],
    python_requires=">=3.8",
    license="modified BSD",
    zip_safe=False,
)
