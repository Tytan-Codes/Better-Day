from setuptools import setup, find_packages

setup(
    name='example-package',
    version='0.1.0',
    description='A short description of your package',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/your-username/example-package',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
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
        # add your package dependencies here
        platform
        openai
        colorama
        signal
        argparse
    ],
)
