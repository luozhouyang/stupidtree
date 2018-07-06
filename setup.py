import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stupidtree",
    version="0.1.0",
    description="A generic tree implementation in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/luozhouyang/stupidtree",
    author="ZhouYang Luo",
    author_email="stupidme.me.lzy@gmail.com",
    packages=setuptools.find_packages(),
    include_package_data=True,
    license="MIT License",
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    )
)
