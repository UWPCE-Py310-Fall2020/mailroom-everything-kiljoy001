import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='mailroom-pkg-kiljoy001',
    version='0.0.1',
    author='Scott J Guyton',
    author_email='kiljoy001@gmail.com',
    description='A small program to record donations',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/UWPCE-Py310-Fall2020/mailroom-everything-kiljoy001',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    scripts=['bin/mailroom.py']
)
