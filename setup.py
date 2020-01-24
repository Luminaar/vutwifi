from distutils.core import setup

setup(
    name="vutwifi",
    author="Thomas Levine, Max K. Luminar",
    author_email="kovykmax@gmail.com",
    description="Connect to the WIFI at FIT VUT in Brno.",
    url="https://github.com/luminaar/vutwifi",
    py_modules=["vutwifi"],
    install_requires=["requests>=2.22, <3.0", "click>=7.0, <8.0",],
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={"console_scripts": ["vutwifi = vutwifi:cli"]},
    version="0.3",
    license="AGPL",
)
