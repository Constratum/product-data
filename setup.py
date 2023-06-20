from setuptools import setup, find_packages

setup(
    name="product-data",
    version="0.19",
    packages=find_packages(),
    install_requires=["pandas"],
    package_data={"": ["*.csv"]},
    include_package_data=True,
    license="Creative Commons Attribution-Noncommercial-Share Alike license",
)
