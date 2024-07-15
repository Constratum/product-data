from setuptools import setup, find_packages

setup(
    name="product_data",
    version="0.048",
    packages=find_packages(),
    install_requires=["pandas"],
    package_data={"": ["*.csv"]},
    include_package_data=True,
)
