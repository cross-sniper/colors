from setuptools import setup, find_packages

setup(
    name='colors',
    version='0.0.1',
    author='cross-sniper',
    author_email='cts.contact.br@email.com',
    description='A Python package for printing colored text.',
    long_description='A package that provides functions to print text in various colors using ANSI escape codes.',
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        # List any dependencies here
    ],
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
)
