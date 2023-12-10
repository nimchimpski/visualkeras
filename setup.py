import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="visualkeras_mod",
    version="0.1.0-alpha",
    author="Paul Gavrikov, modified by nimchimpski",
    author_email="paul.gavrikov@hs-offenburg.de, alex@nimchimpski.com",
    description="Architecture visualization of Keras models - updtated to work PILL 8.0.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/paulgavrikov/visualkeras",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pillow>=10.1.0',
        'numpy>=1.26.2',
        'aggdraw>=1.3.18'
    ],
    python_requires='>=3.6',
)