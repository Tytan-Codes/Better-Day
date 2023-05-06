from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='Better Day',
    version='4.5.6',
    description='It makes your day better',
    long_description=long_description,
    long_description_content_type='text/x-rst',
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
