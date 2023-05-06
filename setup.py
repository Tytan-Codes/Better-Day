from setuptools import setup, find_packages

setup(
    name='Better Day',
    version='4.5.6',
    description='It makes your day better',
    long_description='It is made in python 3 and it makes your day easier as a developer by giving you things that you will use faster and at you finger tips.',
    author='Tytan Codes',
    author_email='spam@thetytan.com',
    url='https://github.com/tytan-codes/better-day',
    packages=find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
    install_requires=[
        "openai",
        "colorama",
        "argparse"
    ],
)
